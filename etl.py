"""
Data Engineer Take-Home Test - ETL Pipeline
============================================

Functional ETL pipeline for processing travel booking data from SQLite.
Clear separation of concerns with defensive data handling.

Pipeline flow: load_data -> clean_bookings -> enrich_with_destinations
    -> transform_data -> save_to_db
"""

import sqlite3
from typing import Tuple

import pandas as pd

from config import DATABASE_PATH, CLEAN_TABLE_NAME

# Fixed exchange rates to EUR. Kept simple for the exercise; in production
# these would come from an external service or config.
CURRENCY_RATES = {
    "EUR": 1.0,
    "USD": 0.92,
    "GBP": 1.15,
}


def load_data(conn: sqlite3.Connection) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Load raw_bookings and destinations from the database.

    Connection is passed in from main() to avoid opening/closing repeatedly
    and to support running multiple operations in one session.

    Args:
        conn: Active SQLite database connection

    Returns:
        Tuple of (bookings DataFrame, destinations DataFrame)
    """
    bookings = pd.read_sql("SELECT * FROM raw_bookings", conn)
    destinations = pd.read_sql("SELECT * FROM destinations", conn)
    return bookings, destinations


def clean_bookings(bookings: pd.DataFrame) -> pd.DataFrame:
    """
    Clean booking data: handle duplicates, standardize dates, handle missing values.

    Duplicate rule: same booking_id appears multiple times with different
    booking_date. The latest record is kept as the authoritative one.
    """
    # --- Duplicates ---
    # Sort by booking_date so the "last" row is the most recent.
    # keep="last" retains the latest booking per booking_id.
    bookings = bookings.sort_values("booking_date")
    bookings = bookings.drop_duplicates(subset="booking_id", keep="last")

    # --- Dates ---
    # Raw data has mixed formats: ISO (2025-08-14), European (14/12/2025),
    # and text (Dec 25, 2025). dayfirst=True correctly parses dd/mm/yyyy.
    # errors="coerce" turns invalid dates into NaT instead of raising.
    date_cols = ["booking_date", "start_date", "end_date"]
    for col in date_cols:
        bookings[col] = pd.to_datetime(bookings[col], errors="coerce", dayfirst=True)

    # Rows with null start_date or end_date cannot be used for duration
    # or trip logic, so they are dropped.
    bookings = bookings.dropna(subset=["start_date", "end_date"])

    # --- Missing values ---
    # Currency: default to EUR when null, since it is the business base.
    # Price: drop rows with null price — revenue metrics need valid amounts.
    bookings["currency"] = bookings["currency"].fillna("EUR")
    bookings = bookings.dropna(subset=["price"])

    return bookings


def enrich_with_destinations(
    bookings: pd.DataFrame, destinations: pd.DataFrame
) -> pd.DataFrame:
    """
    Enrich bookings with destination info via left join on destination_id.

    Left join keeps all bookings even when destination_id has no match.
    Missing destinations get "Unknown" to preserve rows while flagging the gap.
    """
    bookings = bookings.merge(
        destinations,
        how="left",
        on="destination_id",
    )
    bookings["destination_name"] = bookings["destination_name"].fillna("Unknown")
    return bookings


def transform_data(bookings: pd.DataFrame) -> pd.DataFrame:
    """
    Add derived fields: price_eur and trip_duration_days.
    """
    # Convert all prices to EUR using the fixed rate for each currency.
    # .get(x["currency"], 1.0) falls back to 1.0 for unexpected currencies.
    bookings["price_eur"] = bookings.apply(
        lambda x: x["price"] * CURRENCY_RATES.get(x["currency"], 1.0),
        axis=1,
    )

    # Compute trip length in days. Dates are already datetime from clean_bookings.
    bookings["trip_duration_days"] = (
        bookings["end_date"] - bookings["start_date"]
    ).dt.days

    return bookings


def save_to_db(bookings: pd.DataFrame, conn: sqlite3.Connection) -> None:
    """
    Write the final DataFrame to the clean_bookings table.

    if_exists="replace" overwrites the table on each run so the output
    is always fresh. Wrapped in try/except to raise a clear error on failure.
    """
    try:
        bookings.to_sql(
            CLEAN_TABLE_NAME,
            conn,
            if_exists="replace",
            index=False,
        )
        print(f"Saved {len(bookings)} rows to '{CLEAN_TABLE_NAME}'")
    except Exception as e:
        raise RuntimeError(f"Failed to save to database: {e}") from e


def main() -> None:
    """
    Run the full ETL pipeline: load, clean, enrich, transform, save.
    """
    conn = sqlite3.connect(DATABASE_PATH)

    bookings, destinations = load_data(conn)
    bookings = clean_bookings(bookings)
    bookings = enrich_with_destinations(bookings, destinations)
    bookings = transform_data(bookings)
    save_to_db(bookings, conn)

    conn.close()
    print("ETL pipeline completed successfully!")


if __name__ == "__main__":
    main()

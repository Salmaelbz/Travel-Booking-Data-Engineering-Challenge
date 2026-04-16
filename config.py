# =============================================================================
# Configuration for the ETL pipeline
# =============================================================================
# Centralizes paths and table names so they can be changed in one place.
# Used by etl.py for database connection and output table naming.
# =============================================================================

# Path to the SQLite database file. Contains raw_bookings and destinations
# as inputs; clean_bookings is created by the ETL as output.
DATABASE_PATH = "bookings.db"

# Name of the table where the cleaned and enriched data is written.
# Replaced on each ETL run (if_exists="replace").
CLEAN_TABLE_NAME = "clean_bookings"

# Expected columns for the final clean_bookings table.
# Useful for validation or documentation. The ETL enriches raw_bookings
# with destination fields and adds price_eur, trip_duration_days.
REQUIRED_BOOKING_COLUMNS = [
    "booking_id",
    "customer_email",
    "destination_id",
    "booking_date",
    "start_date",
    "end_date",
    "price",
    "currency",
    "number_of_travelers",
]

# Columns in the destinations reference table. Joined to bookings
# on destination_id to add destination_name, country, region.
REQUIRED_DESTINATION_COLUMNS = [
    "destination_id",
    "destination_name",
    "country",
    "region",
    "exchange_rate_to_eur",
]

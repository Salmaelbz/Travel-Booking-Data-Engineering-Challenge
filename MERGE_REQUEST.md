# Merge Request: Data Engineer Take-Home - ETL Pipeline & SQL Analysis

##  Approach

- **Functional ETL pipeline** – Clear, testable functions without OOP overhead
- **Clear separation of concerns** – `load_data` → `clean_bookings` → `enrich_with_destinations` → `transform_data` → `save_to_db`
- **Defensive data handling** – Robust handling of invalid dates, missing values, and duplicates

##  Data Quality Issues Found

- **Duplicate booking IDs** – Same `booking_id` appears multiple times with different `booking_date` values
- **Mixed date formats** – Inconsistent date strings requiring standardization
- **Missing currency and price values** – Nulls in `currency` and `price` columns
- **Inconsistent destination references** – Bookings referencing non-existent `destination_id` values

##  Decisions & Assumptions

| Issue | Decision | Rationale |
|-------|----------|-----------|
| Duplicate `booking_id` | Kept **latest** booking per `booking_id` | Most recent record assumed authoritative |
| Invalid/missing dates | Dropped rows where `start_date` or `end_date` is null | Trip dates are critical; cannot derive meaningful metrics without them |
| Missing currency | Assumed **EUR** | Default currency for the business context |
| Missing price | Dropped row | Revenue metrics require valid prices |
| Missing destination | Filled with `"Unknown"` | Preserve booking for analysis while flagging data gap |
| Currency conversion | Used fixed exchange rates (EUR, USD, GBP) | Simplicity; production would use external service |

##  Improvements if Given More Time

- **External currency service** – Real-time or daily FX rates instead of hardcoded values
- **Schema validation** – Great Expectations or Pydantic for data contract validation
- **Incremental loads** – Process only new/changed records for large datasets
- **Logging & monitoring** – Structured logging, metrics, and alerting for production pipelines

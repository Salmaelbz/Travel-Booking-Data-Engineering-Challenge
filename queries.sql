-- =============================================================================
-- Data Engineer Take-Home Test - SQL Analysis Query
-- =============================================================================
-- Run this query against the 'clean_bookings' table created by the ETL pipeline.
-- Ensure the ETL has been executed first (python etl.py).
-- =============================================================================


-- =============================================================================
-- Query: Revenue by Destination
-- =============================================================================
-- Computes revenue metrics per destination:
--   - Total revenue (sum of price_eur for all bookings)
--   - Number of bookings (count)
--   - Average booking value (avg of price_eur)
--
-- Requirements:
--   - Only destinations with MORE THAN 5 bookings (HAVING clause)
--   - Ordered by total revenue, highest first
--   - Destination name and country included in results
--
-- Note: price_eur is added by the ETL so all amounts are comparable in EUR.
-- GROUP BY destination_name, country handles cases where the same name
-- might exist in different countries.
-- =============================================================================

SELECT
    destination_name,
    country,
    COUNT(*) AS booking_count,
    SUM(price_eur) AS total_revenue,
    AVG(price_eur) AS avg_booking_value
FROM clean_bookings
GROUP BY destination_name, country
HAVING COUNT(*) > 5
ORDER BY total_revenue DESC;

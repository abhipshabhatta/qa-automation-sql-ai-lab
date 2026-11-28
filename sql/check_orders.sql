
-- Show orders and calculate how much is still unpaid.

SELECT
    customer,
    item,
    total_cents,
    paid_cents,
    total_cents - paid_cents AS remaining_cents,
    status
FROM orders
ORDER BY id DESC;

-- Missing mandatory fields
SELECT *
FROM customer
WHERE first_name IS NULL
   OR phone IS NULL;

-- Invalid phone numbers
SELECT *
FROM customer
WHERE length(phone) < 10;

-- Birthdate sanity check
SELECT *
FROM customer
WHERE birthdate > CURRENT_DATE;

-- Duplicate phones (should not exist)
SELECT phone, COUNT(*)
FROM customer
GROUP BY phone
HAVING COUNT(*) > 1;

SELECT name as name, MAX(customers_number) as customers_number FROM lawyers
UNION
SELECT name as name, MIN(customers_number) as customers_number FROM lawyers
UNION
SELECT 'Average' AS name, ROUND(AVG(customers_number),0) FROM lawyers;

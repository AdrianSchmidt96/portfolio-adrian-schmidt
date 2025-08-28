
SELECT 
	COUNT(*) AS transaction_count,
	customer_id,
	SUM(amount) AS amount_sum,
	RANK() OVER(ORDER BY COUNT(*) DESC , SUM(amount) DESC) AS rank_night
FROM "raw".transaction_customer_card
WHERE t_hour = 23 OR t_hour BETWEEN 0 AND 5
GROUP BY customer_id
HAVING COUNT(*) > 100 AND SUM(amount) >10000
ORDER BY COUNT(*) DESC, amount_sum DESC
LIMIT 20

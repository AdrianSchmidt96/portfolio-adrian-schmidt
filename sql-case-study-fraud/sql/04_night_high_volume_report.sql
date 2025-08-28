WITH ids(id) AS(
	VALUES(114),(1718),(641),(461),(1797),(1686),(121),(316),(947),(1989),(503),(301),(1293),(474),(421),(52),(81),(1451),(1629),(1437)
)


SELECT 
	customer_id,
	amount,
	transaction_date,
	t_hour,
	merchant_city,
	card_brand,
	card_type,
	errors
FROM "raw".transaction_customer_card
WHERE customer_id IN (SELECT id from ids) AND t_hour IN (23,0,1,2,3,4,5)



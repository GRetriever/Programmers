-- 코드를 입력하세요
WITH DISCOUNT AS (
    SELECT DURATION_TYPE, (1-(DISCOUNT_RATE * 0.01)) AS RATE
    FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN
    WHERE CAR_TYPE = '트럭'
    )

SELECT HISTORY_ID, ROUND(DAILY_FEE * CASE
                        WHEN DIFF >= 90 THEN (SELECT RATE
                                             FROM DISCOUNT
                                             WHERE DURATION_TYPE = '90일 이상')
                        WHEN DIFF >= 30 THEN (SELECT RATE
                                             FROM DISCOUNT
                                             WHERE DURATION_TYPE = '30일 이상')
                        WHEN DIFF >= 7 THEN (SELECT RATE
                                            FROM DISCOUNT
                                            WHERE DURATION_TYPE = '7일 이상')
                         ELSE 1 
                         END * DIFF) AS FEE
FROM (SELECT CAR_TYPE,
            DAILY_FEE,
            HISTORY_ID,
            DATEDIFF(END_DATE,START_DATE) + 1 AS DIFF
      FROM CAR_RENTAL_COMPANY_CAR
      JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY
            USING (CAR_ID)
     ) AS CAR
WHERE CAR_TYPE = '트럭'
ORDER BY FEE DESC, HISTORY_ID DESC
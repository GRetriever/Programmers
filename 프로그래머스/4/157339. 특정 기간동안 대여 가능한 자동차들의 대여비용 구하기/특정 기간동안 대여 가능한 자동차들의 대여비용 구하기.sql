-- 코드를 입력하세요
WITH DISCOUNT AS (
    select CAR_TYPE, (1-(DISCOUNT_RATE * 0.01)) AS RATE
    from CAR_RENTAL_COMPANY_DISCOUNT_PLAN
    where DURATION_TYPE = '30일 이상'
    )

SELECT A.CAR_ID, A.CAR_TYPE, ROUND(30 * A.DAILY_FEE * C.RATE) AS FEE
FROM CAR_RENTAL_COMPANY_CAR A
JOIN DISCOUNT C ON A.CAR_TYPE = C.CAR_TYPE
WHERE A.CAR_TYPE IN ('세단','SUV')
        AND ROUND(30 * A.DAILY_FEE * C.RATE) >= 500000
        AND ROUND(30 * A.DAILY_FEE * C.RATE) < 2000000
        AND CAR_ID NOT IN (select DISTINCT CAR_ID
                            from CAR_RENTAL_COMPANY_RENTAL_HISTORY
                            where END_DATE >= '2022-11-01'
                            )
ORDER BY FEE DESC, A.CAR_TYPE, A.CAR_ID DESC

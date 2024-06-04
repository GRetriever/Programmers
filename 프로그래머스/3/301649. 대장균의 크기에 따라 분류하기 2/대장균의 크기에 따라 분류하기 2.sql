-- 코드를 작성해주세요
WITH RANKING AS (
        select ID, PERCENT_RANK() OVER(ORDER BY SIZE_OF_COLONY DESC) AS SIZE_RANK
        from ECOLI_DATA
        )

SELECT ID, CASE
            WHEN SIZE_RANK <= 0.25 THEN 'CRITICAL'
            WHEN SIZE_RANK <= 0.50 THEN 'HIGH'
            WHEN SIZE_RANK <= 0.75 THEN 'MEDIUM'
            ELSE 'LOW'
            END AS COLONY_NAME
FROM RANKING
ORDER BY ID
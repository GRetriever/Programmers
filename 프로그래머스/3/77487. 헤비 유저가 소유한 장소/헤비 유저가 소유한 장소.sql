-- 코드를 입력하세요
SELECT *
FROM PLACES
WHERE (HOST_ID) IN (
        select HOST_ID
        from Places
        group by HOST_ID
        having COUNT(HOST_ID) >= 2
        )
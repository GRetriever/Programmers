-- 코드를 입력하세요
SELECT A.NAME,A.DATETIME
FROM ANIMAL_INS A
LEFT JOIN ANIMAL_OUTS B ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE SEX_UPON_OUTCOME IS NULL
ORDER BY 2
LIMIT 3
-- 코드를 입력하세요
SELECT ANIMAL_TYPE,COUNT(1) AS count
FROM ANIMAL_INS
WHERE ANIMAL_TYPE = 'Dog' OR ANIMAL_TYPE = 'Cat'
GROUP BY ANIMAL_TYPE
ORDER BY 1
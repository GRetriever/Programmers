-- 코드를 작성해주세요
WITH HR_GRADE_GROUP AS (
    select EMP_NO, CASE
            WHEN AVG(SCORE) >= 96 THEN 'S'
            WHEN AVG(SCORE) >= 90 THEN 'A'
            WHEN AVG(SCORE) >= 80 THEN 'B'
            ELSE 'C'
            END AS GRADE
    from HR_GRADE
    group by EMP_NO
    )
    
SELECT B.EMP_NO,
        B.EMP_NAME,
        GRADE,
        CASE
            WHEN GRADE = 'S' THEN B.SAL*0.2
            WHEN GRADE = 'A' THEN B.SAL*0.15
            WHEN GRADE = 'B' THEN B.SAL*0.1
            ELSE 0
            END AS BONUS
FROM HR_EMPLOYEES B
JOIN HR_GRADE_GROUP C ON B.EMP_NO = C.EMP_NO
ORDER BY B.EMP_NO
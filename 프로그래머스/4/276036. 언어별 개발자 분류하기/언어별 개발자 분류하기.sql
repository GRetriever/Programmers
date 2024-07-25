-- 코드를 작성해주세요
WITH
GRADE_A AS (
    SELECT CODE
    FROM SKILLCODES
    WHERE NAME = 'Python'
),
GRADE_B AS (
    SELECT CODE
    FROM SKILLCODES
    WHERE NAME = 'C#'
),
GRADE_C AS (
    SELECT SUM(CODE) AS CODE
    FROM SKILLCODES
    WHERE CATEGORY = 'Front End'
)

SELECT 
    CASE
        WHEN SKILL_CODE & GRADE_A.CODE && SKILL_CODE & GRADE_C.CODE THEN 'A'
        WHEN SKILL_CODE & GRADE_B.CODE THEN 'B'
        WHEN SKILL_CODE & GRADE_C.CODE THEN 'C'
    END AS GRADE,
    ID, EMAIL
FROM DEVELOPERS,GRADE_A,GRADE_B,GRADE_C
HAVING GRADE IS NOT NULL
ORDER BY GRADE, ID
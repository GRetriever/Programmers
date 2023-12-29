-- 코드를 입력하세요
# SELECT B.USER_ID,B.NICKNAME,
#     CONCAT(CITY,'',STREET_ADDRESS1,'',STREET_ADDRESS2) AS 전체주소,
#     CONCAT(SUBSTR(B.TLNO,1,3), '-',SUBSTR(B.TLNO,4,4),'-',SUBSTR(B.TLNO,8,4)) AS 전화번호
# FROM USED_GOODS_BOARD A 
# JOIN USED_GOODS_USER B
# ON A.WRITER_ID = B.USER_ID
# GROUP BY B.USER_ID
# HAVING COUNT(A.WRITER_ID) >= 3
# ORDER BY B.USER_ID DESC

SELECT 
    u2.user_id, 
    u2.nickname, 
    CONCAT_WS(' ', u2.city, u2.street_address1, u2.street_address2) 전체주소,
    CONCAT_WS('-', 
              SUBSTR(u2.tlno, 1, 3), 
              SUBSTR(u2.tlno, 4, LENGTH(u2.tlno) - 7), 
              SUBSTR(u2.tlno, -4, 4)) 전화번호
FROM used_goods_board u1
JOIN used_goods_user u2
ON u1.writer_id = u2.user_id
GROUP BY u2.user_id
HAVING count(u1.writer_id) >= 3
ORDER BY u2.user_id desc;
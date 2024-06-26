-- 코드를 작성해주세요
SELECT A.ITEM_ID,A.ITEM_NAME,A.RARITY
FROM ITEM_INFO A
JOIN ITEM_TREE B ON A.ITEM_ID = B.ITEM_ID
WHERE B.PARENT_ITEM_ID IN (
    select ITEM_ID
    from ITEM_INFO
    where RARITY = 'RARE')
ORDER BY 1 DESC
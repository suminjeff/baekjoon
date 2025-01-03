-- 코드를 입력하세요
# SELECT YEAR, MONTH, PURCHASED_USERS, PURCHASED_RATIO
SELECT YEAR(SALES_DATE) YEAR, MONTH(SALES_DATE) MONTH, COUNT(DISTINCT A.USER_ID) PURCHASED_USERS, ROUND(COUNT(DISTINCT A.USER_ID)/C.TOTAL_COUNT, 1) PUCHASED_RATIO
FROM (
    SELECT COUNT(DISTINCT USER_ID) TOTAL_COUNT
     FROM USER_INFO
     WHERE YEAR(JOINED) = 2021
     ) C,
ONLINE_SALE A
JOIN (
    SELECT USER_ID
    FROM USER_INFO
    WHERE YEAR(JOINED) = 2021
) B
ON A.USER_ID = B.USER_ID
GROUP BY MONTH(SALES_DATE)
ORDER BY YEAR, MONTH
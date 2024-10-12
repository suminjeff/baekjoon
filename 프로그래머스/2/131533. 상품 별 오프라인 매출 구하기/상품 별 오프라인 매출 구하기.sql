-- 코드를 입력하세요
SELECT PRODUCT_CODE, PRICE*SUM(SALES_AMOUNT) SALES
FROM PRODUCT A
LEFT JOIN OFFLINE_SALE B
ON A.PRODUCT_ID = B.PRODUCT_ID
WHERE B.PRODUCT_ID IS NOT NULL
GROUP BY A.PRODUCT_ID
ORDER BY SALES DESC, PRODUCT_CODE
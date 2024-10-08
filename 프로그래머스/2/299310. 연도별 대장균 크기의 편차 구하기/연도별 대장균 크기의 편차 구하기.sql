-- 코드를 작성해주세요

# SELECT CONCAT(DIFFERENTIATION_DATE, 4) YEAR, B.MAX_SIZE - A.SIZE_OF_COLONY YEAR_DEV, A.ID
SELECT B.YEAR AS YEAR, B.MAX_SIZE - A.SIZE_OF_COLONY AS YEAR_DEV, A.ID
FROM ECOLI_DATA A,
(
    SELECT YEAR(DIFFERENTIATION_DATE) YEAR, MAX(SIZE_OF_COLONY) MAX_SIZE
    FROM ECOLI_DATA
    GROUP BY YEAR
) B
WHERE YEAR(A.DIFFERENTIATION_DATE) = B.YEAR
ORDER BY YEAR, YEAR_DEV
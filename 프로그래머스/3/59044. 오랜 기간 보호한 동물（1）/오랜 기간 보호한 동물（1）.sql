-- 코드를 입력하세요
SELECT A.NAME, A.DATETIME
FROM ANIMAL_INS AS A
WHERE A.ANIMAL_ID NOT IN (
    SELECT B.ANIMAL_ID
    FROM ANIMAL_OUTS AS B
)
ORDER BY A.DATETIME ASC
LIMIT 3
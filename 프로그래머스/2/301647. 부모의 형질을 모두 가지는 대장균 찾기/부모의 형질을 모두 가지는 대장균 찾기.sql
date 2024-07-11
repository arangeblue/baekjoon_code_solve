-- 코드를 작성해주세요

SELECT B.ID, B.GENOTYPE, A.GENOTYPE AS PARENT_GENOTYPE
FROM ECOLI_DATA AS A, ECOLI_DATA AS B
WHERE B.PARENT_ID = A.ID 
    AND B.GENOTYPE & A.GENOTYPE = A.GENOTYPE
ORDER BY ID ASC;
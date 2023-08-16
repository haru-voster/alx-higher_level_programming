-- list all records with score >=10 in the second_table of the database hbtn_0n_0
-- in mysql server
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;

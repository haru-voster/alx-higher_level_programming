-- list all records of the table second_table of the database hbtn_0n_0
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC

SELECT score, COUNT(DISTINCT id) AS number
FROM hbtn_0c_0.second_table
GROUP BY score
ORDER BY number DESC;

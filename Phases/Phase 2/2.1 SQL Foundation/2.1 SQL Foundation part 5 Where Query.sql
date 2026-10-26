use startersql;
-- SELECT * FROM users WHERE gender = 'Male';
-- select name,gender from users Where gender<>'Female';
-- SELECT * FROM users WHERE date_of_birth < '1995-01-01';
-- SELECT * FROM users WHERE id <= 10;
-- SELECT * FROM users WHERE date_of_birth IS NULL;
-- SELECT * FROM users WHERE date_of_birth IS NOT NULL;

-- SELECT * FROM users WHERE date_of_birth BETWEEN '1995-01-01' AND '2000-12-31';
-- SELECT * FROM users WHERE gender IN ('Male', 'Other');


-- SELECT * FROM users WHERE name LIKE 'A%'; 
-- SELECT * FROM users WHERE name LIKE '%a'; 
-- SELECT * FROM users WHERE name LIKE '%na%';

-- SELECT * FROM users WHERE gender = 'Female' AND date_of_birth > '1990-01-01';
-- SELECT * FROM users WHERE gender = 'Male' OR gender = 'Other' ORDER BY date_of_birth ASC;
SELECT * FROM users WHERE gender = 'Male' OR gender = 'Other' ORDER BY date_of_birth DESC LIMIT 5;

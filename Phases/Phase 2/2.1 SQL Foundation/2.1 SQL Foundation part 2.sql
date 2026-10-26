-- ALTER TABLE users ADD COLUMN is_active BOOLEAN DEFAULT TRUE;
-- ALTER TABLE users DROP COLUMN is_active;
-- ALTER TABLE users MODIFY COLUMN name VARCHAR(150);
-- ALTER TABLE users MODIFY COLUMN email VARCHAR(100) FIRST;
-- ALTER TABLE users modify COLUMN email varchar(100) after id;
-- INSERT INTO users (name, email, gender, date_of_birth) VALUES
-- ('Charlie', 'charlie@example.com', 'Other', '1988-02-17'),
-- ('David', 'david@example.com', 'Male', '2000-08-09'),
-- ('Eva', 'eva@example.com', 'Female', '1993-12-30');
-- select * from users

SELECT * FROM users WHERE gender = 'Male';
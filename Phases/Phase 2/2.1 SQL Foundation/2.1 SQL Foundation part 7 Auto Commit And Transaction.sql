use startersql;
set autocommit = 0;
select * from users;
-- Delete from users where id = 6; -- if deleted unexpected data then roll back to go where you last commit
-- rollback;
-- Delete from users where id = 5;
commit; 
select * from users;
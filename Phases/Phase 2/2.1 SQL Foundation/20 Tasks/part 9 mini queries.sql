-- Aisi query likho jo:
-- sirf name aur salary return kare
-- salary 70000 ya greater ho
-- salary ko descending order mein sort kare
-- sirf top 5 employees return kare.

select name,salary 
from employee
where salary > 70000
order by salary desc
limit 5;
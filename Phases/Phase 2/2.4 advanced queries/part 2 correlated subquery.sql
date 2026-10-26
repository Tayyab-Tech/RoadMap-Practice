-- 3. Correlated Subquery
-- A correlated subquery depends on the current row of the outer query.

SELECT e.employee_name, e.salary, e.department_id
FROM employees as e
WHERE e.salary > (
    SELECT AVG(e2.salary)
    FROM employees as e2
    WHERE e2.department_id = e.department_id
);



SELECT datname FROM pg_database;

SELECT *
FROM pg_catalog.pg_tables 
WHERE schemaname = 'public';

INSERT INTO employee(emp_id, emp_name, dept_name,salary) 
VALUES(125, 'Amit','IT',11000);

-- Highest Salary and smallest emp_id if salary same
with foo as (
    select * from employee where salary = (
        select max(salary) from employee
    )  
)
select * from foo f1
join foo f2 on (f1.emp_id > f2.emp_id) ;


-- Highest Salary and smallest emp_id if salary same
select * from employee where salary = (
    select DISTINCT salary from employee 
    order by salary DESC limit 1 offset 2 
) order by emp_id desc LIMIT 1;


select salary , count(*) from employee 
GROUP BY salary
order by salary DESC limit 5 offset 0; 


-- Second Highest Salary
select * from employee where salary = (
    select max(salary) from employee
    GROUP BY salary 
    ORDER BY 1 desc 
    limit 1 offset 1 
);

-- Find the number of duplicate rows
SELECT salary, count(*) from employee 
GROUP BY salary 
HAVING COUNT(*) > 1
ORDER BY COUNT(*) DESC


-- Remove duplicate rows from a table
-- using window functions
with foo as (
    select * from employee where salary in (
        SELECT salary from employee 
        GROUP BY salary 
        HAVING COUNT(*) > 1
        ORDER BY COUNT(*) DESC
    ) ORDER by salary desc
),
bar as (
    select foo.*, 
    ROW_number() over(PARTITION by salary ORDER BY emp_id desc) 
    from foo ORDER BY salary desc, emp_id desc
)
SELECT emp_id from bar WHERE ROW_number <> 1

-- Remove duplicate rows from a table
select a.salary, a.emp_id, b.emp_id, a.emp_name from employee a
join employee b on (a.salary = b.salary)
where a.emp_id < b.emp_id




-- Users table duplicate username
select user_name, count(*) from users
group by user_name 
HAVING COUNT(*) > 1


select * from (
    SELECT *, 
    ROW_NUMBER() OVER(PARTITION BY user_name) 
    from users
) as foo where row_number > 1


with foo as (
    SELECT *, 
    ROW_NUMBER() OVER(PARTITION BY user_name) 
    from users
) select * from foo where row_number > 1

-- second last record from employee table
select * from employee 
order by emp_id desc limit 1 OFFSET 1

-- Write a SQL query to display only the details of employees who either earn the 
-- highest salary or the lowest salary in each department from the employee table.
with foo as (
    select dept_name, max(salary), min(salary)
    from employee
    group by dept_name
) 
select * from employee join foo USING (dept_name)
WHERE salary in (foo.max, foo.min) 
ORDER BY dept_name, emp_name

-- From the doctors table, fetch the details of doctors who work in the same 
-- hospital but in different specialty
select * from doctors d1
where EXISTS (
    select 1 from doctors 
    where hospital = d1.hospital and speciality <> d1.speciality
) 

select * from doctors d1 
join doctors d2 on (d1.hospital = d2.hospital and d1.speciality <> d2.speciality)

select d1.* from doctors d1  join doctors d2 using(hospital)
where d1.speciality <> d2.speciality

-- From the doctors table, fetch the details of doctors who work in the same hospital 
select distinct on (name) d1.* from doctors d1 
join doctors d2 on (d1.hospital = d2.hospital and d1.id <> d2.id)

select * from doctors d1 
where EXISTS (
    select 1 from doctors 
    where hospital = d1.hospital and id <> d1.id
)

-- 5. From the login_details table, fetch the users who logged in 
--     consecutively 3 or more times.
select distinct user_name from (
    select *, 
    case 
    when user_name = lead(user_name) OVER(order by login_id) 
    and user_name = lead(user_name, 2) OVER(order by login_id)
    then user_name else null
    end repeated
    from login_details
) as foo
where foo.repeated is not null;


-- 6. From the students table, write a SQL query to interchange 
-- the adjacent student names.
SELECT *, 
case 
when id%2 = 0 then lag(student_name, 1) over(ORDER by id)
when id%2 <> 0 then lead(student_name, 1, student_name) over(ORDER by id)
end as new_student_name 
from students













-- Find the fourth-highest score in the Students table using self-join


-- Show the max and min salary together from the Employees table


-- Calculate the number of rows in a table without using count

-- Find repeated characters from your name

-- Display department and month-wise maximum salary

-- Get the 3 Highest salaries records from the Student table

-- Show Odd rows in the Student table

-- Show Even rows in the Student table

-- Find all Employees with their managers.

-- Show 1 to 100 Numbers 

-- Get the previous month’s last day.

-- Display a string vertically.

-- The marks column in the Student table contains comma-separated values. How would you calculate the number of those comma-separated values?

-- Get the 3rd highest salary using Rank Function.

-- Display first 25% records from the Student table

-- Display last 25% records from the Student table

-- Get unique records from the table without using distinct keywords.












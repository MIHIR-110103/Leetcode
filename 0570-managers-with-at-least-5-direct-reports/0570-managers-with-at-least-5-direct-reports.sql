# Write your MySQL query statement below
select 
    name 
from 
    employee 
where 
    id 
in 
    (select 
        managerId 
    from 
        (select 
            id, managerId, name, COUNT(id) as direct_report 
        from 
            Employee 
        group by 
            managerId ) as New 
    where 
        New.direct_report >= 5)
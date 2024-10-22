# Write your MySQL query statement below
with result as (
    select id,movie,description,rating
    from Cinema
    where id % 2 != 0 and description != 'boring'
)
select id,movie,description,rating
from result
order by rating desc
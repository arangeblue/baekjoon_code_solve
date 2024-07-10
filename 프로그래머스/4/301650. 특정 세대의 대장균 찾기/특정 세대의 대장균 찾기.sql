-- 코드를 작성해주세요
with first_g as (
    select * 
    from ecoli_data
    where parent_id is null),
second_g as (
    select e.id, e.parent_id
    from ecoli_data as e
    join first_g as f on e.parent_id = f.id
)

# select *
# from second_g

select e.id 
from ecoli_data as e
join second_g as s on e.parent_id = s.id

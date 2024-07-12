-- 코드를 작성해주세요

select id, fish_name, length
from fish_info as fi
join fish_name_info as fn
    on fi.fish_type = fn.fish_type 
where (fi.fish_type, fi.length) in (
    select distinct fish_type,
        max(length) over(partition by fish_type)
    from fish_info 
)

order by id asc;
-- 코드를 작성해주세요

select emp_no, emp_name, GRADE,  
    case
        when GRADE = 'S' then SAL * 0.2
        when GRADE = 'A' then SAL * 0.15
        when GRADE = 'B' then SAL * 0.1
        else 0
    end as BONUS
from (
    select 
        he.emp_no, 
        he.emp_name, 
        case 
            when avg(score) >= 96 then 'S'
            when avg(score) >=90 and avg(score) < 96 then 'A'
            when avg(score) >=80 and avg(score) < 90  then "B"
            else "C"
        end as GRADE,
        he.SAL
    
    from hr_employees as he
    join hr_grade as hg on he.emp_no = hg.emp_no
    group by he.emp_no
) as a
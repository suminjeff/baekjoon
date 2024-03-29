-- 코드를 작성해주세요

# developers 테이블에서 frontend 스킬을 가진 개발자의 정보 조회
# id, email, first_name, last_name 조회
# 결과는 id 기준으로 오름차순 정렬

select d.id, d.email, d.first_name, d.last_name
from developers as d
where d.skill_code & (
    select sum(s.code)
    from skillcodes as s
    where category = 'Front End'
    group by category
)

order by id asc
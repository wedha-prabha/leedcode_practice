select 
e1.name as EMployee
from employee e1
join employee e2
on e1.managerid=e2.id
where e1.salary>e2.salary;
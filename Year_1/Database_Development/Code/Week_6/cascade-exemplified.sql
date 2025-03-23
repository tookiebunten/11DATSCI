.system echo "inside cascade-exemplified.sql"


-- There is no department with a department_id == 30;
-- DELETE FROM department WHERE department_id = 30;

DELETE FROM department WHERE department_id = 9;

.system echo ""
.system echo "department"
SELECT * FROM department;

.system echo ""
.system echo "employee"
SELECT * FROM employee;

.system echo ""
.system echo "manager"
SELECT * FROM manager;
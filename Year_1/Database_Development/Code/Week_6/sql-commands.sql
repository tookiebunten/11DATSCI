.system echo "********************************"
.system echo "in sql-commands.sql"  
.system echo "Some  SQL Commands"
.system echo "------------------------------"


.system echo "1 All data from Department table:"
.system echo "------------------------------"
SELECT * FROM Department;

.system echo "2 All data from Employee table:"
.system echo "------------------------------"
SELECT * FROM Employee;

.system echo "3 All data from Manager table:"
.system echo "------------------------------"
SELECT * FROM Manager;

.system echo "4 Which employees have a manager?"
.system echo "------------------------------"
SELECT name, sname FROM Employee 
	WHERE departmentId IN (SELECT departmentId FROM Manager);

.system echo "5 Which employees have a manager and who is it?"
.system echo "------------------------------"
SELECT Employee.name, Employee.sname, Manager.name, Manager.sname 
FROM Employee         
INNER JOIN Manager        
ON Employee.departmentId = Manager.departmentId;

.system echo "6 Joining employees with departments"
.system echo "------------------------------"
SELECT Employee.name, Employee.sname, Department.name 
FROM Employee         
INNER JOIN Department        
ON Employee.departmentId = Department.departmentId;


.system echo "7 Storing a view of the join query then displaying it..."
.system echo "------------------------------"
DROP VIEW IF EXISTS EmployeeDepartments;
CREATE VIEW EmployeeDepartments AS
SELECT Employee.name, Employee.sname, Department.name 
FROM Employee         
INNER JOIN Department        
ON Employee.departmentId = Department.departmentId;

SELECT * FROM EmployeeDepartments;

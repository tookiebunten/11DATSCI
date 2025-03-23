--.system cls -- windows
.system clear
.system echo "inside top-level.sql"
--
PRAGMA foreign_keys = ON;
.read create-department.sql
.read create-employee.sql


--/*
.system echo ""
.system echo "Expects no failure in this order"
.system echo "--------------------------------"
.read load-department.sql
.read load-employee.sql
--*/


/*
.system echo ""
.system echo "Expects failure in this order because employee references department"
.system echo "--------------------------------------------------------------------"
.read load-employee.sql
.read load-department.sql
*/

--.read sql-commands.sql

--/*
.system echo ""
.system echo "department"
SELECT * FROM department;

.system echo ""
.system echo "employee"
SELECT * FROM employee;

.system echo ""
.system echo "manager"
SELECT * FROM manager;

.read cascade-exemplified.sql
--/*

--.read sql-commands.sql

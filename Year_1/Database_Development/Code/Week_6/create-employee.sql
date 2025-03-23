.system echo "inside create-employee.sql"

DROP TABLE IF EXISTS Employee;

CREATE TABLE IF NOT EXISTS Employee (
    employeeId INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    sname TEXT NOT NULL,
	department_id INTEGER,
	FOREIGN KEY(department_id) REFERENCES department(department_id)
		ON DELETE CASCADE
);


DROP TABLE IF EXISTS Manager;

CREATE TABLE IF NOT EXISTS Manager (
    managerId INTEGER PRIMARY KEY,
	name TEXT NOT NULL,
    sname TEXT NOT NULL,
	department_id INTEGER NOT NULL
	-- How would you ensure that a manager 'links' to an existing depertment 
);



.system echo "inside create-department.sql"

DROP TABLE IF EXISTS department;

-- see '3' here:
-- https://sqlite.org/autoinc.html 
-- 
CREATE TABLE IF NOT EXISTS department (
	--AUTOINCREMENT ? does this anyways! see department table output
	-- 
    department_id INTEGER PRIMARY KEY, 
    name TEXT NOT NULL,
    managerID INTEGER DEFAULT 0,
	locationId TEXT
);
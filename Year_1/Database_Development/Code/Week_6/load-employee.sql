.system echo "inside load-employee.sql"

-- must include departmentId when inserting values (see table schame)
INSERT INTO Employee(name, sname, department_id)
	VALUES 
		("Neena", "Kochhar", 9),
		("Lex", "De Hass", 9),
		("Alexandra", "Hunold", 6),
		("Bruce", "Ernst", 6),
		("David", "Austin", 6),
		("Valli", "Patabala", 6),
		("Dana", "Lorentz", 6),
		("Nancy", "Greenberg", 10),
		("Daniel", "Faviet", 10);
		
INSERT INTO Employee(name, sname)
	VALUES 
		("Jim", "Smith");
		
INSERT INTO Manager(name, sname, department_id) VALUES ("Steven", "King", 9);
		
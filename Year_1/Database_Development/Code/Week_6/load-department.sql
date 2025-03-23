.system echo "inside load-department.sql"

INSERT INTO department(name, locationID)
	VALUES 
		("Administration", 1700),
		("Marketing", 1800),
		("Purchasing", 1700),
		("Human Resources", 2400),		
		("Shipping", 1500),
		("IT", 1400),
		("Public Relations", 2700),
		("Sales", 2500),
		("Executive", 1700),
		("Finance", 1700);

.system echo ""
.system echo "EXPECT ERROR:"		
INSERT INTO department(department_id, name, locationId)
	VALUES 
		(5, "test-name", -2);.system
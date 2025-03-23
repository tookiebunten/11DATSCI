-- Create the CustomerOrder table
DROP TABLE IF EXISTS CustomerOrder;
CREATE TABLE CustomerOrder (
order_no TEXT, 
date TEXT, 
customer TEXT, 
source TEXT
);

-- Insert the data
INSERT INTO CustomerOrder (order_no, date, customer, source )
VALUES 
("00158","10-DEC-98","NW002","EMAIL"),
("00159","11-DEC-98","SE001","PHONE"),
("00160","11-DEC-98","NE001","MAIL"),
("00161","14-DEC-98","NW002","EMAIL"),
("00162","16-DEC-98","NW001","PHONE");

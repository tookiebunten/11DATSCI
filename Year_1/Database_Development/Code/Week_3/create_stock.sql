-- Create the Stock table
DROP TABLE IF EXISTS Stock;
CREATE TABLE Stock (
stock_no TEXT,
description TEXT,
storage TEXT,
reorder_level TEXT DEFAULT 0,
reorder_quantity TEXT DEFAULT 0,
price TEXT
);

/*  */

-- Insert the data
INSERT INTO Stock (stock_no, description, storage, reorder_level, reorder_quantity, price )
VALUES
("TS001", "AUGUST COVER T-SHIRT", "55", 30,	30,	12.99),
("TS002", "BAND SHOT T-SHIRT", "50", 30,	50,	12.99),
("TS003", "ADAM (AUGUST) T-SHIRT", "28",	30,	30,	12.99),
("TS004", "SATELLITES COVER T-SHIRT", "55",	30,	25,	12.99),
("SS001", "AUGUST COVER SWEATSHIRT", "55",	20,	50,	25.99),
("SS002", "SATELLITES COVER SWEATSHIRT", "55",	20,	50,	25.99),
("CD001", "AUGUST & EVERYTHING AFTER", "125",	100,	100,	11.99),
("CD002", "RECOVERING THE SATELLITES", "155",	50,	50,	11.99),
("CD003", "ACROSS A WIRE", "300",	150,	200,	14.99),
("VD001", "CROWS VIDEO COLLECTION", "229",	100,	50,	9.99),
("LJ001", "CROWS LEATHER JACKET", "52",	10,	20,	125),
("LP001", "AUGUST LP", "10", 5,	10,	18.99),
("LP002", "SATELLITES LP", "12", 10, 10, 18.99),
("LP003", "ACROSS A WIRE LP", "52",	10,	20,	21.99),
("MD001", "AUGUST MD", "5",	5, 10, 16.99),
("MD002", "SATELLITES MD", "10", 7, 10,	16.99),
("MD003", "ACROSS A WIRE MD", "60",	10,	20,	18.99);

INSERT INTO Stock (stock_no, description, storage, price )
VALUES
("CS001", "AUGUST CASSETTE", "15", 8.99),
("CS002", "SATELLITES CASSETTE", "43", 8.99);
.system echo "Inside script <create-books.sql>"

DROP TABLE IF EXISTS books; -- Get rid of existing table

-- Create the table a-new !
CREATE TABLE books(
	title TEXT, -- title of the book
	author TEXT, 
	genre TEXT,
	subgenre TEXT,
	height INTEGER, -- height of the book
	publisher TEXT
);
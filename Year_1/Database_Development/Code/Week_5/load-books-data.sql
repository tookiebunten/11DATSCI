.system echo "Inside script <load-books-data.sql>"

.mode csv
.import books.csv books
.mode list


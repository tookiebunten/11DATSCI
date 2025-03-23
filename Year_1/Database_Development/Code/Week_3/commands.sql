-- commands.sql
-- Display the intent of a subsequent sql 
-- command to screen b4 running it and thus
-- displaying the output.
--
-- temporarily turn echo off to neated to output to stdout
.echo off 
-- ensure output goes to terminal screen
.output stdout 

.print "............................"
.print "List the customer no., name & email for each customer."
SELECT customer_no, name, email FROM customer;

.print "............................"
.print "List the customer of each customer order."
SELECT customer FROM CustomerOrder;

.print "............................"
.print "List the stock no., description & price for each stock item."
SELECT stock_no, description, price FROM stock;

.print "............................"
.print "List the customer nos and email of each customer who has placed an order."
SELECT customer_no, email FROM Customer WHERE customer_no IN (SELECT customer FROM CustomerOrder);

.echo on -- turn echo on again
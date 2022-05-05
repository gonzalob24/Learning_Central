-- concat may be different in other DBMS. + or ||
-- RTRIM() to trim white spaces
SELECT CONCAT(vend_name, ' ', '(', vend_country, ')') AS vend_title 
FROM Vendors
ORDER BY vend_name;

-- performing mathematical calculations
SELECT prod_id, quantity, item_price FROM OrderItems
WHERE order_num = 20008;

-- combine items if they are the same type
SELECT prod_id, quantity, item_price, quantity*item_price AS expanded_price
FROM OrderItems
WHERE order_num = 20008;

-- Challenge questions
-- 1. get vend_id, vend_name, vend_address and vend_city from vendors renaming vend_name to vname, vend_city to vcity and vend_address to vaddress.
SELECT vend_id AS vid, 
       vend_name AS vname,
       vend_city AS vcity,
       vend_address AS vaddress 
FROM Vendors
ORDER BY vname;

-- 2. All sales are 10% off. Write sql to get prod_id, prod_price and sales_price
-- from Products. sale_price is a calculated field that contains sales price. 
SELECT prod_id, prod_price, prod_price * .90 AS sales_price 
FROM Products;
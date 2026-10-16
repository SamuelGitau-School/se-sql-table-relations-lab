# STEP 0

# SQL Library and Pandas Library
import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect('data.sqlite')

pd.read_sql("""SELECT * FROM sqlite_master""", conn)

# STEP 1
# Replace None with your code
df_boston = pd.read_sql("""
    SELECT e.firstName, e.lastName, e.jobTitle
    FROM employess e    
    JOIN offices o USING (officeCode)
    WHERE o.city = 'Boston'
    """,conn)

# STEP 2
# Replace None with your code
df_zero_emp = pd.read_sql("""
    SELECT o.officeCode, o.city
    FROM offices o
    LEFT JOIN employees e USING (officeCode)
    GROUP BY o.fficeCode, o.city
    HAVING COUNT (e.employeeNumber) = 0
    """,conn)

# STEP 3
# Replace None with your code
df_employee = pd.read_sql("""
    SELECT e.firstName, e.lastName, o.city, o.state
    FROM employees e
    LEFT JOIN offices o USING (officeCode)
    ORDER BY e.firstName, e.lastName
    """,conn)

# STEP 4
# Replace None with your code
df_contacts = pd.read_sql("""
    SELECT c.contactFirstName, c.contactLastName, c.phone, c.salesRepEmployeeNumber 
    FROM customers from c 
    LEFT JOIN orders o USING (orderNumber)
    WHERE o.orderNumber is NULL
    ORDER BY c.contactLastName
    """,conn)

# STEP 5
# Replace None with your code
df_payment = pd.read_sql("""
    SELECT c.contactFirstName, c.contactLastName, p.paymentDate, p.amount
    FROM customers c 
    LEFT JOIN payments p USING (customerNumber)
    ORDER BY CAST(p.amount AS REAL) DESC
    """,conn)

# STEP 6
# Replace None with your code
df_credit = pd.read_sql("""
    SELECT e.employeeNumber, e.lastNumber, e.firstName, 
        COUNT(c.customerNumber) AS n_customer
    FROM employees e
    JOIN customers c on c.salesRepEmployeeNumber = e.employeeNumber
    GROUP BY e.employeeNumber, e.lastNumber, e.firstName
    HAVING AVG (c.creditLimit) > 90000
    ORDER BY n_customer DESC
    """,conn)

# STEP 7
# Replace None with your code
df_product_sold = pd.read_sql("""
    SELECT p.productName, 
        COUNT (od.orderNumber) AS numorders,
        SUM (od.quantityOrdered) AS totalunits
    FROM products p
    JOIN orderdetails od USING (productCode)
    GROUP BY p.productCode, p.productName
    ORDER BY totalunits DESC        
    """,conn)

# STEP 8
# Replace None with your code
df_total_customers = pd.read_sql("""
    SELECT p.productCode, p.productName, 
        COUNT(DISTINCT o.customerNumber) AS numpurchasers
    FROM products p 
    JOIN orderdetails od USING (productCode)
    JOIN orders o USING (orderNumber)
    GROUP BY p.productCode, p.productName
    ORDER numpurchasers DESC
    """,conn)

# STEP 9
# Replace None with your code
df_customers = pd.read_sql("""
    SELECT off.officeCode, off.city
        COUNT(c.customerNumber) AS n_customers
    FROM offices off
    JOIN employess e USING (officeCode)  
    JOIN customers c ON c.salesRepEmployeeNumber = e.employeeNumber      
    GROUP BY off.officeCode, off.city
    """,conn)

# STEP 10
# Replace None with your code
df_under_20 = pd.read_sql("""
    SELECT e.employeeNumber, e.firstName, e.lastName, off.city, off.officeCode
    FROM employees e 
    JOIN offices off USING (officeCode)
    JOIN customers c ON c.salesRepEmployeeNumber = e.employeeNumber
    JOIN orders o USING (customerNumber)
    JOIN orderdetails od (orderNumber)
    WHERE od IN od.productCode(
        SELECT od2.productCode
        FROM orderdetails od2 
        JOIN orders o2 USING (orderNumber)
        GROUP BY od2.productCode
        HAVING COUNT(DISTINCT o2.customerNumber) < 20        
    )    
    """,conn)

conn.close()
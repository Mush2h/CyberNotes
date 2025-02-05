
# OWASP TOP 10

## SQLI

- SQL Injection (SQLI) is an attack technique used to exploit vulnerabilities in web applications that do not properly validate user input in SQL queries sent to the database. Attackers can use this technique to execute malicious SQL queries and obtain sensitive information, such as usernames, passwords, and other data stored in the database.

- Types of SQL Injection:
    - Error-based: Exploits SQL code errors to gather information.
    - Time-based: Uses time-delayed queries to extract data.
    - Boolean-based: Employs boolean expressions to obtain additional information.
    - Union-based: Combines two or more queries using the "UNION" clause.
    - Stacked queries: Executes multiple queries in a single statement.

### Examples of SQL Injection exploitation:

#### Authentication bypass:
```sql
SELECT * FROM users WHERE username = 'admin' AND password = '' OR '1'='1'
```

This query always returns true, potentially granting unauthorized access.

#### Data extraction:
```sql
SELECT * FROM users WHERE id = 1 UNION SELECT username, password FROM admin_users
```
This query combines results from two tables, potentially exposing admin credentials.

#### Time-based blind injection:
```sql
SELECT * FROM users WHERE id = 1 AND IF(SUBSTRING(username,1,1) = 'a', SLEEP(5), 0)
```
If the first character of the username is 'a', the query will delay for 5 seconds, allowing data extraction through timing analysis.

#### Inserting malicious data:
```sql
INSERT INTO users (username, email) VALUES ('hacker', 'malicious@email.com'); DROP TABLE users;--')
```
This query inserts a new user and then drops the entire users table.
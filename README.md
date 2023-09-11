## db to json convertion

This Python code connects to an SQLite database, retrieves all data from a table named "data," converts it to a well-formatted JSON string, writes it to a "data.json" file, and closes the database connection.

### full code explanation
This snippet demonstrates how to retrieve data from a SQLite database and write it into a JSON file.

Here's a step-by-step explanation of what each part of the code does:

Importing Libraries:

```
import sqlite3, json
```

This line imports two Python libraries:
- `sqlite3`: This library provides functionality to work with SQLite databases.
- `json`: This library allows you to encode Python data structures as JSON (JavaScript Object Notation) strings.

Database Connection:
```
connection = sqlite3.connect("data.db")
```
This line establishes a connection to an SQLite database file named "data.db". If the file doesn't exist, it will be created. If it already exists, a connection to it is established.

Creating a Cursor:
```
cursor = connection.cursor()
```
This line creates a cursor object. A cursor is used to interact with the database and execute SQL queries.

Executing a SQL Query:
```
cursor.execute("select * from data")
```
This line executes an SQL query that selects all rows from a table named "data". The results of this query will be stored in the data variable.

Fetching Data:
```
data = cursor.fetchall()
```
This line fetches all the rows returned by the SQL query and stores them in the data variable. fetchall() retrieves all rows as a list of tuples.

Writing Data to a JSON File:
```
open('data.json', 'w', encoding='utf-8-sig').write(json.dumps(data, indent=4))
```

This line does the following:
- It opens a file named "data.json" in write mode ('w').
- The 'utf-8-sig' encoding is used to ensure that the JSON file includes a UTF-8 byte order mark (BOM) to indicate that the text is encoded in UTF-8.
- json.dumps(data, indent=4) converts the Python data (which is a list of tuples) into a JSON-formatted string with an indentation of 4 spaces for readability.
- The `.write()` method writes the JSON string to the "data.json" file.

Closing the Database Connection:
```
connection.close()
```
This line closes the SQLite database connection to free up system resources.

In summary, this code connects to an SQLite database, retrieves all the data from a table named "data," converts it into a nicely formatted JSON string, and writes it to a file named "data.json".

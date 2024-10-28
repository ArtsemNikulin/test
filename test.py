import pymssql

with pymssql.connect(server='EPPLWARW009D\\SQLEXPRESS',
                     database='AdventureWorks2022',
                     user='test',
                     password='Qazxcvfr1234',
                     as_dict=True) as conn:
    print("Connection established successfully.")

    cursor = conn.cursor()
    cursor.execute('SELECT 1 AS test_column')
    result = cursor.fetchone()
    print("Query executed successfully:", result)
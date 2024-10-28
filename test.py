import pymssql
print('Hello arch')


conn = pymssql.connect(
    server='EPPLWARW009D\\SQLEXPRESS',
    user='test',
    password='Qazxcvfr1234',
    database='AdventureWorks2022',
    as_dict=True
)
cursor = conn.cursor()
cursor.execute('SELECT TOP 10 * FROM person.person')
records = cursor.fetchall()
print(records)
conn.close()

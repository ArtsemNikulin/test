# import pymssql
# print('Hello arch')


# conn = pymssql.connect(
#     server='192.168.0.53',
#     user='test',
#     password='Qazxcvfr1234',
#     database='AdventureWorks2022',
#     as_dict=True
# )
# cursor = conn.cursor()
# cursor.execute('SELECT TOP 10 * FROM person.person')
# records = cursor.fetchall()
# print(records)
# conn.close()
import pyodbc

with pyodbc.connect(r'DRIVER={SQL Server};Server=host.docker.internal;Database=AdventureWorks2022;UID=test;PWD=Qazxcvfr1234',
                    autocommit=True) as conn:
    cursor = conn.cursor()
    x = list(cursor.execute('SELECT TOP 10 * FROM person.person'))
    print(x)

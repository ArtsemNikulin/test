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

with pyodbc.connect(f'DRIVER={{ODBC Driver 17 for SQL Server}};Server=192.168.0.53;Database=TRN;UID=test;PWD=Qazxcvfr1234',
                    autocommit=True) as conn:
    cursor = conn.cursor()
    x = list(cursor.execute('SELECT 1'))
    print(x)

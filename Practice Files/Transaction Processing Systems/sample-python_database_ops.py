import pyodbc 

conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      'Server=tcp:function.database.windows.net,1433;'
                      'Database=demo;'
                      'Uid=testuser;'
                      'Pwd=P@55word')


cursor = conn.cursor()
cursor.execute('SELECT * FROM tableName')

for i in cursor:
    print(i)

cursor.close()
conn.close()
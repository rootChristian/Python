import pyodbc

cnxn = pyodbc.connect('Driver={SQL Server};Server=Server_Name;Database=Database_Name;')
cursor = cnxn.cursor()
cursor.execute("SELECT * FROM dbo.DIPENDENTE")
while 1:
    row = cursor.fetchone()
 
    if not row:
        break
 
    print(row)


'pyodbc.connect("Driver = {SQL Server Native Client 11.0};"               
               "Server = Server_Name;"
               "Database = Database_Name;"
               "username = User_Name;"
               "password = User_Password;"
               "Trusted_Connection = yes;")

'''

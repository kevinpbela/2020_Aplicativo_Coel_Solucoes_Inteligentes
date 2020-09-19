# from model.login import Login
import pyodbc

# base_de_dados = [
#     Login(id=1, nome="teste", senha="teste"),
#     Login(id=2, nome="teste2", senha="123")
# ]


server = "coel.database.windows.net"
database = "Aplicativo"
username = "Adriano"
password = "Coelmatic01"
driver= '{ODBC Driver 17 for SQL Server}'

conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

with pyodbc.connect('DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM [login]")
        row = cursor.fetchone()
        while row:
            print (str(row[0]) + " " + str(row[1]))
            row = cursor.fetchone()
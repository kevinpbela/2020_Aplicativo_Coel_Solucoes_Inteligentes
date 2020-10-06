"""
    Só utilizar se for criar o Banco por aqui
"""

# import sqlite3

# db_name = "Aplicativo.db"
# table_name = "usuario"

# sql_create_table = f"CREATE TABLE IF NOT EXISTS {table_name} (id integer PRIMARY KEY, nome text NOT NULL, senha text NOT NULL);"


# def createTable(cursor, sql):
#     cursor.execute(sql)


# def popularDb(cursor, id, email, login, nome, senha):
#     sql = f"INSERT INTO {table_name} (id, email, login, nome, senha) VALUES (?, ?, ?, ?, ?)"
#     cursor.execute(sql, (id, email, login, nome, senha))


# def init():
#     connection = sqlite3.connect(db_name)
#     cursor = connection.cursor()
#     createTable(cursor, sql_create_table)
#     try:
#         popularDb(cursor, 1, "alexandre@coel.com", "ale", "alexandre", "123")
#     except:
#         pass
#     cursor.close()
#     connection.commit()
#     connection.close()


# init()

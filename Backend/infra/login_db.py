import sqlite3

db_name = "login.db"
table_name = "login"

sql_create_table = f"CREATE TABLE IF NOT EXISTS {table_name} (id integer PRIMARY KEY, nome text NOT NULL, senha text NOT NULL);"


def createTable(cursor, sql):
    cursor.execute(sql)


def popularDb(cursor, id, nome, senha):
    sql = f"INSERT INTO {table_name} (id, nome, senha) VALUES (?, ?, ?)"
    cursor.execute(sql, (id, nome, senha))


def init():
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    createTable(cursor, sql_create_table)
    try:
        popularDb(cursor, 1, "alexandre", "123")
        popularDb(cursor, 2, "ale", "123")
        popularDb(cursor, 3, "teste", "123")
    except:
        pass
    cursor.close()
    connection.commit()
    connection.close()


init()

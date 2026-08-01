import sqlite3

def conn():
    return sqlite3.connect('data/clients.db')

def create_tables():
    connect = conn()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXIST clients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            cpf TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
    )
''')

connect.commit()
connect.close()
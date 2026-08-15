from database import conn
import bcrypt

def create_user(name,email,cpf,password):
    connect = conn()
    cursor = connect.cursor()

    # transform the typed password in bytes
    bytes_password = password.encode('utf-8')

    #generate the "salt" and do the hash of the password
    salt = bcrypt.gensalt()
    hash_password = bcrypt.hashpw(bytes_password, salt)
    saved_password = hash_password.decode('utf-8')

    cursor.execute('''
        INSERT INTO clients (name, email, cpf, password)
        VALUES (?, ?, ?, ?)
        ''',
        (name,email,cpf,saved_password)
    )

    connect.commit()
    connect.close()

def read_users():
    connect = conn()
    cursor = connect.cursor()

    cursor.execute('SELECT id, name, email, cpf FROM clients')
    res = cursor.fetchall()
    connect.close()
    return res

def update_user(old_cpf, new_name, new_email, new_cpf):
    connect = conn()
    cursor = connect.cursor()

    cursor.execute('''
        UPDATE clients
        SET 
        name = ?,
        email = ?,
        cpf = ?
        WHERE cpf = ?
    ''', (new_name, new_email, new_cpf, old_cpf))

    connect.commit()
    connect.close()

def delete_user(cpf):
    connect = conn()
    cursor = connect.cursor()
    cursor.execute('DELETE FROM clients WHERE cpf = ?', (cpf,))
    connect.commit()
    connect.close()

def login(typed_email, typed_password):
    connect = conn()
    cursor = connect.cursor()
    cursor.execute('SELECT password FROM clients WHERE email = ?', (typed_email,))
    res = cursor.fetchone()
    connect.close()

    if res is None:
        return False

    password_hash = res[0].encode('utf-8')
    password_typed_bytes = typed_password.encode('utf-8')

    return bcrypt.checkpw(password_typed_bytes, password_hash)
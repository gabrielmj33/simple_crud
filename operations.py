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
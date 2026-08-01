from database import conn
import bcrypt

def create_user(name,email,cpf,password):
    connect =
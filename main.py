from database import create_tables
from operations import create_user, read_users, update_user, delete_user, login

def menu():
    print("\n--- NEW USER ---")
    name = input("Name: ").strip()
    if len(name) < 3:
        print("The name have to be at least 3 characters.")
        return

    email = input("Email: ").strip()
    if "@" not in email or "." not in email:
        print("Invalid  email format.")
        return

    cpf = input("CPF (only numbers): ").strip()
    if len(cpf) != 11 or not cpf.isdigit():
        print("The CPF has to have exactly 11 numbers.")
        return

    password = input("Password: ")
    if len(password) < 6:
        print("The password need have at least 6 characters.")
        return

    try:
        create_user(name, email, cpf, password)
        print("User successfully created!")
    except Exception as e:
        print(f"Error when save in the DATABASE (CPF or EMAIL already in use).")
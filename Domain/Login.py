import sqlite3
import hashlib

conn = sqlite3.connect('Navio.db')

def GetUserPassword(username):
    cursor = conn.cursor()
    cursor.execute(f"SELECT Password FROM User WHERE Username = '{username}';")
    for password in cursor.fetchall():
        if (len(password) != 0):
            return password
    
    raise Exception("Usuário não encontrado!")

def LoginUser(inputedUsername, inputedPassword):
    passwordOnDatabase = GetUserPassword(inputedUsername)
    inputedPasswordEncoded = hashlib.sha1(inputedPassword.encode()).hexdigest()

    if (passwordOnDatabase[0] == inputedPasswordEncoded):
        return True

    return False
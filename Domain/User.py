import sqlite3
import hashlib

conn = sqlite3.connect('Navio.db')

def InsertUser(username, password):
    encodedPassword = hashlib.sha1(password.encode()).hexdigest()

    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO User (Username, Password) VALUES ('{username}', '{encodedPassword}');")
    
    conn.commit()


def GetUsers():
    cursor = conn.cursor()
    cursor.execute("SELECT Id, Username FROM User")
    
    users = []
    for user in cursor.fetchall():
        users.append(str(user))
    return users

def UpdateUser(username, userId):
    cursor = conn.cursor()
    cursor.execute(f"UPDATE User SET Username = '{username}' WHERE Id = '{userId}';")
    
    conn.commit()

def DeleteUser(userId):
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM User WHERE Id = '{userId}';")
    
    conn.commit()
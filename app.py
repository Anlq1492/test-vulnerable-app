import os
import sqlite3

def vulnerable_function(user_input):
    # SQL инъекция (уязвимость)
    conn = sqlite3.connect('users.db')
    query = "SELECT * FROM users WHERE name = '" + user_input + "'"
    cursor = conn.execute(query)
    
    # Использование eval (опасно)
    eval(user_input)
    
    # Хардкод секрета (уязвимость)
    API_KEY = "1234567890abcdef"
    PASSWORD = "admin123"
    
    # Небезопасное использование os.system
    os.system("ping " + user_input)
    
    return cursor.fetchall()

if __name__ == "__main__":
    data = input("Enter data: ")
    vulnerable_function(data)

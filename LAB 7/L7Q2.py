#!/usr/bin/python
import sqlite3
import re

def main():
    conn = sqlite3.connect('registration.db')
    print("Opened database successfully")

    create_table(conn)

    choice = input("Enter choice: 1 for signup, 2 for login: ")

    if choice == '1':
        create_users(conn)
    elif choice == '2':
        login(conn)
    else:
        print("Invalid choice")

    conn.close()

def create_table(conn):
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY,
                        username TEXT UNIQUE,
                        email TEXT UNIQUE,
                        password TEXT
                    )''')
    conn.commit()
    cursor.close()

def create_users(conn):
    num_users = int(input("Enter number of users to create: "))
    for _ in range(num_users):
        while True:
            username = input("Enter username: ")
            email = input("Enter email: ")
            password = input("Enter password: ")

            if validate_username(username) and validate_email(email) and validate_password(password):
                insert_user(conn, username, email, password)
                print("User created successfully!")
                break
            else:
                print("Invalid input. Please try again.")

def login(conn):
    username = input("Enter username: ")
    password = input("Enter password: ")

    if validate_username(username) and validate_password(password):
        if check_user(conn, username, password):
            print("Login successful!")
        else:
            print("Invalid username or password")
    else:
        print("Invalid username or password")

def check_user(conn, username, password):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()
    cursor.close()
    return user is not None

def insert_user(conn, username, email, password):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (username, email, password))
    conn.commit()
    cursor.close()

def validate_username(username):
    return re.match(r'^[a-zA-Z0-9_]{3,20}$', username)

def validate_email(email):
    return re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)

def validate_password(password):
    return len(password) >= 8

if __name__ == "__main__":
    main()

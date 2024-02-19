#!/usr/bin/python
import sqlite3
import re

def main():
    conn = sqlite3.connect('registration.db')
    print("Opened database successfully")

    create_table(conn)


    create_users(conn)


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



def insert_user(conn, username, email, password):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (username, email, password))
    conn.commit()
    cursor.close()

if __name__ == "__main__":
    main()

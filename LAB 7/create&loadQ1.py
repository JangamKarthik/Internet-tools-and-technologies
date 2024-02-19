#!/usr/bin/python
import sqlite3

def main():
    conn = sqlite3.connect('test.db')
    print("Opened database successfully")

    create_table(conn)

    insert_records(conn)

    conn.close()
    print("Records inserted successfully")

def create_table(conn):
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS student (
                        Student_ID INTEGER PRIMARY KEY,
                        Reg_No TEXT,
                        Branch TEXT,
                        Semester INTEGER,
                        Section TEXT,
                        CGPA REAL,
                        email TEXT
                    )''')
    conn.commit()
    cursor.close()

def insert_records(conn):
    cursor = conn.cursor()
    for i in range(1, 11):
        cursor.execute("INSERT INTO student (Reg_No, Branch, Semester, Section, CGPA, email) \
                        VALUES (?, ?, ?, ?, ?, ?)",
                        ('REG00' + str(i), 'Branch' + str(i % 3 + 1), i % 8 + 1, 'Section' + str(i % 2 + 1), i % 4 + 7.5, 'student' + str(i) + '@example.com'))
    conn.commit()
    cursor.close()

if __name__ == "__main__":
    main()


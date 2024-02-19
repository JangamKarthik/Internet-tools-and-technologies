#!/usr/bin/python
import sqlite3

def main():
    conn = sqlite3.connect('test.db')
    print("Opened database successfully")

    display_sorted_records(conn)

    conn.close()

def display_sorted_records(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM student ORDER BY Student_ID")
    student_records = cursor.fetchall()

    print("Student ID\tReg No\tBranch\tSemester\tSection\tCGPA\temail")
    print("-------------------------------------------------------------")
    for record in student_records:
        print("\t".join(str(field) for field in record))
    cursor.close()

if __name__ == "__main__":
    main()

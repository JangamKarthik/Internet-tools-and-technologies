#!/usr/bin/python
import sqlite3

def main():
    conn = sqlite3.connect('test.db')
    print("Opened database successfully")

    student_id = int(input("Enter Student ID: "))
    new_cgpa = float(input("Enter new CGPA: "))

    update_cgpa_by_id(conn, student_id, new_cgpa)

    conn.close()

def update_cgpa_by_id(conn, student_id, new_cgpa):
    cursor = conn.cursor()
    cursor.execute("UPDATE student SET CGPA=? WHERE Student_ID=?", (new_cgpa, student_id))
    conn.commit()
    cursor.close()
    print("CGPA updated successfully for Student ID:", student_id)

if __name__ == "__main__":
    main()
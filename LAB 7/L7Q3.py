#!/usr/bin/python
import sqlite3

def main():
    conn = sqlite3.connect('test.db')
    print("Opened database successfully")

    regno = input("Enter registration number to search: ")

    student_details = search_student_by_regno(conn, regno)

    if student_details:
        print("Student details found:")
        print("Student ID:", student_details[0])
        print("Reg No:", student_details[1])
        print("Branch:", student_details[2])
        print("Semester:", student_details[3])
        print("Section:", student_details[4])
        print("CGPA:", student_details[5])
        print("Email:", student_details[6])
    else:
        print("Student not found with registration number:", regno)

    conn.close()

def search_student_by_regno(conn, regno):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM student WHERE Reg_No=?", (regno,))
    student_details = cursor.fetchone()
    cursor.close()
    return student_details

if __name__ == "__main__":
    main()

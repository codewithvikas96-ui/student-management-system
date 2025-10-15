import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "***",  # in the place of ** enter your mysql password
    database = "student_db"
)

cursor = conn.cursor()

def add_student(id,name,age,grade):
    query = "INSERT INTO Students (id,name,age,grade) VALUES (%s, %s, %s, %s)"
    values = (id,name,age,grade)
    cursor.execute(query,values)
    conn.commit()
    print("Student added Successfully")


def view_student():
    query = "SELECT * FROM Students"
    cursor.execute(query)
    records = cursor.fetchall()

    if not records:
        print("Nothing to view")
    else:
        print("\n------ Students records ------")
        print(f"{'Sr.no':<6} {'ID':<5} {'Name':<30} {'Age':<5} {'Grade':<5}")
        for idx,(id,name,age,grade) in enumerate(records,start=1):
            print(f"{idx:<6} {id:<5} {name:<30} {age:<5} {grade:<5}")

def search_student(sid):
    query = "SELECT * FROM Students WHERE id = %s"
    cursor.execute(query,(sid,))
    record = cursor.fetchone()

    if record:
        print(f"\nStudent Found ")
        print(f"{'Sr.no':<6} {'ID':<5} {'Name':<30} {'Age':<5} {'Grade':<5}")
        for idx,(id,name,age,grade) in enumerate(record,start=1):
            print(f"{idx:<6} {id:<5} {name:<30} {age:<5} {grade:<5}")
    else:
        print(f"\nStudent Not found with ID {sid}")

def update_student(sid,name,age,grade):
    query = "UPDATE Students SET name = %s, age = %s, grade = %s WHERE id = %s"
    values = (name,age,grade,sid)
    cursor.execute(query,values)
    conn.commit()
    print("Student Updated Successfully")

def delete_student(sid):
    query = "DELETE FROM Students WHERE id = %s"
    cursor.execute(query,(sid,))
    conn.commit()
    print("Student Deleted Successfully")

while True:
    print("\n====== Student Management System ======")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter choice(1-6): ")

    if choice == '1':
        id = int(input("Enter id: "))
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        grade = input("Enter grade: ")

        add_student(id,name,age,grade)

    elif choice == '2':
        view_student()

    elif choice == '3':
        sid = int(input("Enter student ID: "))
        search_student(sid)

    elif choice == '4':
        sid = int(input("Enter student id: "))
        name = input("Enter new name: ")
        age = int(input("Enter new age: "))
        grade = input("Enter new grade: ")

        update_student(sid,name,age,grade)

    elif choice == '5':
        sid = int(input("Enter student id: "))
        delete_student(sid)

    elif choice == '6':
        print("Exiting.....")
        break
    else:
        print("Invalid Choice! Try again")


cursor.close()
conn.close()




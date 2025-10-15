
# 🎓 Student Management System

A simple command-line based Student Management System built with Python and MySQL. This project allows users to add, view, search, update, and delete student records from a MySQL database.

---

## 🚀 Features

- Add new student records
- View all students
- Search student by ID
- Update student details
- Delete student records
- Persistent storage using MySQL

---

## 🛠️ Technologies Used

- Python 3.x
- MySQL
- mysql-connector-python

---

## 📦 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/codewithvikas96-ui/student-management-system.git
```
### 2. Navigate inside the project folder
```bash
cd student-management-system
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up the MySQL Database
 - Open MySQL and create a database:
   ```sql
   CREATE DATABASE student_db;
   ```
 - Use the database:
   ```sql
   USE student_db;
   ```
   or just right click on the database (student_db) and click on 'Set as default Schema'
 - Create the Students table:
   ```sql
   CREATE TABLE Students (
      id INT AUTO_INCREMENT PRIMARY KEY,
      name VARCHAR(100),
      age INT,
      grade VARCHAR(2)
    );
   ```


# 🎓 Student Management System

A simple command-line based Student Management System built with Python and MySQL. This project allows users to add, view, search, update, and delete student records from a MySQL database.

<img width="1536" height="1024" alt="student-management-system" src="https://github.com/user-attachments/assets/27092aae-169f-49d5-9988-ca71201d764a" />


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
### 5. Run the application
```bash
python src/main.py
```

---
## 📂 File Structure

<p align = "center">

| File/Folder | Description |
|:-------------:|:---------------------------------------------:|
| <b>src/main.py</b> | Main Python script with all CRUD operations |
| <b>sql/create_table.sql</b>	| SQL script to create the Students table |
| <b>requirements.txt</b> |	Python dependencies |
| <b>.gitignore</b> |	Git ignore rules |

</p>

---

## 🙌 Contributing
Contributions are welcome! Feel free to fork the repo and submit a pull request.

---

## 📄 License
This project is licensed under the MIT License.

---

## 💡 Author
Made with ❤️ by Vikas Vishwakarma

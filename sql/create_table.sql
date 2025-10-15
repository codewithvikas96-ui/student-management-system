-- Create the database
CREATE DATABASE student_db;

-- Use the database
USE student_db;

-- Create the Students table
CREATE TABLE Students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    grade VARCHAR(2)
);


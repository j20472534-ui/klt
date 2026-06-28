
CREATE DATABASE university_db;

USE university_db;
CREATE TABLE Students(
    StudentID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    Age INT NOT NULL,
    Phone VARCHAR(15),
    Major VARCHAR(100),
    GPA DECIMAL(3,2) NOT NULL,
    EnrollmentYear YEAR NOT NULL
);

-- Ma'lumotlar
INSERT INTO Students
(FirstName, LastName, Age, Phone, Major, GPA, EnrollmentYear)
VALUES
('Ali','Karimov',19,'+998931112233','Computer Science',3.75,2023),
('Vali','Aliyev',20,'+998941234567','Mathematics',3.95,2022),
('Hasan','Sobirov',18,'+998901111111','Computer Science',3.40,2024),
('Husan','Ergashev',21,'+998932223344','Physics',3.85,2021),
('Dilshod','Rahimov',22,'+998944445566','Mathematics',3.60,2020),
('Jamshid','Toshmatov',17,'+998951112233','Economics',3.20,2025),
('Aziza','Nazarova',19,'+998933334455','Computer Science',3.98,2023),
('Madina','Qodirova',20,'+998944447788','Biology',3.55,2022),
('Bekzod','Xolmatov',23,'+998935556677','Physics',3.90,2019),
('Malika','Yusupova',18,'+998977778899','Economics',3.45,2024);

SELECT *
FROM Students
WHERE Age > 18;

SELECT *
FROM Students
ORDER BY GPA DESC
LIMIT 5;

SELECT *
FROM Students
WHERE Phone LIKE '+99893%'
   OR Phone LIKE '+99894%';

SELECT Major, COUNT(*) AS StudentCount
FROM Students
GROUP BY Major;
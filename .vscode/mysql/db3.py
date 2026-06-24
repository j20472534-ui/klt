import pymysql

class MySQL:
    def __init__(self):
        self.ConnectDB()
        self.CreateTB()
        # self.InsertData()

    def ConnectDB(self):
        self.db = pymysql.connect(
            host='localhost',
            user='root',
            password='1234'
        )
        self.c = self.db.cursor()
        self.c.execute('CREATE DATABASE IF NOT EXISTS school')
        self.c.execute('USE school')

    def CreateTB(self):
        self.c.execute('''
            CREATE TABLE IF NOT EXISTS teachers(
                name VARCHAR(50),
                surname VARCHAR(50),
                salary INT,
                experience INT,
                branch VARCHAR(50))
        ''')
        self.c.execute('''
            CREATE TABLE IF NOT EXISTS students(
                name VARCHAR(50),
                surname VARCHAR(50),
                monthly_payment INT,
                course_duration INT,
                branch VARCHAR(50))
        ''')

    def InsertTeacher(self, name, surname, salary, experience, branch):
        self.c.execute(
            f'''INSERT INTO teachers(name, surname, salary, experience, branch)
            VALUES("{name}", "{surname}", {salary}, {experience}, "{branch}")''')
        self.db.commit()

    def InsertStudent(self, name, surname, monthly_payment, course_duration, branch):
        self.c.execute(
            f'''INSERT INTO students(name, surname, monthly_payment, course_duration, branch)
            VALUES("{name}", "{surname}", {monthly_payment}, {course_duration}, "{branch}")''')
        self.db.commit()

    # def InsertData(self):
    #     self.InsertTeacher('Ali', 'Karimov', 5000000, 5, 'Toshkent')
    #     self.InsertTeacher('Vali', 'Aliyev', 4500000, 3, 'Samarqand')
    #     self.InsertTeacher('Sardor', 'Toshmatov', 6000000, 7, 'Buxoro')
    #     self.InsertTeacher('Jamshid', 'Rasulov', 5500000, 6, 'Andijon')
    #     self.InsertTeacher('Bekzod', 'Hakimov', 4800000, 4, 'Namangan')
    #     self.InsertTeacher('Aziza', 'Qodirova', 5200000, 5, 'Fargona')
    #     self.InsertTeacher('Madina', 'Saidova', 4700000, 2, 'Qarshi')
    #     self.InsertTeacher('Bobur', 'Yusupov', 5100000, 4, 'Dubay')
    #     self.InsertTeacher('Kamol', 'Ergashev', 4900000, 3, 'Chilonzor')

    #     self.InsertStudent('Hasan', 'Karimov', 800000, 6, 'Toshkent')
    #     self.InsertStudent('Husan', 'Aliyev', 750000, 5, 'Samarqand')
    #     self.InsertStudent('Akmal', 'Tursunov', 900000, 8, 'Buxoro')
    #     self.InsertStudent('Dilshod', 'Raximov', 850000, 7, 'Andijon')
    #     self.InsertStudent('Sarvar', 'Nematov', 700000, 4, 'Namangan')
    #     self.InsertStudent('Malika', 'Qosimova', 950000, 9, 'Fargona')
    #     self.InsertStudent('Zarina', 'Sobirova', 1000000, 10, 'Qarshi')
    #     self.InsertStudent('Jasur', 'Mirzayev', 820000, 6, 'Dubay')
    #     self.InsertStudent('Nilufar', 'Tosheva', 780000, 5, 'Chilonzor')
    def query(self):
        self.c.execute('''select * from teachers order by salary''')
        self.db.commit()
        return self.c.fetchall()
    def query2(self):
        self.c.execute('''select * from teachers order by salary,order by experience desc''')
        self.db.commit()
        return self.c.fetchall()
    def query3(self):
        self.c.execute(''' update teachers  set salary=1000000 order by salary desc limit 1''')
        self.db.commit()
        return self.c.fetchall()
    def query4(self):
        self.c.execute('''update teachers branch set branch='Chilonzor' order by experience desc limit 1''')
        self.db.commit()
        return self.c.fetchall()
    def query5(self):
        self.c.execute('''select * from students order by surname''')
        self.db.commit()
        return self.c.fetchall()
    def query6(self):
        self.c.execute('''select * from students order by monthly_payment desc''')
        self.db.commit()
        return self.c.fetchall()
    def query7(self):
        self.c.execute('''select name,surname,monthly_payment*course_duration as total from students''')
        self.db.commit()
        return self.c.fetchall()
    def query8(self):
        self.c.execute('''update students set branch='Dubay' order by monthly_payment*course_duration desc limit 1  ''')
        self.db.commit()
        return self.c.fetchall()
    def query9(self):
        self.c.execute('''SELECT students.name, students.surname, teachers.name, teachers.surname, students.branch FROM students
                                   INNER JOIN teachers ON students.branch = teachers.branch  ''')
        self.db.commit()
        return self.c.fetchall()
    def query10(self):
        self.c.execute('''SELECT name, branch FROM students GROUP BY name, branch HAVING COUNT(name) > 1  ''')
        self.db.commit()
        return self.c.fetchall()
    def query11(self):
        self.c.execute(''' SELECT surname, monthly_payment FROM students GROUP BY surname, monthly_payment
                 HAVING COUNT(surname) > 1;''')
        self.db.commit()
        return self.c.fetchall()
    
obj = MySQL()
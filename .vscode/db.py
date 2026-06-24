    def sort(self):
        self.c.execute('''select * from company order by name''')
        self.db.commit()
        return self.c.fetchall()
    def capital(self):
        self.c.execute('''select * from company order by capital desc''')
        self.db.commit()
        return self.c.fetchall()
    def employee(self):
        self.c.execute('''select * from company order by employees_count limit 1''')
        self.db.commit()
        return self.c.fetchall()
    def location(self):
        self.c.execute('''select * from company where location LIKE 'tashkent' ''')
        self.db.commit()
        return self.c.fetchall()
    def ls(self):
        self.c.execute('''select location,count(*) from company group by location ''')
        self.db.commit()
        return self.c.fetchall()
    def ls2(self):
        self.c.execute(''' SELECT name, monthly_expense * (YEAR(NOW()) - YEAR(establishedAt)) * 12 AS total_expense FROM company''')
        self.db.commit()
        return self.c.fetchall()
    def CreateTB(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS restuarant(
                                id int auto_increment primary key,
                                name VARCHAR(50) NOT NULL,
                                address varchar(50) NOT NULL, 
                                maxFoodPrice int NOT NULL ,
                                minFoodPrice int NOT NULL,
                                employeesCount int not null,
                                experience int not null
                       )''')
    def InsertTB(self,name,address,maxFoodPrice,minFoodPrice,employeesCount,experience):
        self.c.execute(f'''insert into restuarant(name,address,maxFoodPrice,minFoodPrice,employeesCount,experience) 
                                                 VALUES
                            ( "{name}", "{address}", {maxFoodPrice}, {minFoodPrice},{employeesCount},{experience})''')
        self.db.commit()
        return self.c.fetchall()
    def least(self):
        self.c.execute(f'''select * from restuarant order by minFoodPrice limit 3''')
        self.db.commit()
        self.c.fetchall()
mysql=MySQL()
# for i in range(5):
#     mysql.InsertTB(input("Name: "), input("address: "), int(input("maxfoodprice:")), input("minfoodprice:"),int(input("employeescount:")),int(input("experience:")))
# mysql.sort()
# mysql.capital()
# mysql.employee()
# mysql.ls()
# mysql.ls2()
mysql.least()


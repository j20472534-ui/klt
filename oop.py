# class book:
#     def __init__(self,name,author,cost,publisher):
#        self.name=name
#        self.author=author
#        self.cost=cost
#        self.publisher=publisher
#     def display(self):
#         if self.publisher[0].lower()>='a' and self.publisher[0].lower()<='h':
#             print(f"Name: {self.name}, Author: {self.author}, Cost: {self.cost}, Publisher: {self.publisher}")
# b1=book("python","xyz",500,"abc")
# b2=book("mysqll","pqr",600,"def")
# b3=book("c++","lmn",700,"ghi")
# b4=book("javascript","uvw",800,"jkl")
# b5=book("html","rst",900,"mno")
# lst=[b1,b2,b3,b4,b5]
# for i in lst:
#     i.display()

# ---------------------------------------

# class computer:
#     def __init__(self,name,ram,cost,processpor):
#         self.name=name
#         self.ram=ram
#         self.cost=cost
#         self.processpor=processpor
#     def display(self):
#         if self.ram>4 and self.ram<16:
#             print(f"Name: {self.name}, Ram: {self.ram}, Cost: {self.cost}, Processpor: {self.processpor}")
# k1=computer("dell",4,50000,"i5")
# k2=computer("hp",16,60000,"i7")
# k3=computer("lenovo",8,70000,"i9")
# k4=computer("asus",12,80000,"i11")
# k5=computer("acer",128,90000,"i13")
# lst=[k1,k2,k3,k4,k5]
# for i in lst:
#     i.display()

# ---------------------------------------

# class user:
#     def __init__(self,name,username,email):
#         self.name=name
#         self.username=username
#         self.email=email
#     def get_info(self):
#         print(f"Name: {self.name}, Username: {self.username}, Email: {self.email}")
# u1=user("ALI","ali123","ali@example.com")
# u2=user("AHMED","ahmed456","ahmed@example.com")
# u3=user("USMON","usmon789","usman@example.com")
# u4=user("VALI","vali123","vali@example.com")
# u5=user("AHMAD","ahmad456","ahmad@example.com")
# lst=[u1,u2,u3,u4,u5]
# for i in lst:
#     i.get_info()


# class population:
#     def __init__(self,name,age,jins):
#         self.name=name
#         self.age=age
#         self.jins=jins
#     def get_info(self):
#      if self.age>50:
#         if self.jins=="male":
#          print(f"name: janob {self.name} , age: {self.age}, jins: {self.jins}")
#         else:
#            print(f"name: xonim {self.name} , age: {self.age}, jins: {self.jins}")
# h1=population("jack",17,"male")
# h2=population("john",68,"male")
# h3=population("jessica",19,"female")
# h4=population("anna",76,"female")
# h5=population("joseph",20,"male")
# lst=[h1,h2,h3,h4,h5]
# for i in lst:
#    i.get_info()

class employee:
    def __init__(self,surname,position,salary):
        self.surname=surname
        self.position=position
        self.salary=salary
class EnterpriseEmployee(employee):
    def __init__(self,surname,position,salary,rating):
        super().__init__(surname,position,salary)
        self.rating=rating
        100<=rating>=0
    def increased_salary(self):
        t=self.salary*1.20
        f=self.salary*1.40
        s=self.salary*1.60
        if not self.rating<0 or self.rating>100:
         if 60<=self.rating<75:
            self.salary+=t
         elif 75<=self.rating<90:
            self.salary+=f
         elif 90<=self.rating<100:
            self.salary+=s
        else:
           print("reyting 0 va 100 oraligida bolishi kerak")
e1=EnterpriseEmployee("aliyev","programmist",170000,80)
e2=EnterpriseEmployee("valiyev","muhandis",200000,70)
e3=EnterpriseEmployee("valiyeva","teacher",300000,60)
e4=EnterpriseEmployee("aliyeva","coder",670000,97)
e5=EnterpriseEmployee("malikov","support",390000,101)
lst=[e1,e2,e3,e4,e5]
for i in lst:
   i.increased_salary
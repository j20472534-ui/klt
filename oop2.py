# class AnagramChecker:
#     def check(self, word1, word2):
#         return sorted(word1.lower()) == sorted(word2.lower())
# s1 = AnagramChecker()
# print(s1.check("listen", "silent"))
# print(s1.check("hello", "world"))

# class CaesarCipherNumbers:
#     def encrypt(self,numbers):
#         result = []
#         for i in numbers:
#             shifted = "".join(map(lambda x: str((int(x) + 3) % 10), i))
#             result.append(shifted)
#         return result
# s2 = CaesarCipherNumbers()
# numbers = ["37412", "9999", "12345", "0000", "56789"]
# print(s2.encrypt(numbers))

# class Student:
#     def __init__(self, name, student_id):
#         self.name = name
#         self.student_id = student_id
#         self.__grades = []
#     def add_grade(self, grade):
#         if 0 <= grade <= 100:
#             self.__grades.append(grade)
#         else:
#             print("Xato: Noto'g'ri baho")
#     def calculate_average(self):
#         return sum(self.__grades) / len(self.__grades)
#     def get_status(self):
#         avg = self.calculate_average()
#         if avg >= 90: return "A'lo"
#         elif avg >= 80: return "Yaxshi"
#         elif avg >= 70: return "Qoniqarli"
#         else: return "Qoniqarsiz"
# s3 = Student("Nodira", "S123")
# s4 = Student("Ali", "S124")
# s5 = Student("Vali", "S125")
# s3.add_grade(85)
# s3.add_grade(90)
# s4.add_grade(75)
# s4.add_grade(80)
# s5.add_grade(60)
# s5.add_grade(65)
# students = [s3, s4, s5]
# for s in students:
#     print(f"{s.name} | avg: {s.calculate_average()} | status: {s.get_status()}")

# def count_passing_students(grades: list[int], passingGrade: int) -> int:
#     count = 0

#     for grade in grades:
#         if grade >= passingGrade:
#             count += 1

#     return count
# grades = [45, 60, 75, 30, 90]
# passingGrade = 60

# print(count_passing_students(grades, passingGrade))
# def ends_with_gram(words: list[str]) -> list[str]:
#     result = []

#     for word in words:
#         if word.lower().endswith("gram"):
#             result.append(word)

#     return result

# words = ["telegram", "Instagram", "hello", "program", "diagram", "world"]

# print(ends_with_gram(words))

# class Employee:
#     def __init__(self, name: str, employee_id: str, hourly_rate: float = 15.0):
#         self.name = name
#         self.employee_id = employee_id
#         self.__working_hours = []
#         self.hourly_rate = hourly_rate

#     def log_hours(self, hour: int) -> bool:
#         if 0 <= hour <= 24:
#             self.__working_hours.append(hour)
#             return True
#         return False

#     def total_hours(self) -> int:
#         return sum(self.__working_hours)

#     def calculate_salary(self) -> float:
#         return self.total_hours() * self.hourly_rate

#     def reset_hours(self) -> None:
#         self.__working_hours.clear()


# employee = Employee("Javlon", "E101", 20.0)

# print(employee.log_hours(8))
# print(employee.log_hours(9))
# print(employee.log_hours(10))
# print(employee.log_hours(25))

# print(employee.total_hours())
# print(employee.calculate_salary())

# employee.reset_hours()

# print(employee.total_hours())
# print(employee.calculate_salary())


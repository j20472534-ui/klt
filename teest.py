# lst=[[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]] 
# new=[]
# for i in lst[::-1]:
#     if i not in new:
#         new.append(i)
# print(new)
# a=input()
# b=input()
# c=[]
# for i in range(len(a)):
#     c.append([])

#     for j in range(len(b)):
#         c[i].append(a[i][j] + b[i][j])
# # print(c)
# def count_passing_students(grades: list[int], passingGrade: int) -> int:
#     passingGrade=60
#     count = 0
#     for grade in grades:
#         if grade >= passingGrade:
#             count += 1
#     return count
# n=int(input())
# grades=[]
# for i in range(n):
#     ball=input()
#     grades.append(int(ball))
# passingGrade=60
# print(count_passing_students(grades, passingGrade))
# nums=[1,2,2,3,4,4,5]
# new=tuple(set(nums))
# print(new)
# words=["apple", "banana", "grape", "apple", "grape"]
# print(tuple(set(sorted(words))))
# students = [("Ali", 85), ("Vali", 72), ("Soli", 91)]
# print()sorted(students, key=lambda x: x[1], reverse=True))
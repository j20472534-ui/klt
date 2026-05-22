# list=["Salom","Dunyo","phyton"]
# count=0
# for i in list:
#     for x in i:
#      if x.islower():
#         count+=1
# print(count)


# list=[True,1,False,"salom",0]
# for i in list:
#     if type(i)==bool:       
#      print(i)


# list=[1,20,10,28,20]
# print(max(list))


# list=[True,"salom",5,5.6]
# n=[]
# for i in list:
#  n.append(type(i))
# print(n)

 
# list=[7,8,1,3,4,6,7,5]
# natija=[]
# for i,value in enumerate(list):
#     if i%2==0:
#        print(value**2,end=" " )
#     else:
#        print(value**3,end=" " )


# list=["salom","dunyo","phyton"]
# for i in list:
#     list.reverse()
# print(list)

# lst = ["olma", "shaftoli", "nok", "uzum"]
# max = ""
# for i in lst:
#     if len(max) < len(i):
#         max = i
# print(max)

# list=[0,1,2,3,4,0,2,0,2,5,3,0,0,3,2,7,8,0,6,4,0,4,3,9]
# for i in range(list.count(0)):
#       list.remove(0)
#       list.append(0)
# print(list)


# lst = [100, 23, 76, 40, 19]
# x = lst[0]
# for i in lst:
#     if i > x:
#         x = i     
# lst.remove(x)
# z = lst[0]
# for i in lst:
#     if i > z:
#         z = i
# print(z)

# lst = [1,2,2,1,4,5,6,7,8,8,9,10,2,3,4,6] 
# n = []
# for i in lst:
#     if i not in n:
#         n.append(i)
# print(n)

# a=[1,2,3,4,5,6]
# b=[1,2,3,4,5,6,8,9]
# r=0
#     n=a+b
#     r=sum(n)/len(n)
# print(r)

# list=[11,33,55,77]
# r=""
# for i in list:
#     r+=str(i)
#     int(r)
# # print(r)


# a=["ada",212,False,4567,"aziza"]
# for i in  a:
#   s=str(i)
#   if s[::-1]==s:
#     print(f"{i}->polindrom")
#   else:
#     print(f"{i}->polindrom emas")


# a=["ada",212,False,4567,"aziza"]
# count=0
# for i in  a:
#   s=str(i)
#   if s[::-1]==s and len(a)>=2:
#     count+=1
# print(count)

# list=[11,22,33,44,55,66]
# n=list=[11,22,33,44,55,66]
# n=[]
# for i in list:
#     if i%2==0:
#       n.remove(i)
# print(n)

# lists = [[1,2,3], [4,5,6], [9,27], [2,0,10], [0,1], [1], [2,2,2]]
# max_sum = -1
# result = []
# for lst in lists:
#     if len(lst) >= 2:
#         s = sum(lst)
#         if s > max_sum:
#             max_sum = s
#             result = lst
# print(result)

# lst=input().split()
# s=""
# for i in lst:
#     s=s+i
# s=int(s)
# s+=1
# print(s)

# a=[1,2,3,4,5,6,7,8]
# b=[1,2,3,4,6,8,9,10]
# new=[]
# for i in a:
#     if i in b:
#         new.append(i)
# print(new)
 
# lst = [5,3,8,1]
# rise = True
# fall = True
# for i in range(len(lst)-1):
#     if lst[i] < lst[i+1]:
#         fall = False
#     elif lst[i] > lst[i+1]:
#         rise = False
# if rise and not fall:
#     print("o'sish")
# elif fall and not rise:
#     print("kamayish")
# else:
#     print("tartibsiz")
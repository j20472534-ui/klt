# lst=[1,2,33,5,6,7]
# n=8
# new=[]
# for i in lst:
#     for x in lst:
#         if lst.index(i) !=lst.index(x):
#             if i+x==n:
#                 if lst.index(i) and lst.index(x) not in new:
#                     new.append(lst.index(x))
#                     new.append(lst.index(i))
# print(new)

# lst=[2,4,6,8]
# n=[i*2 for i in lst]
# print(n)

# lst=[(10,20,30),(40,50,60),(70,80,90)]
# new=[]
# for i in lst:
#    new.append(i[:-1]+(100,))
# print(new)

# lst=[(""),("a","b","c"),("a","b"),("f","j"),(),("h","n"),()]
# n=[i for i in lst if i]
# print(n)

# lst = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
# for i in range(len(lst)):
#     for x in range(len(lst)-1):
#        if lst[x][1] < lst[x+1][1]:
#            lst[x],lst[x+1]=lst[x+1],lst[x]
# print(lst)

# s="python 3.0"
# new=[]
# for i in s:
#     new.append(i)
# print(tuple(new))


# lst=[1,2,3,4]
# new=[]
# prefix="emp"
# for i in lst:
#     new.append(prefix+str(i))
# print(new)

# gap = "salom aziz qalaysan"
# lst = gap.split()
# for i in range(len(lst)):
#     for j in range(len(lst)-1):
#         if len(lst[j]) > len(lst[j+1]):
#             lst[j], lst[j+1] = lst[j+1], lst[j]
# print(lst)

# lst=[1,2,True,"dunyo","salom",False]
# new=[]
# for index,i in enumerate(lst):
#     if type(i)==str:
#         new.append(i)
# print(new)

# t=(1,2,4,-4,-4,-2,-1,-9)
# n=tuple(i for i in t if i>0)
# print(n)

# lst = ['salom', 23, 'dunyo', 5, 100, 'python']
# strings=[]
# nums=[]
# for i in lst:
#     if type(i)==str:
#         strings.append(i)
#         sorted(strings,reverse=True)
#     elif type(i)==int:
#         nums.append(i)
# nums.sort(reverse=True)
# print(strings)
# print(nums)

# lst=[(3,10),(1,20),(2,30)]
# for i in lst:
#     lst.sort()
# print(lst)

# lst=[1,2,3,4]
# n=[i**2 for i in lst]
# print(n)

# lst=["salom","dunyo","foundation"]
# n=[]
# for i in  lst:
#     n.append((i.capitalize()))
# print(n)

# t=(1,2,3,4,5)
# natija=0
# for i in t:
#     natija+=i
# print(natija)
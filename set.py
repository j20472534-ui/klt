# def a(a,b):
#     count=0
#     print(a, end="")
#     while a>b:
#         a=a/2
#         if a>b:
#           print(" ->",a, end="")
#           count+=1
#     return count

# natija = a(int(input()), int(input()))
# print(natija)


# def bigger_price(n, lst):
#     return sorted(lst, key=lambda x: x['price'])[-n:]

# son = int(input())
# n = int(input())
# lst = []
# for i in range(n):
#     name = input()
#     price = int(input())
#     lst.append({"name": name, "price": price})

# natija=bigger_price(son, lst)
# print(natija)


# def steal(a,b):
#     p,p1=0,0
#     for  i in range(len(L1)):
#         a,b=L1[i],L2[i]
#         if a=="share" and b=="share":
#             p+=5
#             p1+=5
#         elif a=="steal" and b=="share":
#             p+=6
#             p1+=2
#         elif a=="share" and b=="steal":
#             p+=2
#             p1+=6
#         elif a=="steal" and b=="steal":
#             p+=3
#             p1+=3
#         return [p,p1]
# n=int(input())
# L1=input().split()
# L2=input().split()
# print(steal(L1,L2))  
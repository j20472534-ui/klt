# def get_top_user(data):
#     score={}
#     for user,ball in data:
#         if user in score:
#             score[user]+=ball
#         else:
#              score[user]=ball
#     return  max(score,key=lambda x: score[x])
    

# n=int(input())
# data=[]
# for i in range(n):
#         user,ball=input().split()
#         data.append((user,int(ball)))
# print(get_top_user(data))

# def format_date(date):
#     month = ["Yanvar", "Fevral", "Mart", "Aprel", "May", "Iyun",
#              "Iyul", "Avgust", "Sentabr", "Oktabr", "Noyabr", "Dekabr"]
    
#     day, oy, year = date.split(".")
    
#     return f"{int(day)} {month[int(oy)-1]} {year} yil"

# print(format_date(input()))

# def ends_with_gram(word):
#     return [i for i in word if i[-4:].lower()=="gram"]


# print(ends_with_gram(input().split()))

# def count_passing_students(grade,passingGRADE):
#     lst=[i for i in grade  if i>=passingGRADE]
#     return len(lst)

# n=int(input())
# passingGRADE=int(input())
# grades=list(map(int,input().split()))
# print(count_passing_students(grades,passingGRADE))


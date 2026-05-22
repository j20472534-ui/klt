# import json
# f = open("test.json")
# natija=json.load(f)
# for i in natija:
#  if i['price']>=500 and i['price']<=1000 and i['is_available']==True:
#   print(f"{i['id']},{i['material']}")
# f.close()

# import json
# f=open("test.json")
# natija=json.load(f)
# user=input()
# new=[]
# for i in natija:
#     if user==i['material'] and i['is_available'] == True:
#        new.append(i['price'])

# print(sorted(new))
# f.close(
       


# import json
# f=open("test.json")
# n=json.load(f)
# dik = {}
# for k, v in n.items():
#     print(f"\nStudent: {k}")
#     for k1, v1 in v.items():
#         avg = sum(v1) / len(v1)
#         print(f"Fan: {k1} | {avg:.1f}")


# import json
# f=open("test.json")
# n=json.load(f)
# new=[]
# for k,v in  n.items():
#     for k1 in v:
#      new.append(k1['name'])
# print(new)
# f.close()

# import json
# f=open("test.json")
# n=json.load(f)
# sum=0
# for k,v in n.items():
#     for k1 in v:
#      sum+=k1['age']
# print(sum)
# f.close()


# import json
# f=open("test.json")
# n=json.load(f)
# for k,v in n.items():
#     for k1 in v:
#         print(f"{k1['name']}: {k1['price']}")


import json
f=open("test.json")
n=json.load(f)
players=n["oyinchilar"]

top3=sorted(players,key=lambda x:x["ball"],reverse=True)[:3]
for i in top3:
   print(f"{i['ism']}: {i['ball']}")
the_lowest=min(players,key=lambda x: x['ball'])
print(f"{the_lowest['ism']} ({the_lowest['ball']})")
players.remove(the_lowest)
      

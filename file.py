# f=open("test.txt","r")
# for i in f.read().split():
    
#     if i.lower()==i[::-1].lower():
#         print(i)
# f.close()


# dct={}
# count=0
# f=open("test.txt",encoding="utf-8")

# for i in f.read().split('\n'):
#     davlat = i.split(',')[-1]
#     if davlat not in dct:
#         dct[davlat] = 1
#     else:
#         dct[davlat] += 1

# print(dct)
# f.close()

# st=set()
# f=open("test.txt",encoding="utf-8")
# for i in f.read().split("\n"):
#     v=i.split(',')[1]
#     cntry = i.split(',')[-1]
#     if "visa" in v:
#        st.add(f"{v},{cntry}")
# natija=sorted(st)
# print(natija)
       
# f=open("test.txt",encoding="utf-8")
# for i in f.read().split("\n"):
#     card=i.split(',')[0]
#     cntry=i.split(',')[-1]
#     v=i.split(',')[1] 
#     cmpny=i.split(',')[4]
#     print(i[0])
#     if len(set(card))==10:
#         print(i)
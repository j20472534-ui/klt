#  def last_unique_character(text: str):
#     count=0
#     for i in text[::-1]:
#           if text.count(i)==1:
#            return i
#     return "_"

# text=input()
# n=last_unique_character(text)
# print(n)

# ------------------------------------------------------------------

# def analyze_floats_in_text(text:str):
#     text=text.replace(",", " ")
#     word=text.split()
#     floats=[]
#     for i in word:
#         try:
#            num=float(i)
#            if "." in i:
#                floats.append(num)
#         except ValueError:
#            pass
#     if not floats:
#         return {"average": 0,"min": 0,"max": 0}
#     average=round(sum(floats)/len(floats),2)
#     maks=max(floats)
#     minm=min(floats)
#     return {"average": average,"max": maks,"min": minm}
# text=input()
# n=analyze_floats_in_text(text)
# print(n)
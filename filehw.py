
# with open("test.txt", encoding="utf-8") as f:
#     lines = f.read().split("\n")[1:]
# brand_count = {}
# for line in lines:
#     brand = line.split(",")[-4]
#     if brand in brand_count:
#         brand_count[brand] += 1
#     else:
#         brand_count[brand] = 1
# top_brand = max(brand_count, key=brand_count.get)
# print("Top brend:", top_brand, "->", brand_count[top_brand])
# country_count = {}
# for line in lines:
#     brand = line.split(",")[-4]
#     country = line.split(",")[-1]
#     if brand == top_brand:
#         if country in country_count:
#             country_count[country] += 1
#         else:
#             country_count[country] = 1
# max_country = max(country_count, key=country_count.get)
# min_country = min(country_count, key=country_count.get)
# # print("max:", max_country, "->", country_count[max_country])
# print("min:", min_country, "->", country_count[min_country])

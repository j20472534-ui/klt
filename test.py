# import json
# def count_languages(filename: str):
#     with open(filename, encoding="utf-8") as f:
#         data = json.load(f)
#     counts = {}
#     for i in data:
#         language = i.get("language")
#         if language:
#             counts[language] = counts.get(language, 0) + 1
#     return dict(sorted(counts.items()))

# language_counts = count_languages("country.json")
# print(language_counts)

# def count_characters(file: str):
#     with open(file, encoding="utf-8") as f:
#         text = f.read()
#     return dict((char, text.count(char)) for char in set(text))
# print(count_characters("string.txt"))
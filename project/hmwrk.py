def majority_element(nums):
    return max(nums, key=nums.count) if nums else -1
nums=[2,3,3,4,5,7,8,9,3,2]
print(majority_element(nums))





def cinemas(film,genre):
    return [i for i in film if i["genre"]==genre]
cinema = [
    {"title": "Avatar", "genre": "Fantastika", "price": 40000},
    {"title": "Sherlock", "genre": "Detektiv", "price": 30000},
    {"title": "Oq yol", "genre": "Drama", "price": 25000},
    {"title": "Dune", "genre": "Fantastika", "price": 35000}
]
genre=input()
print(cinemas(cinema,genre))
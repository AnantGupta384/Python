# list1 = [["Anant", 2], ["Monika", 4], ["Manish", 100], ["Shagun", 1]]

# dict1 = dict(list1)

# for item in dict1:
#     print(item)
# for item, roti in dict1.items():
    # print(item, "eats roti a day is", roti)

items = [10, 11, 15, 17, 1.8, 8.6, "Anant", "Harry"]

for items in items:
    if str(items).isnumeric() and items>6:
        print(items)

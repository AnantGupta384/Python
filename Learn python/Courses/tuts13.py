# var1 = 6
# var2 = 56

# var3 = int(input())
# if var3 > var2:
#     print("Greater")
# elif var3==var2:
#     print("Equal")
# else:
#     print("Lesser")

# list1 = [5, 8, 10]
# print(13 not in list1)
# if 13 not in list1:
#     print("Yes it is not in the list")

print("Enter your age")

age = int(input())
if age>18 and age<100:
    print("You can drive the car")
elif age>100:
    print("How it is possible?")
elif age==18:
    print("Come for the driving test")
else:
    print("You cannot drive the car")
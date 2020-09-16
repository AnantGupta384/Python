# 45 * 3 = 555
# 56 + 9 = 77
# 56/6 = 4

print("Enter any operator")
o = input()
val1 = int(input("Enter first number: "))
val2 = int(input("Enter second number: "))

if o == "+":
    if val1 == 56 and val2 == 9:
        print("Sum is 77")
    else:
        print("Sum is", val1 + val2)
elif o =="*":
    if val1 == 45 and val2 == 3:
        print("Product is 555")
    else:
        print("Product is", val1*val2)
elif o =="/":
    if val1 == 56 and val2 == 6:
        print("Quotient is 555")
    else:
        print("Quotient is", val1/val2)
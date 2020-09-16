# i = 0

# while (True):
#     if i + 1<5:
#         i = i+1
#         continue


#     print(i, end = " ")
#     if (i==45):
#         break # Stop the loop
#     i = i+1
#     # Yahan par

while (True):
    print ("Enter a number")
    n = int(input())

    if n>=100:
        print("Congrats you have won the game")
        break
    else:
        print("Enter a bigger number")
        continue
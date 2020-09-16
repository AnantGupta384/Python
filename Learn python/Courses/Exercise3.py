n=67
number_of_guesses=1
print("Number of guesses is limited to only 9 times: ")
while (number_of_guesses<=9):
    guess_number = int(input("Guess the number :\n"))
    if guess_number<67:
        print("Enter a big number\n")
    elif guess_number>67:
        print("Enter a smaller number\n ")
    else:
        print("Congrats you won!!!\n")
        print("You took", number_of_guesses, "to finish the game")
        break
    print(9-number_of_guesses,"no. of guesses left")
    number_of_guesses = number_of_guesses + 1

if(number_of_guesses>9):
    print("Game Over")
    
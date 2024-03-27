from random import randint
num=randint(1,100)
# print(num)
chances=5
while chances>0:
    try:
        userResponse=input("Guess the number:")
        if userResponse==num:
            print("YOU WON THE GAME")
            break
        elif userResponse>num:
            chances-=1
            print("Guessed Number is Greater than actual Number")
        elif userResponse<num:
            chances-=1
            print("Guessed Number is Less than actual Number")
    except ValueError:
        print("Invalid input!! Please enter an integer")
else:
    print("You Lost the Game")
    print("The actual Number is :",num)
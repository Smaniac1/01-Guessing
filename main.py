import random

Quit = False

while not Quit:
    #Start up message to the user
    print("Hello user, this program allows you to play a guessing game"\
    " with the computer. The computer will select a number between 1 and"\
    " your max number and you will have to guess which number the computer has"\
    " selected.")
    print("The program will also keep a running total on how many times you guessed")

    #Have the program select a number between 1 and the players number
    Max = int(input("Please enter the maximum number you want:"))
    Computer = random.randint(1, Max)
    
    #Setup the counter
    Counter = 0
    
    #Tell the user that the computer has choosen and it is time to guess
    print("The computer has choosen a number")
    User = int(input("Please guess a number:"))
    
    #Set up the loop
    while User != Computer :
        Counter += 1
        print("You guessed wrong")
        if User > Computer:
            print("It was to high")
            User = int(input("Please try a diffrent number:"))
        elif User < Computer:
            print("It was to low")
            User = int(input("Please try a diffrent number:"))
    
    #Once they guessed right
    print("Congradulations user, you guessed the right number which was", \
    User ,"you guessed a total of", Counter ,"times!")
    PlayAgain = input("Would you like to play again (yes or no)?")
    PlayAgain = PlayAgain.lower()
    if PlayAgain == "yes" or PlayAgain == "y":
        Quit = False
    else:
        Quit = True

print("Thanks for playing, hope you come back again!")

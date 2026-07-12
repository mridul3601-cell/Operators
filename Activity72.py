import random
playing = True
number = str (random.randint(0,9))
print("I will genarte a number 0 to 9 and you will have to guess the number 1 digit at a time")
print("the game ends when you get 1 her0!")
while playing:
    guess = input("give me your best guess!\n")
    if number == guess:
        print("you winn the game")
        print("the number was", number)
        break
    else:
        print("your guess wasn't quite right, try again\n")
              
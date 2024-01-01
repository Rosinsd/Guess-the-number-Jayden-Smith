from random import randint
x = int(input("What is your guess for the number?"))
random_number = randint(1, 6)   
if x == random_number:
    print("you got the number right")
else:
    print("You got the number wrong")
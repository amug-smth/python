import random
num=int(input("Enter a number from 0 to 100: "))
print("The computer chooses:",random.randint(0,100))
if num==random.randint(0,100):
    print("Congrats! You guessed the number!")
else:
    print("You guessed the wrong number.")
import random
print("Press r for rock, p for paper, s for scissors")
choices=["r", "p", "s"]
gam=input("Enter your choice: ")
comp=random.choice(choices)
print("Yo chose:", gam)
print("Computer chose:", comp)
if gam==comp:
    print("It's a tie!")
elif gam=="r" and comp=="s":
    print("You win! Rock crushes scissors.")
elif gam=="p" and comp=="r":
    print("You win! Paper covers rock.")
elif gam=="s" and comp=="p":
    print("You win! Scissors cut paper.")
else:
    print("Invalid choice! You have to choose r, p, or s.")
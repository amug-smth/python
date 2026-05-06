try:
    nam=int(input("Enter your age: "))
    if nam<18:
        print("You cannot vote")
    else:
        print("You can vote")
except ValueError:
    print("Invalid input. Please enter a valid age.")
if nam%2==0:
    print("Wow, your age is even!")
elif nam%3==0:
    print("Wow, your age is odd!")
else:
    print("Your age is neither even nor odd.")
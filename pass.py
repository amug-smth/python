for i in range(21):
    if i%3 == 0:
        print("Buzz")
    elif i%5 == 0:
        print("Fizz")
    elif i%15 == 0:
        pass
    elif i%20 == 0:
        print("Twist")
    else:
        print(i)

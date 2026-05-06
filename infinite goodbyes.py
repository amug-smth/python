while True:
    try:
        num=int(input("Enter a number: "))
        while num%2==0:
            print("bye")
    except ValueError:
        print("Invalid")

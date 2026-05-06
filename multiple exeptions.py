try:
    num1=int(input("Enter the first number: "))
    num2=int(input("Enter the second number: "))
    result=num1/num2
    print(f"The quotient of {num1} and {num2} is: {result}")
except ZeroDivisionError:
    print("We can't divide by zero")
except:
    print("wrong input")
finally:
    print("I'm always going to be printed")
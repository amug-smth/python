rad=(input("Enter the radius of the circle you want to calculate the circumference of: "))
pi= 3.14
def circumference(rad):
    return 2*pi*rad
print("The circumference of the circle is: ", circumference(float(rad)))
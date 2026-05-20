str=["efg","abc","def","xyz","pqr","efg"]
print(str)
print(f"the count of efg is {str.count('efg')}")
if str[0]==str[-1]:
    print("same")
else:
    print("not same")
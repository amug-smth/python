list=[1,2,3,4,5,6,7,8,9,10]
print(list)
count=0
for i in list:
    count+=1
print(count)
avg=count/len(list)
print(f"the average of this list is {avg}")
print(max(list))
print(min(list))
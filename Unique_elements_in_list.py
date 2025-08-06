list=[]
n= int (input("Enter number of elements:"))
for i in range(n):
    value=int(input("Enter element:"))
    list.append(value)
unique=[]
for item in list:
    if item not in unique:
        unique.append(item)
print("Unique element",unique)

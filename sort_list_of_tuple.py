l=[(5,2),(1,4),(3,1),(6,3)]
n=len(l)
for i in range(n):
    for j in range(0,n-i-1):
        if l[j][1]>l[j+1][1]:
            l[j],l[j+1]=l[j+1],l[j]
print("Sorted list : ",l)

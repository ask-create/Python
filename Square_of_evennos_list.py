m=int(input("Enter the starting no."))
n=int(input("Enter the ending no."))
even_squares = {x**2 for x in range(m,n+1)if x%2==0}
print("Set of squares of even numbers:",even_squares)

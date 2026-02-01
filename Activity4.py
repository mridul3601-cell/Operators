import math

print("Square Root Calculator")

n = int(input("Enter a number: "))

if n < 0:
    print("Square root is not defined for negative numbers.")
else:
    result = math.sqrt(n)
    print("The square root of", n, "is", result)
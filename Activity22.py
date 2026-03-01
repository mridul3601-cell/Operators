a = input("Enter first number: ")
b = input("Enter second number: ")
c = input("Enter third number: ")

print("Before swapping:")
print(a, b, c)

# Swap them (rotate)
a, b, c = b, c, a

print("After swapping:")
print(a, b, c)
print("enter a number(numerator):")
num=int(input())
print("enter a number(denominator):")
numd=int(input())

if num%numd==0:
    print("\n is" +str(num) +"is divisible by"+str(numd))
else:
     print("\n is" +str(num) +"is not divisible"+str(numd))

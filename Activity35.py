num= int(input("please enter a number to reverse"))

sum= 0

temp=num

while temp>0:
    digit= temp % 10
    sum= sum *10+digit
    temp //=10
print("the reversed number is" , sum)

num1 = (input("please enter a number"))
num2 = (input("please enter another number"))
sum_ans = int(num1)+int(num2)
print(sum_ans)
symbol = input("please enter the operation(+.-,*,/) :")
num1 = input("please enter you first number: ")
num2 = input("please enter you second number: ")

if symbol == '+':
    sum_ans = int(num1) + int(num2)
    print("My sum is: " , sum_ans)

if symbol == '-':
    sum_ans = int(num1) - int(num2)
    print("My difference is: " , sum_ans)

if symbol == '*':
    sum_ans = int(num1) * int(num2)
    print("My product is: " , sum_ans)

if symbol == '/':
    sum_ans = int(num1) / int(num2)
    print("My quotient is: " , sum_ans)

if symbol == '**':
    sum_ans = int(num1) ** int(num2)
    print("My exponent is: " , sum_ans)


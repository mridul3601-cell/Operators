Actual_cost= float(input("please enter Actual amount"))
sale_amount= float(input('please enter the sales amount'))
if sale_amount>Actual_cost:
 print ('profit ')
 profit = sale_amount - Actual_cost
 print ('you got a profit of',profit)
else: 
 print('you got no profit')

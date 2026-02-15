print("please enter marks obtained in subjects")

mark1= int(input())
mark2= int(input())
mark3= int(input())
mark4= int(input())
mark5= int(input())


tot = mark1+mark2+mark3+mark4+mark5

avg = tot/5

if avg>=91 and avg<=100:

    print("you have a A1 grade")

elif avg>=81 and avg<=91:

    print("you have a A2 grade")

elif avg>=71 and avg<=81:

    print("you have a B1 grade")

elif avg>=61 and avg<=71:

    print("you have a B2 grade")

elif avg>=51 and avg<=61:

    print("you have a C1 grade")

elif avg>=41 and avg<=51:

     print("you have a C2 grade")
print(" Half a pyamid of stars (*) : ")
n = int(input("please enter number of stars"))
for i in range (n) :
    for j in range (i+1) :
        print("*", end= "")
    print()
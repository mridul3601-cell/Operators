n = int(input("enter a number"))
note1 = n//100
note2 = (n%100)//50
note3 = ((n%100)%50)//10
print("100 notes are",note1)
print("50 notes are", note2)
print("10 notes are", note3)

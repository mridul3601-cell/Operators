string = input ("please enter a word")
char = input (" please enter your own alphabet")
i= 0
count= 0
while (i<len (string)) :
    if(string[i] == char) :
        count = count + 1
    i = i+1

print("the total times" , char, " has occured =" , count)


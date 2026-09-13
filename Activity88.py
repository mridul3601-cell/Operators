a = {'100':5,'101':8,'102':11,'103':14}
count = 0
for c in a.values():
    if c ==5:
        count=count+1
        print('count',count)
marks = [85, 90, 78, 92, 88]

print("Marks:", marks)
print("Number of marks:", len(marks))
print("First mark:", marks[0])
print("Last mark:", marks[-1])
print("First 3 marks:", marks[:3])

total = sum(marks)
average = total / len(marks)

print("Total:", total)
print("Average:", average)
print("Smallest:", min(marks))
print("Largest:", max(marks))

for mark in marks:
    print("Mark:", mark)
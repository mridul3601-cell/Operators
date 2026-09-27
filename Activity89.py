students = {'Alex':'Math','Sam':'Science','Jordan':'English','Taylor':'Math'}

print(students)

print(students.values())

print(students.keys())

print(students.items())

# Access a student
print(students.get('Alex'))

# Add a student
students['Chris'] = 'History'

# Update a student
students['Sam'] = 'Math'

# Remove a student
students.pop('Jordan')

# Dictionary length
print(len(students))

# Print final records
for c in students:
    print(c, students[c])
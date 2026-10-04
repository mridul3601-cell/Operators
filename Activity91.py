box1 = {"chips", "cookies", "apple", "juice"}
box2 = {"cookies", "banana", "juice", "granola"}

print("Box 1:", box1)
print("Box 2:", box2)

box1.add("crackers")
print("Box 1 after adding crackers:", box1)

shared_snacks = box1.intersection(box2)
print("Shared snacks:", shared_snacks)

snack_counts = [5, 10, 3, 8, 10]

print("Snack counts:", snack_counts)

snack_counts.append(7)
print("After adding 7:", snack_counts)

print("Number of 10s:", snack_counts.count(10))

snack_counts.reverse()
print("Reversed array:", snack_counts)
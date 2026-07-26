import random
import math

print("Lucky Number:", random.randint(1, 100))

activities = ["Read", "Walk", "Game"]
print("Activity:", random.choice(activities))

guess = int(input("Guess 1-10: "))
secret = random.randint(1, 10)

if guess == secret:
    print("Correct!")
else:
    print("Wrong! It was", secret)

print("Ceil:", math.ceil(4.7))
print("Floor:", math.floor(4.7))
print("Copy Sign:", math.copysign(5, -1))
print("Absolute:", math.fabs(-8))
print("GCD:", math.gcd(12, 18))
#!/usr/bin/python3
for number in range(1,101):
    if number % 3 == 0:
        print("Fizz", end=" ")
    elif number % 5 == 0:
        print("Buzz", end=" ")
    else:
        print(f"{number}", end=" ")

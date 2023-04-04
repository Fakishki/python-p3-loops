#!/usr/bin/env python3

def happy_new_year():
    minute = 10
    while minute > 0:
        print(f"{minute}")
        minute -= 1
        if minute == 0:
            print("Happy New Year!")

def square_integers(int_list):
    squared_list = []
    for int in int_list:
        squared_integer = int ** 2
        squared_list.append(squared_integer)
    return squared_list

def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

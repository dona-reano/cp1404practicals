"""
CP1404 - List exercises
"""

# 1. Write a program that prompts the user for 5 numbers and then
# stores each of these in a list called numbers.
numbers = []
for i in range(5):
    number = int(input("Number: "))
    numbers.append(number)

print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of the numbers is {sum(numbers) / len(numbers)}")

# 2. Ask the user for their username. If the username is in the list of
# authorised users, print "Access granted", otherwise print "Access denied".
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = input("What is your username? >> ")
if username in usernames:
    print("Access granted")
else:
    print("Access denied")

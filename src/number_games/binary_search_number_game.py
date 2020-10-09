# Write a number guessing game
# User thinks of a number 1-100
# Program makes a guess
# Tell it if the number is > or < than its guess
# Uses that info to modify its guess until it homes in

# This program has a pretty sharp learning rate as it uses
# user input in a range for random.randint()
import random
import time


user_number = int(input('Select a number from 1-100: '))
time.sleep(1)

print('Computer is selecting a number...')
time.sleep(1)

high = 100
low = 1

computer_number = low + (high - low) // 2

while True:
    if user_number == computer_number:
        print(f'Computer chooses: {computer_number}')
        time.sleep(0.5)
        print('Computer has selected your number!')
        break
    else:
        print(f'Computer chooses: {computer_number}')
        time.sleep(0.5)
        response = input(f'Is your number > or < than {computer_number}? ')
        if response == '<':
            high = computer_number - 1
        elif response == '>':
            low = computer_number + 1
        computer_number = low + (high - low) // 2

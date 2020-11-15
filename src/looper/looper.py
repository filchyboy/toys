# from random import randint  # use randint(a, b) to generate a random number between a and b

# number = 0 # store random number in here, each time through
# i = 0  # i should be incremented by one each iteration
# print(number)
# while number != 5:
#     rand_num = randint(1,10)
#     print(rand_num)
#     number += rand_num 
#     print(number)
#     i += 1
#     if number == 5:
#         break
#     else:
#         number == 0

from random import randint  # use randint(a, b) to generate a random number between a and b
 
number = 0 #store random number in here, each time through
i = 0  # i should be incremented by one each iteration
 
while number != 5: #keep looping while number is not 5
    i += 1
    number = randint(1, 10)
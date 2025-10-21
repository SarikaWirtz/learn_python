# Calculate prime number between 1 to 250.

# 1) number should be bigger than 1
# 2) Find the list of factors of each number
# 3) Taking each number one by one, we need to see 
# if the factors of the number are only 1 and the number itself, 
# then it is a prime number

# 4) If a number has factors other than 1 and itself, then it is not a prime number.

# for num in range(1, 250 + 1):
#     if num > 1:
#         for i in range(2, num):
#             if (num % i) == 0:
#                 break

#         else:
#             print(num)

import math

for num in range(2, 251):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            break
    else:
        print(num)


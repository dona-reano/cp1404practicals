"""
CP1404 - Random Numbers
"""
import random

# What did you see on line 1?
# 12, 10, 15, 8, 9
# What was the smallest number you could have seen, what was the largest?
# The smallest number 5, and largest 20.


# What did you see on line 2?
# 7, 5, 9, 3
# What was the smallest number you could have seen, what was the largest?
# The smallest number 3, and largest 9.
# Could line 2 have produced a 4?
# Line 2 couldn't have produced 4 because the range starts from 3 and increases in increments of 2.

# What did you see on line 3?
# 2.6010936154061337, 4.69734683324691, 4.165450577718838
# What was the smallest number you could have seen, what was the largest?
# The smallest number 2.5 and largest 5.5.

# Write code, not a comment, to produce a random number between 1 and 100 inclusive.
print(random.randint(1, 100))

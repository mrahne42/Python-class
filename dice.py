# FILE NAME - dice.py

# NAME: Mike Rahne
# DATE: 9/28/2025
# BRIEF DESCRIPTION: my_attempt_at_dice.py



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience

import random


########## ENTER YER CODE BELOW THIS LINE ##########

import random

die_roll = input('Enter a seed for the random number generation: ')
random.seed(die_roll)

die_one = random.randint(1,6)
die_two = random.randint(1,6)

print(f'Die roll one is {die_one}\nDie roll two is {die_two}')


########### END YER CODE ABOVE THIS LINE ###########



########################################
#          SAMPLE OUTPUT
########################################

'''

Enter a seed for the random number generation: 33
Die roll one is 5
Die roll two is 2

'''



'''

Enter a seed for the random number generation: 22
Die roll one is 2
Die roll two is 2

'''



'''

Enter a seed for the random number generation: -30
Die roll one is 5
Die roll two is 3

'''



########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is the purpose of "seeding" the random number generator?






'''

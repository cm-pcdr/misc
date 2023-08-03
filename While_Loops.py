
## While loops:

## Lets start with a simple count

## STEP THROUGH WITH BREAKPOINT ##

# count = 0
# while count < 10:
#     count += 1
#     print(count)

## Our count increments by 1 and then restarts the loop until our count hits 10

## now lets look at working with a string

# done = "no"
# print("Welcome to the endless loop. It will keep going until you type yes:")
# while done != "yes":
#     done = input("Would you like to stop?")
# print("Goodbye")

## Next lets start to sprinkle in random
## This program guesses random numbers between 1 and 20 until it guesses 
## the right number

# import random      ##Random was imported for the guesser
# import time        ##Time was imported to space out the guesses

# num = int(input("What number (Between 1 and 20) would you like the computer to try and guess?"))
# guess = 0
# while guess != num:
#     guess = random.choice(range(1,21))
#     print(f"I'm guessing {guess}")
#     time.sleep(.5)
# print(f"{guess} was correct!")

## By adding a list instead of a range we can refine this program
## Now it cannot guess the same number twice!!

# import random      
# import time        

# num = int(input("What number (Between 1 and 20) would you like the computer to try and guess?"))
# guess = 0
# guessRange = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# while guess != num:
#     guess = random.choice(guessRange)
#     print(f"I'm guessing {guess}")
#     guessRange.remove(guess)
#     time.sleep(.5)
# print(f"{guess} was correct!")

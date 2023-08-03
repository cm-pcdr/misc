## Now lets move on to For-Loops
## We use these to take a block of code and iterate, or repeat it.

# cars = ["Jeep", "Toyota", "Ford", "Ram"]
# for car in cars:
#     print(f"This car brand is {car}")

## What we did is establish a list and then used a for-loop to work 
## through and input each item in that list into a sentence. Once every item 
## was displayed, the loop was complete and it ended.

## We can even use a for-loop to do arithmetic

# multiplier = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for number in multiplier:
#     print(f"{number} multiplied by 2 equals {number * 2}")

## We can also use a range
# for num in range(1,10):
#     print(num)

## Notice how the print starts at one but ends at 9 so if we wanted to print
## numbers 1 through 10 we would need to change it to this:

# for num in range(1,11):
#     print(num)

## OR

# for num in range(1,10+1):
#     print(num)

## This is because the logic has the range run from 1 all the way up to 10, but
## stops just before 10.

## A more complex example from the hands on material:

# fruits = ["strawberry", "raspberry", "blueberry", "grape", "mango", "melon"]
# berryCount = 0
# for fr in fruits:
#     if fr.endswith("berry"):
#         berryCount += 1
# print("I've finished counting the fruits.")
# print(f"There were {berryCount} that ended with berry.")

## We can even make a list within a list

# fruits = [["Blueberry", "blue", 3.00], ["Strawberry", "red", 4.50], 
#           ["Blackberry", "purple", 5.00]]

# for name, color, price in fruits:
#     print(f"The {name} is the color {color} and costs ${price:.2f} per pound.")

## Let's add onto this. 

# fruitPounds = int(input("How many pounds of each fruit would you like to buy?"))
# for name, color, price in fruits:
#     totalPrice = fruitPounds * price 
#     print(f"{fruitPounds} of {name} costs ${totalPrice:.2f}")

## We prompted the user to input how many they would like to buy and then
## we calculated how much that would cost.
## Take note of the fact we used :.2f to ensure that there were two zeros
## after the decimal.
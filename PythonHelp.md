
# For those struggling with some of the concepts of python, here are some clarifications and tips:


As you go through the page, copy and paste the following code from...

``` python3
# ...Boxes like this...
```
...into your Visual Studio Python file and run the code so you can see what is happening as you work through the lesson. Feel free to skip this for the examples that state: 
**You don't need to copy and paste this**

## Functions and Variables

This is a **print()** function. We Know it's a function because of the parentheses at the end:

```python3
print() # You don't need to copy and paste this
```
This print() function is set to display Hello World to the user:
```python3
print("Hello World") 
```
This is an **input()** function. It will wait for the user to enter some information and press enter:
```python3
input() # You don't need to copy and paste this
```
Input will print to the screen the same as the print() function.
This is handy for prompting the user to enter data, like the following example, which is asking for a name.
```python3
input("Please enter your name: ") 
```

Unfortunately, it doesn't matter what the user enters, the code isn't storing their response. For that we need a **variable**.

**Variables** are used to store information. We set a variable's value by using the equal sign followed by some code.
Variables have what is called a **'typevalue'** or what kind of data can be stored in that variable.
Here are some examples of variables:
```python3
variable1 = "Steve" # This one has a typevalue of string which is text.
variable2 = 5       # This one has a typevalue of int which is short for integer.
variable3 = 5.1     # This one has a typevalue of float which is for a floating point decimal number.
```
We can name a variable almost anything with a couple exceptions:

**Unacceptable variables:**
```python3
1stVariable =  - We can't start with a number.
first variable =  - We can't use spaces.
print =  - We can't use function names as this will break the function.
```
**Acceptable variables:**
```python3
variable1st =  - We can put a number within or at the end of the variable's name.
first_variable =  - We can use an underscore to add a space to a variable.
print1 =  - We modified this one so it isn't the same as the print() function.
```

Now let's revisit the **input()** function example. We can use a variable to store what the user types in:
```python3
name = input("Please enter your name: ")
print(name) # We can view the value of a variable by adding it to a print() function like so.
```
# As you can see, it saves the name the user inputs and then prints it to the screen.

# Now lets look at how to display a variable inside of a print statement

print(f"Hello {name}, I hope you are having a good day!")

# By putting 'f' before the quotations in a print() function identifies the string as what is called a 'Formatted String'
# This means that when we put variables inside braces {}, we want the code to print the value stored in the variable.
# As you can see, when the code is run, it replaces {name} with the name the user entered previously.

# Lets look at a more complex example:

name2 = input("Please enter your name: ") # Notice that we used a different variable because 'name' was already in use previously
car = input("What kind of car do you drive?: ") # New variable to save what kind of car the user drives
print(f"Good to meet you {name2}. {car} is a good type of car!") # Formatted string that is diplaying both the user's name and car

# Lets look at different typevalues for inputs:

int() # This can be used to convert an input to an integer
float() # This can be used to convert a number to a float

stringVar = input("Please enter a whole number: ") # This will save the number as a string
integerVar = int(input("Please enter another whole number: ")) # This will save the number as an integer
floatVar = float(input("Please enter one more whole number: ")) # This will save the number as a float

# Some prints so we can see what is going on:

print(f"The first number you entered was {stringVar}") 
print(f"The second number you entered was {integerVar}")
print(f"The third number you entered was {floatVar}")

# Notice how the third number has a decimal in it even though you entered a whole number. 
# This is because when float() is used to convert the user's input into a float, it add the decimal.

# Lets take a deeper look at the typevalues by trying to do some math with our numbers

intSum = integerVar + integerVar 

print(integerVar) # Notice how the value of this variable didn't change despite adding it with itself!
print(intSum) # This is our sum of the two numbers

# We created a new variable 'intSum'.
# Using the '+' operator we were able to add the same variable together with itself to create our sum and then store it in 'intSum'
# We will discuss operators in more depth later. For now we are just using it to demonstrate typevalues.

# Lets add out float and our integer together
x = integerVar + floatVar
print(x)

# Notice how the value of our two numbers added has a decimal. 
# Since we added a float to an integer, it automatically converted the typevalue of 'x' to float.

# Finally, we are going to add our stringVar and integerVar

# y = integerVar + stringVar
# print(y)

# Uh oh, we broke it. Why?
# Well, even though we put a whole number in when requested for our stringVar, it is still being recognized as a string typevalue
# In other words, we are trying to add a string "1" with an integer 1 which isn't possible.
# This is the same as trying to add the word "Cheeseburger" with 1. It just doesn't make sense. 
# To do arithmetic, we need to ensure we are working with integers or floats.









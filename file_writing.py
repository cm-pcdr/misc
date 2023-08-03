# ## To use the file structure in python we first have to open a file to create it

# f = open("first_file.txt", "w")
# f.close()

# ## What we just did s create a file, but it has no data in it.
# ## Why must we close a file when we are done?
#     ## In general, the system should close the file automatically,
#     ## However if it doesn't then you risk of losing the data.
#     ## This is because when you send the "write" command, the operating
#     ## system doesnt write at that moment, it may pause and wait before doing so
#     ## which can lead to unpredicatable behavior. When we send the "close"
#     ## command, the OS writes to the file as well as saves the file and closes it.

# ## Lets create a new file and add data to it

# f = open("a_file.txt", "w")
# f.write("This is the data we are putting in a file.")
# f.close()
# print("File created")

# ## We use the "w" to denote that we are writing to a file.
# ## How do you think we denote only reading a file without editing its data?
#     ## We use "r" to denote read only.

# f = open("a_file.txt", "r")
# contents = f.read()
# print(contents)
# f.close

# ## What we did is told the system to read the file and store its contents 
# ## inside of the string variable "contents".

# ## What happens if we try to write to a file while in read only mode?
#     ## Let's see:

# f = open("a_file.txt", "r")
# f.write("I am going to attempt write to this file.")
# f.close()

# ## Notice how we get the error "not writable"

# ## Sometimes we need to add data to a file without overwriting the data currently
# ## stored in the file. To do this we use "a" for "append"

# f = open("a_file.txt", "a")
# f.write("\nWe added this to the file!")
# f.close()

# ## Note that I used \n to tell the system to add my appended data onto a new line.

# ## Of course we need to then switch back to "read" mode to view the contents.

# f = open("a_file.txt", "r")
# stuff = f.read()
# print(stuff)

# ## Finaly, if you would like to write to a file, but are unsure if a file of that
# ## name exists, you can use "x" instead of "w".

# f = open("a_file.txt", "x")
# f.write("This file exists")
# f.close()


## Here is a quick example of how to ask a user for input and then put that input into a file:

# stuff = input("What would you like to put in the file?")
# f = open("input_file", "w")
# f.write(f"This is what you wanted to input into the file: {stuff}")
# f.close()

# f = open("input_file", "r")
# contents = f.read()
# print(contents)
# f.close()


## Average practice:

# a = 98
# b = 87
# c = 87
# total = a + b + c
# average = total/3
# print(f"The average of these numbers is {average:.1f}%")
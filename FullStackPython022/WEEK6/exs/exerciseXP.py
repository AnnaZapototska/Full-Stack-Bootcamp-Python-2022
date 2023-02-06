# ex 1
# Print the following output in one line of code:
strPrint = "Hello world " + "\n"
print(strPrint * 4)

# ex2
# Write code that calculates the result of: (99^3)*8 (meaning 99 to the power of 3, times 8).
calculate = (99 ** 3) * 8
print(calculate)
# ex 3
# Predict the output of the following code snippets
# a = 5 < 3
# false
# a = 3 == 3
# true
# a = 3 == '3'
# false
# a = "3" > 3
# error
# a = "Hello" == "hello"
# false

#ex 4
# Create a variable called computer_brand which value is the brand name of your computer.
# Using the computer_brand variable print a sentence that states the following: "I have a <computer_brand> computer".

computer_brand = 'Acer Nitro 5'
print("I have a " + computer_brand + " computer")


# ex 5
# Create a variable called name, and set it’s value to your name.
# Create a variable called age, and set it’s value to your age.
# Create a variable called shoe_size, and set it’s value to your shoe size.
# Create a variable called info and set it’s value to an interesting sentence about yourself. The sentence must contain all the variables created in parts 1, 2 and 3.
# Have your code print the info message.
# Run your code

name = 'Anna'
age = 24
shoe_size = 38
info = f"My name is {name}, I am {age} years old, and my shoe size is {shoe_size}."
print(info)

# ex 6
# Create two variables, a and b.
# Each variable value should be a number.
# If a is bigger then b, have your code print Hello World.


a = 25
b = 2
if a > b:
    print('Hello world')

# ex 7
# Write code that asks the user for a number and determines whether this number is odd or even.
number = int(input('Please enter your number'))
if (number % 2) == 0:
    print(f'The number {number} is even')
else:
    print(f'The number {number} is odd')


# ex 8
# Write code that asks the user for their name and determines whether or not you have the same name, print out a funny message based on the outcome.

name_user = input('Please write your name: ')
if name_user == name:
    print("We have the same name. Do you want a joke? Which one of you is Bill? One of them replied, I'm Bill! The bartender then asked, What's your name? The other Bill replied, Bill.")
else:
    print("You will never hear a cool joke((")

# ex 9

# Write code that will ask the user for their height in inches.
# If they are over 145cm print a message that states they are tall enough to ride.
# If they are not tall enough print a message that says they need to grow some more to ride.

inch_value = int(input('Enter the value in inch: '))
cm_value = 2.54 * inch_value
if cm_value > 145:
    print("You are tall enough to ride")
else:
    print("You are need to grow some more to ride")

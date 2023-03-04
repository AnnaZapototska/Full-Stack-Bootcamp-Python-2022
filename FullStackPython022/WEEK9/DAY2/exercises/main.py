# Exercise 1 : Built-In Functions
# Instructions
# Python has many built-in functions.
# If you feel that you don’t know how to properly implement them take a look at the python documentation online.
# Write a program which prints the results of the following python built-in functions: abs(), int(), input().
# Using the __doc__ dunder method create your own documentation which explains the execution of your code. Take a look at the doc method on google for help.

"""This program demonstrates the usage of built-in functions in Python - abs(), int(), and input()."""

user_input = input("Enter a number: ")
number = int(user_input)
absolute_value = abs(number)

print("The absolute value of", number, "is", absolute_value)

# version 2
def new():
    """This program demonstrates the usage of built-in functions in Python - abs(), int(), and input()."""
    return abs(int(input("Enter your number: ")))


print(new.__doc__)

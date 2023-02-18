# ex1
# Instructions
# Write a function called display_message() that prints one sentence telling everyone what you are learning in this course.
# Call the function, and make sure the message displays correctly.

def display_message():
    print("In the course we are learning: HTML, CSS, JS and Python.")


display_message()


# ex 2
# Instructions
# Write a function called favorite_book() that accepts one parameter called title.
# The function should print a message, such as "One of my favorite books is <title>".
# For example: “One of my favorite books is Alice in Wonderland”
# Call the function, make sure to include a book title as an argument when calling the function.

def favorite_book(title):
    print(f"One of my favorite books is {title}")


favorite_book("Black")


# ex 3
# Instructions
# Write a function called describe_city() that accepts the name of a city and its country as parameters.
# The function should print a simple sentence, such as "<city> is in <country>".
# For example “Reykjavik is in Iceland”
# Give the country parameter a default value.
# Call your function.

def describe_city(city, country):
    print(f"{city} is in {country}")


describe_city("Kherson", "Ukraine")
#
# def describe_city(city, country="unknown"):
#     print(f"{city} is in {country}")
# describe_city("Kherson")

# ex 4
# Instructions
# Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100.
# Compare the two numbers, if it’s the same number, display a success message, otherwise show a fail message and display both numbers.


import random


def compare_numbers(num):
    rand_num = random.randint(1, 100)
    if num == rand_num:
        print("Success! The numbers are the same.")
    else:
        print(f"Fail! The numbers are different. Your number was {num} and the random number was {rand_num}.")


compare_numbers(4)


# ex 5
# Instructions
# Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
# The function should print a sentence summarizing the size of the shirt and the message printed on it, such as "The size of the shirt is <size> and the text is <text>"
# Call the function make_shirt().
# Modify the make_shirt() function so that shirts are large by default with a message that reads “I love Python” by default.
# Make a large shirt with the default message
# Make medium shirt with the default message
# Make a shirt of any size with a different message.
# Bonus: Call the function make_shirt() using keyword arguments.

def make_shirt(size="large", message="I love Python"):
    print(f"The size of the shirt is {size} and the text is '{message}'.")


make_shirt()
make_shirt(size="medium")
make_shirt(size="small", message="Python is fun!")

# ex 6
# Instructions
# Using this list of magician’s names. magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
# Pass the list to a function called show_magicians(), which prints the name of each magician in the list.
# Write a function called make_great() that modifies the list of magicians by adding the phrase "the Great" to each magician’s name.
# Call the function make_great().
# Call the function show_magicians() to see that the list has actually been modified.
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']


def show_magicians(magicians):
    for magician in magicians:
        print(magician)


def make_great(magicians):
    for i in range(len(magicians)):
        magicians[i] = "the Great " + magicians[i]


make_great(magician_names)
show_magicians(magician_names)

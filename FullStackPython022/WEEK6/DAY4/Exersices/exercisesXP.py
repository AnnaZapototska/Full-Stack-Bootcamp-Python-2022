#  ex 1
# Instructions
# Create a set called my_fav_numbers with all your favorites numbers.
# Add two new numbers to the set.
# Remove the last number.
# Create a set called friend_fav_numbers with your friend’s favorites numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.

my_fav_numbers = {11, 25, 9, 8}
my_fav_numbers.add(0)
my_fav_numbers.add(14)

my_fav_numbers = list(my_fav_numbers)
my_fav_numbers.pop()
my_fav_numbers = set(my_fav_numbers)

friend_fav_numbers = {2, 8, 41, 5}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
# my_fav_numbers.update(friend_fav_numbers)
print(our_fav_numbers)

# ex2
# Given a tuple which value is integers, is it possible to add more integers to the tuple?
# Nope, you need create a new tuple with a new integers

tuple_one = (1, 2, 3, 4)
tuple_two = tuple_one + (5, 6, 7)
print(tuple_two)

# ex 3
# Using this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];
# Remove “Banana” from the list.
# Remove “Blueberries” from the list.
# Add “Kiwi” to the end of the list.
# Add “Apples” to the beginning of the list.
# Count how many apples are in the basket.
# Empty the basket.
# Print(basket)
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0, "Apples")
count = basket.count("Apples")
basket.clear()
print(basket)


# EX 4
# Instructions
# Recap – What is a float? What is the difference between an integer and a float?
# Can you think of another way to generate a sequence of floats?
# Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).

# Float () - converts the specified value into a floating point number.
# Integer is an integer with no remainder

#  solution 1
# start = 1.5
# end = 5
# step = 0.5
# sequence = []
# while start <= end:
#     sequence.append(start)
#     start += step
# print(sequence)

# solution 2

start = 1
end = 5
step = 0.5
sequence = []
counter = 0
while start <= end:
    if counter % 2 == 0:
        sequence.append(int(start))
    else:
        sequence.append(start)
    start += step
    counter += 1
sequence.pop(0)
print(sequence)



# ex 5
# Use a for loop to print all numbers from 1 to 20, inclusive.
# Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.
# solution 1
for numbers in range(1, 21):
    if numbers % 2 == 0:
        print(numbers)

# solution 2
numbers_v2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for number in numbers_v2:
    if number % 2 == 0:
        print(number)


# ex6
# Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.

my_name = "Anna"
while True:
    ask_name = input("Please enter your name: ")
    if my_name == ask_name:
        print("Our name is ", ask_name)
        break


# ex 7
# Instructions
# Ask the user to input their favorite fruit(s) (one or several fruits).
# Hint : Use the built in input method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
# Store the favorite fruit(s) in a list (convert the string of words into a list of words).
# Now that we have a list of fruits, ask the user to input a name of any fruit.
# If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.
# If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.

fruits = input("Please enter a list your favorite fruits. Separate the fruits with a single space: ")
fruits_list = fruits.split()
fruits_name = input("Please enter one fruit: ")
if fruits_name in fruits_list:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy")


# ex 8
# Instructions
# Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
# As they enter each topping, print a message saying you’ll add that topping to their pizza.
# Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).

# solution 1
price = 10
while True:
    pizza_toppings = input("Please enter a series of pizza toppings: ")
    if pizza_toppings != "quit":
        price += 2.5
        print("Adding " + pizza_toppings + " to your pizza.")
    else:
        break
print("Your pizza has the following toppings: " + str(pizza_toppings))
print("The total price of your pizza is $" + str(price))

# solution 2

# toppings = []
# price = 10
# topping = input("Enter a topping for your pizza (or 'quit' to stop): ")
# while topping.lower() != 'quit':
#     toppings.append(topping)
#     price += 2.5
#     print("Adding " + topping + " to your pizza.")
#     topping = input("Enter a topping for your pizza (or 'quit' to stop): ")
# print("Your pizza has the following toppings:")
# for topping in toppings:
#     print("- " + topping)
# print("The total price of your pizza is $" + str(price))


# ex 9
# Instructions
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.
# Ask a family the age of each person who wants a ticket.
# Store the total cost of all the family’s tickets and print it out.

# A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
# Given a list of names, write a program that asks teenager for their age, if they are not permitted to watch the movie, remove them from the list.
# At the end, print the final list.


asked_age = "How old are you?"
asked_age += "\nEnter 'quit' when you are finished. "
price_ticket = 0

while True:
    age = input(asked_age)
    if age == 'quit':
        break
    age = int(age)
    if age < 3:
        price_ticket = 0
    elif 3 <= age < 12:
        price_ticket += 10
    else:
        price_ticket += 15
print(f"Your total is ${price_ticket}")

list_teenagers = ["Jack", "Mary", "Max", "Alex", "Lera"]
list_restricted = []
for name in list_teenagers:
    ask_age = int(input(f"Enter your age, please, {name}: "))
    if 16 <= ask_age < 21:
        print(f"You can watch the film, {name}")
        list_restricted.append(name)
    else:
        print(f"You cannot watch the film, {name}")
print(list_restricted)


# ex 10
# Instructions
# sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
# Use the above list called sandwich_orders.
# Make an empty list called finished_sandwiches.
# As each sandwich is made, move it to the list of finished sandwiches.
# After all the sandwiches have been made, print a message listing each sandwich that was made , such as I made your tuna sandwich.

sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")
print(sandwich_orders)

finished_sandwiches = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made  {current_sandwich}.")
    finished_sandwiches.append(current_sandwich)

print("All sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")


# ex 11
# Instructions
# Using the list sandwich_orders from the previous exercise, make sure the sandwich ‘pastrami’ appears in the list at least three times.
# Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of ‘pastrami’ from sandwich_orders.
# Make sure no pastrami sandwiches end up in finished_sandwiches.

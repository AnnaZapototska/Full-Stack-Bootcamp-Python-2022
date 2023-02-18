# ex 1
# Instructions
# Create a function called get_random_temp().
# This function should return an integer between -10 and 40 degrees (Celsius), selected at random.
# Test your function to make sure it generates expected results.
# Create a function called main().
# Inside this function, call get_random_temp() to get a temperature, and store its value in a variable.
# Inform the user of the temperature in a friendly message, eg. “The temperature right now is 32 degrees Celsius.”
# Let’s add more functionality to the main() function. Write some friendly advice relating to the temperature:
# below zero (eg. “Brrr, that’s freezing! Wear some extra layers today”)
# between zero and 16 (eg. “Quite chilly! Don’t forget your coat”)
# between 16 and 23
# between 24 and 32
# between 32 and 40
# Change the get_random_temp() function:
# Add a parameter to the function, named ‘season’.
# Inside the function, instead of simply generating a random number between -10 and 40, set lower and upper limits based on the season, eg. if season is ‘winter’, temperatures should only fall between -10 and 16.
# Now that we’ve changed get_random_temp(), let’s change the main() function:
# Before calling get_random_temp(), we will need to decide on a season, so that we can call the function correctly. Ask the user to type in a season - ‘summer’, ‘autumn’ (you can use ‘fall’ if you prefer), ‘winter’, or ‘spring’.
# Use the season as an argument when calling get_random_temp().
# Bonus: Give the temperature as a floating-point number instead of an integer.
# Bonus: Instead of asking for the season, ask the user for the number of the month (1 = January, 12 = December). Determine the season according to the month.

import random


def get_random_temp(season):
    if season == 'winter':
        return random.uniform(-10, 16)
    elif season == 'spring':
        return random.uniform(0, 23)
    elif season == 'summer':
        return random.uniform(24, 32)
    elif season == 'autumn' or season == 'fall':
        return random.uniform(16, 23)


def main():
    season = input("Please enter a season (winter, spring, summer, or fall): ")
    temperature = get_random_temp(season)
    print("The temperature right now is {:.1f} degrees Celsius.".format(temperature))
    if temperature < 0:
        print("Brrr, that's freezing! Wear some extra layers today.")
    elif 0 <= temperature < 16:
        print("Quite chilly! Don't forget your coat.")
    elif 16 <= temperature < 24:
        print("Nice weather! Enjoy your day.")
    elif 24 <= temperature < 32:
        print("It's warm outside! Stay hydrated.")
    elif temperature >= 32:
        print("It's hot! Stay cool and drink plenty of water.")


month = int(input("Please enter the number of the month (1-12): "))
if month in [1, 2, 12]:
    season = 'winter'
elif month in [3, 4, 5]:
    season = 'spring'
elif month in [6, 7, 8]:
    season = 'summer'
elif month in [9, 10, 11]:
    season = 'fall'
main()

# ex 2
# Instructions
# The point of the exercise is to check if a person can retire depending on their age and their gender.
# Note : Retirement age in Israel is 67 for men, and 62 for women (born after April, 1947).
#
# Create a function get_age(year, month, day)
# Hard-code the current year and month in your code (there are better ways of doing this, but for now it will be enough.)
# After calculating the age of a person, the function should return the age (the age is an integer).
# Create a function can_retire(gender, date_of_birth).
# It should call the get_age function (with what arguments?) in order to receive an age.
# Now it has all the information it needs in order to determine if the person with the given gender and date of birth is able to retire or not.
# Calculate. You may need to do a little more hard-coding here.
# Return True if the person can retire, and False if he/she can’t.
# Some Hints
#
# Ask for the user’s gender as “m” or “f”.
# Ask for the user’s date of birth in the form of “yyyy/mm/dd”, eg. “1993/09/21”.
# Call can_retire to get a definite value for whether the person can or can’t retire.
# Display a message informing the user whether they can retire or not.
# As always, test your code to ensure it works.


# i dont want to hardcode current year and month, thats why I import datetime
import datetime


def get_age(year, month, day):
    current_date = datetime.now()
    age = current_date.year - year - ((current_date.month, current_date.day) < (month, day))
    return age


def can_retire(gender, date_of_birth):
    year, month, day = map(int, date_of_birth.split('/'))
    age = get_age(year, month, day)
    if gender == 'm':
        retirement_age = 67
    elif gender == 'f':
        retirement_age = 62
    else:
        # used raise to show error and stop program
        raise ValueError('Invalid gender')
    return age >= retirement_age


gender = input("Enter your gender (m/f): ")
date_of_birth = input("Enter your date of birth (yyyy/mm/dd): ")
if can_retire(gender, date_of_birth):
    print("You can retire!")
else:
    print("Sorry, you can't retire yet.")

# ex 3
# Instructions
# Write a function that accepts one parameter (an int: X) and returns the value of X+XX+XXX+XXXX.
# Example:
# If X=3, the output when calling our function should be 3702 (3 + 33 + 333 + 3333)

number = int(input("Enter number: "))


def compute_sum(x):
    str_x = str(x)
    total = 0
    for i in range(1, 5):
        num_str = str_x * i
        num = int(num_str)
        total += num
    return total


result = compute_sum(number)
print(result)

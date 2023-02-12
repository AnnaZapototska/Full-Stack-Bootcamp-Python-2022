# Instructions
# Using the input function, ask the user for a string. The string must be 10 characters long.
# If it’s less than 10 characters, print a message which states “string not long enough”.
# If it’s more than 10 characters, print a message which states “string too long”.
#
# Then, print the first and last characters of the given text.
#
# Using a for loop, construct the string character by character: Print the first character, then the second, then the third, until the full string is printed. For example:
# 4. Bonus: Swap some characters around then print the newly jumbled string (hint: look into the shuffle method).

import random

text = str(input("Please enter phrase: "))

if len(text) > 10:
    print('string too long')
else:
    print('string not long enough')

print(text[0])
print(text[-1])

for x in text:
    print(x)

text_list = list(text)
random.shuffle(text_list)
print(text_list)


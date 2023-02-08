# Challenge 1
# Ask the user for a number and a length.
# Create a program that prints a list of multiples of the number until the list length reaches length.

number = int(input("Enter a number: "))
length = int(input("Enter the length of the list: "))

multiples = []
for i in range(1, length+1):
    multiple = number * i
    multiples.append(multiple)

print("List of multiples of", number, ":", multiples)


# Challenge 2
# Write a program that asks a string to the user, and display a new string with any duplicate consecutive letters removed.
# Final strings won’t include words with double letters (e.g. “passing”, “lottery”).

string = input("Enter your string: ")
include_char = ""
for char in string:
    if char not in include_char:
        include_char = include_char + char
print(include_char)

# solution 2
string = input("Enter your string: ")
print("".join(dict.fromkeys(string)))


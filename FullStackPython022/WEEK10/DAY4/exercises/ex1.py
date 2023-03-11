# ex1
# Download this word list
# Save it in your development directory.
# Create a function called get_words_from_file. This function should read the file’s content and return the words as a collection. What is the correct data type to store the words?
# Create another function called get_random_sentence which takes a single parameter called length. The length parameter will be used to determine how many words the sentence should have. The function should:
# use the words list to get your random words.
# the amount of words should be the value of the length parameter.
# Take the random words and create a sentence (using a python method), the sentence should be lower case.
# Create a function called main which will:
# Print a message explaining what the program does.
# Ask the user how long they want the sentence to be. Acceptable values are: an integer between 2 and 20. Validate your data and test your validation!
# If the user inputs incorrect data, print an error message and end the program.
# If the user inputs correct data, run your code.

def get_words_from_file(file_name):
    with open(file_name, 'r') as file:
        words = file.read().split()
    return words


import random


def get_random_sentence(words, length):
    sentence = " ".join(random.sample(words, length))
    return sentence.lower()


def main():
    print("Welcome to the Random Sentence Generator!")
    words = get_words_from_file('sowpods.txt')

    while True:
        try:
            length = int(input("How long should the sentence be (2-20)? "))
            if length < 2 or length > 20:
                print("Error: Length must be between 2 and 20")
            else:
                sentence = get_random_sentence(words, length)
                print("Your random sentence is:\n", sentence)
                break
        except ValueError:
            print("Error: Length must be an integer")


main()

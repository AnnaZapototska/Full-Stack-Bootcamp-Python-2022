# # ex1
# # Ask a user for a word
# # Write a program that creates a dictionary. This dictionary stores the indexes of each letter in a list.
# # Make sure the letters are the keys.
# # Make sure the letters are strings.
# # Make sure the indexes are stored in a list and those lists are values.
#
# # solution 1
# word = input("Please enter a word: ")
# result = {}
# letters = []
# for letter in word:
#     if letter not in letters:
#         letters.append(letter)
#
# for letter in letters:
#     result[letter] = []
#     for i, letter2 in enumerate(word):
#         if letter == letter2:
#             result[letter].append(i)
#
# print(result)
#
#
# # solution 2
# word = input("Please enter a word: ")
# result = {}
# for index, char in enumerate(word):
#     if char in result:
#         result[char].append(index)
#     else:
#         result[char] = [index]
#
# print(result)

# ex 2
# Create a program that prints a list of the items you can afford in the store with the money you have in your wallet.
# Sort the list in alphabetical order.
# Return “Nothing” if you can’t afford anything from the store.
wallet = int(input("How many money you have in your wallet: "))
items_purchase = {
  "Water": "$1",
  "Bread": "$3",
  "TV": "$1000",
  "Fertilizer": "$20"
}

afford_list = []
for index, value in items_purchase.items():
    int_amount = int(value.replace("$", ""))
    if int_amount <= wallet:
        afford_list.append(index)
        afford_list.sort()
        if len(afford_list) > 0:
            print(f"You can afford: {afford_list}")
        else:
            print("Nothing")

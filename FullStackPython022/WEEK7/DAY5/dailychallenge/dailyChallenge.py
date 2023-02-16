# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Use List Comprehension

# if user enter words without comma like: world text hello more one | hello, more, one, text, world
# lst = [item for item in input("Please enter your words: ").split()]
# sort = ", ".join(sorted(lst))
# print(sort)

# if user enter words without comma like: without,hello,bag,world | bag, hello, without, world
lst = input("Please enter your words: ").split(',')
sorted_lst = sorted([item.strip() for item in lst])
sort = ", ".join(sorted_lst)
print(sort)

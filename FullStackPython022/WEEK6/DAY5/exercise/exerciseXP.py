# ex 1
# Convert the two following lists, into dictionaries.
# Hint: Use the zip method

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
x = zip(keys, values)
print(tuple(x))


# ex2
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.
# How much does each family member have to pay ?
# Print out the family’s total cost for the movies.
# Bonus: Ask the user to input the names and ages instead of using the provided family variable (Hint: ask the user for names and ages and add them into a family dictionary that is initially empty).

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

total_cost = 0

for member, age in family.items():
    if age < 3:
        cost = 0
    elif age >= 3 and age <= 12:
        cost = 10
    else:
        cost = 15

    total_cost += cost
    print(f"{member} has to pay ${cost}")

print(f"Total cost for the family is ${total_cost}")

bonus
family = {}

while True:
    name = input("Enter family member's name (Enter 'done' when finished): ")

    if name.lower() == 'done':
        break

    age = int(input("Enter age: "))

    family[name] = age

total_cost = 0

for member, age in family.items():
    if age < 3:
        cost = 0
    elif age >= 3 and age <= 12:
        cost = 10
    else:
        cost = 15

    total_cost += cost
    print(f"{member} has to pay ${cost}")

print(f"Total cost for the family is ${total_cost}")

# ex3
# Here is some information about a brand.
# 2. Create a dictionary called brand which value is the information from part one (turn the info into keys and values).
# 3. Change the number of stores to 2.
# 4. Print a sentence that explains who Zaras clients are.
# 5. Add a key called country_creation with a value of Spain.
# 6. Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.
# 7. Delete the information about the date of creation.
# 8. Print the last international competitor.
# 9. Print the major clothes colors in the US.
# 10. Print the amount of key value pairs (ie. length of the dictionary).
# 11. Print the keys of the dictionary.
# 12. Create another dictionary called more_on_zara with the following details:
#  Use a method to add the information from the dictionary more_on_zara to the dictionary brand.
# 14. Print the value of the key number_stores. What just happened ?


brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": "pink, green"
    }
}
# 3. Change the number of stores to 2.
number_stores = brand['number_stores'] = 2
# 5. Add a key called country_creation with a value of Spain.
brand["country_creation"] = "Spain"
# 4. Print a sentence that explains who Zaras clients are.
print(f"Zara caters to a wide range of customers: " + brand["type_of_clothes"][0], brand["type_of_clothes"][1], brand["type_of_clothes"][2], brand["type_of_clothes"][3])
# 6. Check if the key international_competitors is in the dictionary.
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")

# 7. Delete the information about the date of creation.
if "creation_date" in brand:
    del brand["creation_date"]

# 8. Print the last international competitor
print(brand["international_competitors"][-1])
# 9. Print the major clothes colors in the US.
print(brand["major_color"]["US"])
# 10. Print the amount of key value pairs (ie. length of the dictionary).
print(len(brand))
# 11. Print the keys of the dictionary.
print(list(brand.keys()))
# 12. Create another dictionary called more_on_zara with the following details:
more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10000
}
#  Use a method to add the information from the dictionary more_on_zara to the dictionary brand.
brand.update(more_on_zara)
# 14. Print the value of the key number_stores. What just happened ?
print(brand["number_stores"])

print(brand)



# ex4
# Use a for loop to recreate the 1st result. Tip : don’t hardcode the numbers.
# Use a for loop to recreate the 2nd result. Tip : don’t hardcode the numbers.
# Use a method to recreate the 3rd result. Hint: The 3rd result is sorted alphabetically.
# Only recreate the 1st result for:
# The characters, which names contain the letter “i”.
# The characters, which names start with the letter “m” or “p”.

users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
disney_users_A = {}
for index, char in enumerate(users):
    if char in disney_users_A:
        disney_users_A[char].append(index)
    else:
        disney_users_A[char] = [index]

print(disney_users_A)
for char, indices in disney_users_A.items():
    print(f"{char}: {', '.join(map(str, indices))}")


disney_users_B = dict(enumerate(users))
print(disney_users_B)

users.sort()
disney_users_C = {}
for i, item in enumerate(users):
    disney_users_C[item] = i

print(disney_users_C)

disney_users_C = dict(sorted(disney_users_A.items()))
print(disney_users_C)

disney_users_D = {}
i = 0
for item in users:
    if item[0] == 'M' or item[0] == 'P' or 'i' in item:
        disney_users_D[item] = i
        i += 1
    else:
        continue

print(disney_users_D)
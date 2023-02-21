# ex 1
# Instantiate three Cat objects using the code provided above.
# Outside of the class, create a function that finds the oldest cat and returns the cat.
# Print the following string: “The oldest cat is <cat_name>, and is <cat_age> years old.”. Use the function previously created.

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age


cat1 = Cat("Dasha", 13)
cat2 = Cat("Lucifer", 1)
cat3 = Cat("Matilda", 3)


def serch_oldest_cat(cats):
    oldest_cat = None
    for cat in cats:
        if oldest_cat is None or cat.age > oldest_cat.age:
            oldest_cat = cat
    return oldest_cat


cats = [cat1, cat2, cat3]

oldest_cat = serch_oldest_cat(cats)

# print the result
print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")

# ex 2
# Create a class called Dog.
# In this class, create an __init__ method that takes two parameters : name and height. This function instantiates two attributes, which values are the parameters.
# Create a method called bark that prints the following string “<dog_name> goes woof!”.
# Create a method called jump that prints the following string “<dog_name> jumps <x> cm high!”. x is the height*2.
# Outside of the class, create an object called davids_dog. His dog’s name is “Rex” and his height is 50cm.
# Print the details of his dog (ie. name and height) and call the methods bark and jump.
# Create an object called sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.
# Print the details of her dog (ie. name and height) and call the methods bark and jump.
# Create an if statement outside of the class to check which dog is bigger. Print the name of the bigger dog.

class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        print(f"{self.name} jumps {self.height * 2} cm height")


davids_dog = Dog("Rex", 50)

print(f"David's dog is named {davids_dog.name} and is {davids_dog.height} cm tall.")
davids_dog.bark()
davids_dog.jump()

sarahs_dog = Dog("Teacup", 20)

print(f"Sarahs's dog is named {sarahs_dog.name} and is {sarahs_dog.height} cm tall.")
sarahs_dog.bark()
sarahs_dog.jump()


def find_biggest_dog():
    if davids_dog.height > sarahs_dog.height:
        print("Rex")
    else:
        print("Teacup")


find_biggest_dog()

# ex 3
# Instructions
# Define a class called Song, it will show the lyrics of a song.
# Its __init__() method should have two arguments: self and lyrics (a list).
# Inside your class create a method called sing_me_a_song that prints each element of lyrics on its own line.
# Create an object, for example:
# stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
# Then, call the sing_me_a_song method. The output should be:
# There’s a lady who's sure
# all that glitters is gold
# and she’s buying a stairway to heaven

from typing import List


class Song:
    def __init__(self, lyrics: List[str]):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


stairway = Song(["There’s a lady who’s sure",
                 "all that glitters is gold",
                 "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()

# ex 4
# Create a class called Zoo.
# In this class create a method __init__ that takes one parameter: zoo_name.
# It instantiates two attributes: animals (an empty list) and name (name of the zoo).
# Create a method called add_animal that takes one parameter new_animal. This method adds the new_animal to the animals list as long as it isn’t already in the list.
# Create a method called get_animals that prints all the animals of the zoo.
# Create a method called sell_animal that takes one parameter animal_sold. This method removes the animal from the list and of course the animal needs to exist in the list.
# Create a method called sort_animals that sorts the animals alphabetically and groups them together based on their first letter.
# Example:
# {
#     1: "Ape",
#     2: ["Baboon", "Bear"],
#     3: ['Cat', 'Cougar'],
#     4: ['Eel', 'Emu']
# }
# Create a method called get_groups that prints the animal/animals inside each group.
# Create an object called ramat_gan_safari and call all the methods.
# Tip: The zookeeper is the one who will use this class.
# Example
# Which animal should we add to the zoo --> Giraffe
# x.add_animal(Giraffe)

class Zoo:
    def __init__(self, zoo_name: str):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, new_animal: str):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        print(f"All animals in the zoo {self.name}:")
        for animal in self.animals:
            print(animal)

    def sell_animal(self, animal_sold: str):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        sorted_animals = {}
        for animal in self.animals:
            first_letter = animal[0].upper()
            if first_letter not in sorted_animals:
                sorted_animals[first_letter] = []
            sorted_animals[first_letter].append(animal)

        sorted_animals = dict(sorted(sorted_animals.items()))
        for key in sorted_animals:
            sorted_animals[key] = sorted(sorted_animals[key])

        return sorted_animals

    def get_groups(self):
        sorted_animals = self.sort_animals()
        for key, value in sorted_animals.items():
            print(f"{key}: {', '.join(value)}")


best_zoo = Zoo("The best Zoo")
best_zoo.add_animal("Ape")
best_zoo.add_animal("Cat")
best_zoo.add_animal("Emu")
best_zoo.add_animal("Giraffe")
best_zoo.add_animal("Lion")
best_zoo.add_animal("Bear")
best_zoo.add_animal("Tiger")
best_zoo.add_animal("Cougar")
best_zoo.get_animals()
best_zoo.sell_animal("Bear")
sorted_animals = best_zoo.sort_animals()
print(sorted_animals)
best_zoo.get_groups()

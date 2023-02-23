# Create the code that is needed to receive the result provided above. Below are a few questions to assist you with your code:
# Create a class called Farm. How should it be implemented?
# Does the Farm class need an __init__ method? If so, what parameters should it take?
# How many methods does the Farm class need?
# Do you notice anything interesting about the way we are calling the add_animal method? What parameters should this function have? How many…?
# Test your code and make sure you get the same results as the example above.
# Bonus: nicely line the text in columns as seen in the example above. Use string formatting.

# Expand The Farm
# Add a method called get_animal_types to the Farm class. This method should return a sorted list of all the animal types (names) in the farm. With the example above, the list should be: ['cow', 'goat', 'sheep'].
#
# Add another method to the Farm class called get_short_info. This method should return the following string: “McDonald’s farm has cows, goats and sheep.”. The method should call the get_animal_types function to get a list of the animals.


class Farm:
    def __init__(self, farm_name):
        self.farm_name = farm_name
        self.animals = {}

    def add_animal(self, animal_type, count=1): # you can make this function in just a single line: self.animals[animal_type] = self.animals.get(animal_type, 0) + count
        animal_type = animal_type.lower()
        if animal_type in self.animals:
            self.animals[animal_type] += count
        else:
            self.animals[animal_type] = count

    def get_animal_types(self):
        return sorted(self.animals.keys())

    def get_short_info(self):
        animal_types = self.get_animal_types()
        animal_types_str = ", ".join(animal_types)
        return f"{self.farm_name}'s farm has {animal_types_str}."

    def get_info(self):
        info_str = f"{self.farm_name}'s farm \n\n"
        for animal, count in self.animals.items():
            info_str += f"{animal} : {count}\n"
        info_str += "\n      E-I-E-I-0!" # you can use \t rather than the spaces
        return info_str

macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())

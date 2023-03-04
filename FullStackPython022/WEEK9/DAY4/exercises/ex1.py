# Instructions
# Create a class Human, it has the following attributes:
# name (str)
# age (int)
# living_place (Building - Default is None)
#
# Create another class Building, it has the following attributes:
# address (str)
# inhabitants (List of Human objects - Default is empty)
#
# Create a class City, it has the following attributes:
# name (str)
# buildings (List of Building objects - Default is empty)
#
# Add the move(self, building) method to the Human class, it sets the living place of this human to the building and add this human to the building inhabitants.
# Add the construct(self, address) method to the City class, it adds a building at the referenced address.
# Add the info(self, address) method to the City class, it displays the number of buildings and the mean age of the citizens.
# Created objects and call the methods
class Human:
    def __init__(self, name: str, age: int, living_place=None):
        self.name = name
        self.age = age
        self.living_place = living_place

    def move(self, building):
        if self.living_place:
            self.living_place.inhabitants.remove(self)
        self.living_place = building
        building.inhabitants.append(self)


class Building:
    def __init__(self, address: str, inhabitants=[]):
        self.address = address
        self.inhabitants = inhabitants


class City:
    def __init__(self, name: str, buildings=[]):
        self.name = name
        self.buildings = buildings

    def construct(self, address):
        self.buildings.append(Building(address))
        return self.buildings[-1]

    def info(self):
        for building in self.buildings:
            if building.inhabitants:
                total_age = sum(human.age for human in building.inhabitants)
                num_citizens = len(building.inhabitants)
                mean_age = total_age / num_citizens
                print(f"Building at {building.address}: {num_citizens} inhabitants with mean age of {mean_age:.1f}")
            else:
                print(f"No inhabitants in building with address {building.address}")


# Sample usage:
human1 = Human("Alice", 25)
human2 = Human("Bob", 30)
building1 = Building("123 Main St")
building2 = Building("456 Oak St")
city = City("New York")
city.construct("123 Main St")
city.construct("456 Oak St")
human1.move(building1)
human2.move(building2)
city.info()

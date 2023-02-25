# Instructions
# Create a class called Family and implement the following attributes:
#
# members: list of dictionaries with the following keys : name, age, gender and is_child (boolean).
# last_name : (string)
# Initial members data:
#
# [
#     {'name':'Michael','age':35,'gender':'Male','is_child':False},
#     {'name':'Sarah','age':32,'gender':'Female','is_child':False}
# ]
# Implement the following methods:
#
# born: adds a child to the members list (use **kwargs), don’t forget to print a message congratulating the family.
# is_18: takes the name of a family member as a parameter and returns True if they are over 18 and False if not.
# family_presentation: a method that prints the family’s last name and all the members’ first name.


class Family:
    def __init__(self, members, last_name):
        self.members = members
        self.last_name = last_name

    def born(self, **kwargs):
        child = {'name': kwargs.get('name'),
                 'age': kwargs.get('age'),
                 'gender': kwargs.get('gender'),
                 'is_child': True}
        self.members.append(child)
        print(f"Congratulations to the {self.last_name} family on the birth of their new child, {child['name']}!")

    def is_18(self, name):
        for member in self.members:
            if member['name'] == name:
                return member['age'] >= 18
        return False

    def family_presentation(self):
        first_names = [member['name'] for member in self.members]
        print(f"The {self.last_name} family: {' '.join(first_names)}")


family = Family([{'name':'Michael','age':35,'gender':'Male','is_child':False},{'name':'Sarah','age':32,'gender':'Female','is_child':False}], 'Gelfman')
family.born(name='Elis', age=14, gender='Female', is_child=True)
print(family.is_18('Michael'))
family.family_presentation()


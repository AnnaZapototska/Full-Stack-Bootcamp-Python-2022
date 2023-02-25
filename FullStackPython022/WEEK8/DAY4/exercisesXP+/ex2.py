# Instructions
# Create a class called TheIncredibles. This class should inherit from the Family class:
# This is no random family they are an incredible family, therefore we need to add the following keys to our dictionaries: power and incredible_name.
# Initial members data:
# [
#     {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
#     {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
# ]
# 2.Add a method called use_power, this method should print the power of a member only if they are over 18 years old. If not raise an exception (look up exceptions) which stated they are not over 18 years old.
# 3. Add a method called incredible_presentation which : * prints the family’s last name and all the members’ first name (ie. use the super() function, to call the family_presentation method) * prints all the members’ incredible name and power.
# 4. Call the incredible_presentation method.
# 5. Use the born method inherited from the Family class to add Baby Jack with the following power: “Unknown Power”.
# 6. Call the incredible_presentation method again.


from ex1 import Family


class TheIncredibles(Family):
    def use_power(self, name):
        for member in self.members:
            if member['name'] == name:
                if member['age'] > 18:
                    print(member['power'])
                else:
                    raise Exception(f"{name} is not over 18 years old.")

    def incredible_presentation(self):
        super().family_presentation()
        list_powers = []
        for member in self.members:
            if 'incredible_name' in member and 'power' in member:
                list_powers.append(f'{member["incredible_name"]} - {member["power"]}')
        if list_powers:
            print(f'Incredible names and powers: {", ".join(list_powers)}')


incredibles = TheIncredibles([{'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False, 'power': 'fly',
                               'incredible_name': 'MikeFly'},
                              {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False,
                               'power': 'read minds', 'incredible_name': 'SuperWoman'}], 'Gelfman')

incredibles.use_power('Michael')
incredibles.incredible_presentation()
incredibles.born(name='Elis', age=3, gender='Female', is_child=True, power='Unknown Power',
                 incredible_name='Baby Elis')
incredibles.incredible_presentation()

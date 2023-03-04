# Create a Door class, it has only the following attributes:
# id (int) : An id number, use a class variable objs that counts how many door have been created so far and use this number as the id of the door.
# locked (boolean)
# next (List of Door obs) : The next doors available from this one
#
# Create a method can_go_to(self, other_door) in the Door class that checks if the path from this door to other_door can be made (the locked doors cannot be opened !).
#
# Bonus: Display the path
# Bonus 2: Add an integer variable KEYS that holds a limited number of keys available to open locked doors (each key can be used only once).


class Door:
    objs = 0

    def __init__(self):
        Door.objs += 1
        self.id = Door.objs
        self.locked = False
        self.next = []

    def can_go_to(self, other_door):
        if other_door in self.next:
            if not other_door.locked:
                return True
            else:
                print(f"Door {other_door.id} is locked!")
                return False
        else:
            print(f"Door {other_door.id} is not connected to door {self.id}!")
            return False


d1 = Door()
d2 = Door()
d3 = Door()

d1.next = [d2]
d2.next = [d3]

print(d1.can_go_to(d2))
print(d1.can_go_to(d3))
print(d2.can_go_to(d1))
print(d2.can_go_to(d3))

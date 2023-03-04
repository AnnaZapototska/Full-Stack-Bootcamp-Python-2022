# Part 1
# You will have to create two classes:
# Human
# Queue
# Human
# Represents a citizen of the city, it has the following attributes: id_number (str), name (str), age (int), priority (bool) and blood_type (str). Its blood type can be “A”, “B”, “AB” or “O”.
# This class has no methods.
# Queue
# Represents a queue of humans waiting for their vaccine.
# It has the following attribute : humans, the list containing the humans that are waiting. It is initialized empty.
# This class is useful to manage who will get vaccinated in priority. It has the following methods:
# add_person(self, person) : Adds a human to the queue, if he is older than 60 years old or a priority person, put him at the beginning of the list (at index 0) before every other.
# find_in_queue(self, person) : Returns the index of a human in the queue.
# swap(self, person1, person2): Swaps person1 with person2.
# get_next(self) : Returns the next human waiting in the queue. The next human should be the one located at the index 0 in the list.
# get_next_blood_type(self, blood_type) : Returns the first human with this specific blood type.
# sort_by_age(self) : Sorts the queue
# first the priority people
# then, the older people
# then the younger people
# Every human returned by get_next and get_next_blood_type is removed from the list.
# Those functions return None if the list is empty (ie. no one in the list).
# Bonus: Don’t use any of the following built-in methods: list.insert, list.pop, list.index, list.sort, sorted.
# Part 2
# Human
# Create an attribute family for the Human class.
# Initialized as empty, family is a list of all the humans that are living in the same house with this human.
# Add a method add_family_member(self, person) that adds the person to this human’s family and this human to the person’s family.
# Queue
# Add the rearange_queue(self) method to the Queue class, so that there won’t be two members of the same family one after the other in the line.

class Human:
    def __init__(self, id_number, name, age, priority, blood_type):
        self.id_number = id_number
        self.name = name
        self.age = age
        self.priority = priority
        self.blood_type = blood_type
        self.family = []

    def add_family_member(self, person):
        if person not in self.family:
            self.family.append(person)
            person.add_family_member(self)


class Queue:
    def __init__(self):
        self.humans = []

    def add_person(self, person):
        if person.age >= 60 or person.priority:
            self.humans.insert(0, person)
        else:
            self.humans.append(person)
        self.rearrange_queue()

    def find_in_queue(self, person):
        for i, p in enumerate(self.humans):
            if p.id_number == person.id_number:
                return i
        return None

    def swap(self, person1, person2):
        index1 = self.find_in_queue(person1)
        index2 = self.find_in_queue(person2)
        self.humans[index1], self.humans[index2] = self.humans[index2], self.humans[index1]
        self.rearrange_queue()

    def get_next(self):
        if not self.humans:
            return None
        person = self.humans.pop(0)
        self.rearrange_queue()
        return person

    def get_next_blood_type(self, blood_type):
        for i, person in enumerate(self.humans):
            if person.blood_type == blood_type:
                self.humans.pop(i)
                self.rearrange_queue()
                return person
        return None

    def sort_by_age(self):
        priority_people = []
        older_people = []
        younger_people = []
        for person in self.humans:
            if person.priority:
                priority_people.append(person)
            elif person.age >= 60:
                older_people.append(person)
            else:
                younger_people.append(person)
        self.humans = priority_people + older_people + younger_people
        self.rearrange_queue()

    def rearrange_queue(self):
        for i in range(len(self.humans) - 1):
            if self.humans[i].family and self.humans[i].family == self.humans[i + 1].family:
                for j in range(i + 1, len(self.humans)):
                    if not self.humans[j].family or self.humans[j].family != self.humans[i].family:
                        self.humans[i + 1], self.humans[j] = self.humans[j], self.humans[i + 1]
                        break


h1 = Human("001", "John", 70, True, "A")
h2 = Human("002", "Mary", 30, False, "B")
h3 = Human("003", "Bob", 50, False, "AB")
h4 = Human("004", "Alice", 65, True, "O")
h5 = Human("005", "Tom", 20, False, "B")


h1.add_family_member(h2)
h1.add_family_member(h3)
h3.add_family_member(h4)
h5.add_family_member(h1)

q = Queue()

q.add_person(h1)
q.add_person(h2)
q.add_person(h3)
q.add_person(h4)
q.add_person(h5)

# check the queue order
for h in q.humans:
    print(h.name)

# swap two humans
q.swap(h2, h4)

# check the queue order again
for h in q.humans:
    print(h.name)

# get the next person
next_person = q.get_next()
print("Next person:", next_person.name)


next_a_person = q.get_next_blood_type("A")
print("Next person with blood type A:", next_a_person.name)

print(f"Sort by age:", q.sort_by_age())


for h in q.humans:
    print(h.name)

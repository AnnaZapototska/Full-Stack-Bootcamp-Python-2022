# Ex1

# What is a class?
# A class is a code template for creating objects.
# Objects have member variables and have behaviour associated with them.

# What is an instance?
# An instance is an individual object created from a class.
# It has its own set of values for the attributes defined in the class.

# What is encapsulation?
# Encapsulation is the practice of combining data and its related methods into a single unit.
# This mechanism involves hiding the internal details of a class from the outside world,
# so that the variables can only be accessed through the class's methods, and not directly by other classes.

# What is abstraction?
# Abstraction is a fundamental principle of object-oriented programming (OOP) languages, which involves simplifying complexity by concealing irrelevant details from the user. In Python, this process enables users to interact with the essential aspects of a program's functionality,
# while ignoring its implementation details.

# What is inheritance?
# Inheritance is a mechanism for creating new classes based on existing ones. The new class inherits the attributes and methods of the parent class and can also add new attributes and methods or override existing ones.

# What is multiple inheritance?
# Multiple inheritance is a feature of some object-oriented programming languages, including Python, that allows a class to inherit from more than one parent class.

# What is polymorphism?
# Polymorphism is the ability of objects of different classes to be used interchangeably. It allows a single interface to be used for objects of different types, and it is often achieved through inheritance and/or interfaces.

# What is method resolution order or MRO?
# The order in which a program searches for methods to call in a class hierarchy is known as the Method Resolution Order (MRO). Python uses the C3 linearization algorithm to determine the MRO, which considers both the order of inheritance and any instances of multiple inheritance. You can access the MRO of a class by calling its mro() method or by examining its __mro__ attribute.


# ex 2
# The Deck of cards class should NOT inherit from a Card class.
#
# The requirements are as follows:
#
# The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)
# The Deck class :
# should have a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
# should have a method called deal which deals a single card from the deck. After a card is dealt, it should be removed from the deck.

import random


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value


class Deck:
    def __init__(self):
        self.cards = []
        for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']:
            for value in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
                self.cards.append(Card(suit, value))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) == 0:
            return None
        else: #this else is redundant, please remove, because linke before you are doing return
            return self.cards.pop()


deck = Deck()
deck.shuffle()
card = deck.deal()
if card is not None:
    print(f"Dealt card: {card.value} of {card.suit}")
else:
    print("No cards left in the deck!")

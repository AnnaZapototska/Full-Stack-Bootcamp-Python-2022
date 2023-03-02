import math


class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None and diameter is not None: # think how you can implement this login using the classmethid
            raise ValueError("Both radius and diameter cannot be specified")
        elif radius is not None:
            self.radius = radius
            self.diameter = radius * 2
        elif diameter is not None:
            self.diameter = diameter
            self.radius = diameter / 2
        else:
            raise ValueError("Either radius or diameter must be specified")

    def area(self):
        return math.pi * self.radius ** 2

    def draw(self):
        size = self.radius * 2 + 1
        grid = [[' ' for _ in range(size)] for _ in range(size)]
        for y in range(size):
            for x in range(size):
                dx = x - self.radius
                dy = y - self.radius
                distance = math.sqrt(dx ** 2 + dy ** 2)
                if distance <= self.radius:
                    grid[y][x] = '*'

        # Print the grid
        for row in grid:
            print(' '.join(row))

    def __str__(self):
        return f"Circle with radius {self.radius}"

    def __repr__(self):
        return f"Circle({self.radius})"

    def __add__(self, other):
        print("The radius equal to the sum of the radii of the two circles")
        return print(Circle(radius=self.radius + other.radius)) # you can't return prin, you need to return somehitng of type Circle

    def __lt__(self, other):
        print("Compares two circles to see which is smaller")
        return print(self.radius < other.radius) # you can't return prin, you need to return boolean

    def __eq__(self, other):
        print("Compares two circles to see if they are equal")
        return print(self.radius == other.radius) # you can't return prin, you need to return boolean

c = Circle(radius=2)
print(f"The area circle: {c.area()}")
c.draw()

c1 = Circle(radius=8)
print(f"The area circle: {c1.area()}")
c1.draw()

c2 = Circle(radius=8)
print(f"The area circle: {c2.area()}")
c2.draw()

list_circles = [c, c1, c2]
list_circles.sort()
print(list_circles)

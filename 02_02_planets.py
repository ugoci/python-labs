# Create a `Planet()` class that models attributes and methods of
# a planet object.
# Use the appropriate dunder method to get informative output with `print()`

class Planet():
    
    def __init__(self, name, size, colour, distance, condition):
        self.name = name
        self.size = size
        self.colour = colour
        self.distance = distance 
        self.condition = condition

e = Planet("earth", 100, "blue", 1000, "habitable")
v = Planet("venus", 1000, "brown", 10000, "inhabitable")
p = Planet("pluto", 10, "white", 1000000, "cold")
        
print(e.name)
print(v.name, v.colour)
print(p.name, p.size, p.condition)
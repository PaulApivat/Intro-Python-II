# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    
    def __init__(self, name, description):
        self.name = name 
        self.description = description

    def __repr__(self):
        return "The current room is.. " + self.name + "..description " + self.description

my_room = Room("Placeholder Room", "Foyer")
print(my_room)
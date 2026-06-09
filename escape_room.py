"""
Escape Room Game - Logic implementation for rooms and items
"""

# Global inventory to keep track of items across different rooms 
# Without needing a separate Player class, but it would be better.
player_inventory = []


class Room:
    """
    A class representing a single room in the escape game
    """

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []          # Items currently lying on the floor
        self.exits = {}          # Maps direction to Room object
        self.locked_doors = {}   # Maps direction to the name of the required key

    def add_exit(self, direction, room, required_key=None):
        self.exits[direction] = room
        if required_key:
            self.locked_doors[direction] = required_key

    def add_item(self, item_name):
        self.items.append(item_name)

    def move(self, direction):
        print(f"\nYou try to move in the {direction}")
        if direction not in self.exits:
            print(f"There is no exit to the {direction}")
            return self

        if direction in self.locked_doors:
            key_needed = self.locked_doors[direction]
            print(f"The door to the {direction} is locked")
            print(f"Hint: You need a '{key_needed}' to pass")
            return self

        next_room = self.exits[direction]
        print(f"You walk into the {next_room.name}")
        return next_room

    def pick_up(self, item_name):
        print(f"\nYou try to pick up {item_name}")
        if item_name in self.items:
            self.items.remove(item_name)
            player_inventory.append(item_name)
            print(f"You picked up: {item_name}")
        else:
            print(f"I don't see a '{item_name}' here")

    def use_item(self, item_name, direction=None):
        print(f"\nYou try to use {item_name}")
        if item_name not in player_inventory:
            print(f"You don't have a '{item_name}' in your pockets")
            return

        # Case: Unlocking a door
        if direction:
            if direction in self.locked_doors:
                if self.locked_doors[direction] == item_name:
                    print(f"Click! The {item_name} unlocked the {direction} door")
                    del self.locked_doors[direction]
                    # player_inventory.remove(item_name) ## we could remove the object
                else:
                    print(f"The {item_name} doesn't seem to work on the {direction} door")
            else:
                print(f"The {direction} door isn't locked")
        else:
            print(f"You used the {item_name}, but nothing happened")

    def __str__(self):
        output = f"\n> LOCATION: {self.name}\n"
        output += f"  {self.description}\n\n"

        # List items
        if self.items:
            output += f"  Visible items: {', '.join(self.items)}\n"
        else:
            output += "  The room is empty of items.\n"

        # List exits
        exit_desc = []
        for direction in self.exits:
            status = "(LOCKED)" if direction in self.locked_doors else "(Open)"
            exit_desc.append(f"{direction} {status}")
        
        output += f"  Exits: {', '.join(exit_desc)}\n"
        
        # Show global inventory status
        inv_str = ", ".join(player_inventory) if player_inventory else "Empty"
        output += f"\n  Your Inventory: {inv_str}\n"
        
        return output


def run_test_game():
    
    # Create rooms
    cell = Room("Dungeon Cell", "A cold, damp stone cell. The air is stale")
    hallway = Room("Dark Hallway", "A long corridor with torches flickering on the walls")
    exit_gate = Room("The Great Gate", "A massive iron gate leading to freedom")

    # Setup connections and locks
    cell.add_exit("north", hallway)
    cell.add_item("Brass Key")
    
    hallway.add_exit("south", cell)
    hallway.add_exit("east", exit_gate, required_key="Brass Key")
    hallway.add_item("Old Torch")

    # Game start
    current_room = cell
    print("\nStarting Escape Game Simulation")
    print(current_room)

    # Test moving to existing exit
    current_room = current_room.move("north")
    print(current_room)

    # Test trying to move through a locked door
    current_room = current_room.move("east")
    
    # Test picking up an item
    current_room = current_room.move("south")
    print(current_room)
    current_room.pick_up("Brass Key")
    print(current_room)

    # Test unlocking the door
    current_room = current_room.move("north")
    print(current_room)
    current_room.use_item("Brass Key", direction="east")
    
    # Test final move
    current_room = current_room.move("east")
    print(current_room)
    print("\nSimulation complete. You escaped!")


if __name__ == "__main__":
    run_test_game()

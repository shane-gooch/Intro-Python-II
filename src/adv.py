from room import Room
from player import Player
from item import Item

# Create Item Objects
sword = Item("sword")
hammer = Item("hammer")
gaterode = Item("gaterode")
helmet = Item("helemt")
wings = Item("wings")
computer = Item("computer")
glasses = Item("glasses")
bike = Item("bike")
cloak = Item("cloak",)

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [sword, hammer]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [gaterode, helmet, wings]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [computer]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [glasses, bike]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [cloak]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player_one = Player("Bobby Smith", room["outside"])

is_active = True
while is_active:
    # Handle Exception

    # Print info
    print("\n" + player_one.get_name() + " is in \"",
          player_one.get_current_room().get_name() + "\"\n")
    print(player_one.get_current_room().get_description() + "\n")
    print("Items Available:")
    print(player_one.get_current_room().print_items())
    print(player_one.get_name(), " please enter a command: " +
          "\n[n]: North\n[w]: West\n[e]: East\n[s]: South")
    # Handle user input
    command = input().lower()
    # Splting input
    c_arr = command.split()
    if len(c_arr) == 1:
        # Control flow for command
        if command in ["n", "s", "e", "w"]:
            player_one.move_player(command)
        elif command == "i":
            player_one.get_inventory()
        elif command == "q":
            print("Ending game for " + player_one.get_name())
            is_active = False
        else:
            print("Invalid Command - Try again")
            continue
    else:
        # Player takes, room drops
        if c_arr[0] in ["take", "get"]:
            if player_one.get_current_room().check_items(c_arr[1]):
                # Pop from room's list / add to player's list
                taken_item = player_one.get_current_room(
                ).remove_item(c_arr[1])
                player_one.add_item(taken_item)
            else:
                print("Item not in " + player_one.get_current_room().get_name())

        elif c_arr[0] in ["drop", "take"]:
            if player_one.check_items(c_arr[1]):
                # Pop from room's list / add to player's list
                dropped_item = player_one.drop_item(c_arr[1])
                player_one.get_current_room().add_item(dropped_item)
            else:
                print(f"You do not have a {c_arr[1]}")
        else:
            print("incorrect command try again")

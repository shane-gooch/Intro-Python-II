from room import Room
from player import Player
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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
count += 1
while is_active:
    # Handle Exception
    try:
        # Print info
        print(player_one.get_name() + " is in \"",
              player_one.get_current_room().get_name() + "\"\n")
        print(player_one.get_current_room().get_description() + "\n")
        print(player_one.get_name(), " please enter a command: " +
              "\n[n]: North\n[w]: West\n[e]: East\n[s]: South")
        # Handle user input
        command = input().lower()

        # Control flow for command
        if command in ["n", "s", "e", "w"]:
            player_one.move_player(command)
        elif command == "q":
            print("Ending game for " + player_one.get_name())
            is_active = False
        else:
            print("Invalid Command - Try again")
            continue

    except AttributeError:
        print("Unable to move in that direction")
        break

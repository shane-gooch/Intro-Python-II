# Write a class to hold player information, e.g. what room they are in
# currently.


class Player():
    def __init__(self, name, current_room):
        self.__name = name
        self.__current_room = current_room

    def move_player(self, command):
        move = {
            "n": self.__current_room.n_to,
            "s": self.__current_room.s_to,
            "w": self.__current_room.w_to,
            "e": self.__current_room.e_to
        }
        self.__current_room = move[command]
        print(self.__name, " is in ", self.__current_room.get_name())

    def get_name(self):
        return self.__name

    def get_current_room(self):
        return self.__current_room

# Write a class to hold player information, e.g. what room they are in
# currently.


class Player():
    def __init__(self, name, current_room):
        self.__name = name
        self.__current_room = current_room
        self.__items = []

    def move_player(self, command):
        move = {
            "n": self.__current_room.n_to,
            "s": self.__current_room.s_to,
            "w": self.__current_room.w_to,
            "e": self.__current_room.e_to
        }
        self.__current_room = move[command]

    def get_name(self):
        return self.__name

    def get_current_room(self):
        return self.__current_room

    def add_item(self, item):
        self.__items.append(item)
        print(item.on_take())
        print("size", len(self.__items))

    def check_items(self, item):
        for i in range(len(self.__items)):
            if self.__items[i].get_name().lower() == item:
                return True
        return False

    def drop_item(self, item):
        if len(self.__items) < 1:
            return f"{self.__name} has no items"
        else:
            index = 0
            for i in range(len(self.__items)-1):
                print("index", index)
                if self.__items[i].get_name().lower == item:
                    break
                index += 1
            print("drop", len(self.__items))
            return self.__items.pop(index)
            print(item.on_drop())

    def get_inventory(self):
        for i in self.__items:
            print(f"{self.__name} has the following items: \n{i.get_name()}")

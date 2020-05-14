# Implement a class to hold room information. This should have name and
# description attributes.


class Room():

    def __init__(self, name, description, items=[]):
        self.__name = name
        self.__description = description
        self.n_to = None
        self.w_to = None
        self.e_to = None
        self.s_to = None
        self.__items = items

    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def get_items(self):
        return self.__items

    def print_items(self):
        if len(self.__items) < 1:
            return "No items in " + self.__name + "."
        else:
            for i in range(len(self.__items)):
                print(self.__items[i].get_name())

    def add_item(self, item):
        self.__items.append(item)

    def remove_item(self, item):
        # Get index of item
        index = 0
        for i in range(len(self.__items)-1):
            if self.__items[i].get_name().lower() == item:
                break
            index += 1
        return self.__items.pop(index)

    def check_items(self, item):
        for i in range(len(self.__items)-1):
            if self.__items[i].get_name().lower() == item:
                return True
        return False

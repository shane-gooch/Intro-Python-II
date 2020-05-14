
class Item():
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def on_take(self):
        return f"\nYou have picked up a {self.__name}"

    def on_drop(self):
        return f"\nYou have dropped a {self.__name}"

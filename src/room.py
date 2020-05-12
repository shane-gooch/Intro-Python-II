# Implement a class to hold room information. This should have name and
# description attributes.


class Room():

    def __init__(self, name, description):
        self.__name = name
        self.__description = description
        self.n_to = None
        self.w_to = None
        self.e_to = None
        self.s_to = None

    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

from name import Name
from names import Names
from name_gen import NameGen


class Manager:

    def __init__(self):
        self.name = Name()
        self.names = Names()
        self.ng = NameGen()

    def __repr__(self):
        return 'Manager'

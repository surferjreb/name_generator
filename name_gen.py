import random as rand
from name import Name
from names import Names

class NameGen:
    '''
        The name generator class is as it implies, it generates the names
        @author: James R Brown

        .. autoclass::
           :methods:

    '''

    def __init__(self, amount=100, unique=False, names=Names()):
        self.amount = amount
        self.unique = unique
        self.names = names

    def generate_names(self):
        for i in range(0, self.amount):
            temp = self._gen_name()
            self.names.add_name(temp)

    def _gen_name(self):
        rand_nums = (rand.randint(0, len(self.names.FIRST_NAMES)),
                     rand.randint(0, len(self.names.LAST_NAMES)),
                     rand.randint(0, len(self.names.MIDDLE_NAMES)))

        first = self.get_rand_first(rand_nums[0])
        last = self.get_rand_last(rand_nums[1])
        middle = self.get_rand_middle(rand_nums[2])

        name = Name(first, last, middle)

        return name

    def get_rand_first(self, rand_num):
        temp_first = self._get_rand_name(rand_num, self.names.FIRST_NAMES)
        return temp_first

    def get_rand_last(self, rand_num):
        temp_last = self._get_rand_name(rand_num, self.names.LAST_NAMES)
        return temp_last

    def get_rand_middle(self, rand_num):
        temp_middle = self._get_rand_name(rand_num, self.names.MIDDLE_NAMES)
        return temp_middle

    def _get_rand_name(self, rand_num, name_list):
        temp_name = None

        if rand_num < len(name_list):
            temp_name = name_list[rand_num]
        return temp_name

    def check_dup(self):
        pass

    def __repr__(self):
        return 'Name Generator'

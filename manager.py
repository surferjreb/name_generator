from names import Names
from name_gen import NameGen


class Manager:

    def __init__(self):
        self.names = Names()
        self.ng = NameGen(names=self.names)
        self.ran = False

    def run_name_gen(self):
        try:
            self.ng.generate_names()
            self.ran = True
        except Exception:
            raise Exception('Name generator failed to run')

    def set_name_inputs(self, nameType, nameStr)
        pass

    def print_names_list(self):
        pass

    def output_names_list(self):
        pass

    def __repr__(self):
        return 'Manager'

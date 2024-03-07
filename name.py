'''
    The name class used for name object that is created
    @author: James R Brown

'''



class Name:

    def __init__(self, firstName='Jane', lastName='Doe'):
        self.firstName = firstName
        self.lastName = lastName

    def get_firstName(self):
        '''
            returns the first name as a new string.
        '''
        return str(self.firstName)

    def get_lastName(self):
        '''
            returns the last name as a new string.
        '''
        return str(self.lastName)

    def set_firstName(self, firstName):
        '''
           Sets a new string using firstName paramater to the variable
           firstName.
        '''
        self.firstName = str(firstName)

    def set_lastName(self):
        '''
           Sets a new string using lastName paramater to the variable
           lastName.
        '''
        self.lastName = str(lastName)

    def __repr__(self):
        return f'{self.firstName} {self.lastName}'

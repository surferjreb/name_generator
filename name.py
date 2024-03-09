

class Name:
    '''

        The name class used for name object that is created.
        @author: James R Brown

        .. autoclass:: Name
           :methods:

    '''
    def __init__(self, firstName=None, lastName=None, middleName=None):
        self.firstName = firstName
        self.lastName = lastName
        self.middleName = middleName

    def get_firstName(self):
        '''

            Returns first name as a new string.

            :return: first name string
            :rtype: str
        '''
        if type(self.firstName) is bytes:
            return str(self.firstName, 'utf-8', 'strict')
        return self.firstName

    def get_lastName(self):
        '''
            Returns last name as a new string.

            :return: last name string
            :rtype: str

        '''
        if type(self.lastName) is bytes:
            return str(self.lastName, 'utf-8', 'strict')
        return self.lastName

    def get_middleName(self):
        '''
            Returns last name as a new string.

            :return: last name string
            :rtype: str

        '''
        if type(self.middleName) is bytes:
            return str(self.middleName, 'utf-8', 'strict')
        return self.middleName

    def set_firstName(self, firstName):
        '''
           Sets a new string using firstName paramater to the variable
           firstName.

           :param firstName: string value for first name.
           :type firstName: str

        '''
        self.firstName = self._set_name(firstName)

    def set_lastName(self, lastName):
        '''
           Sets a new str byte value using the string lastName paramater.  This
           saves to class variable lastName

           :param lastName: The string value for lastName
           :type lastName: str

        '''
        self.lastName = self._set_name(lastName)

    def set_middleName(self, middleName):
        '''
           Sets a new str byte value using the string middleName paramater.  This
           saves to class variable middleName

           :param middleName: The string value for middleName
           :type middleName: str

        '''
        self.middleName = self._set_name(middleName)

    def _set_name(self, name):
        '''
            Takes a string input and encodes it into a byte value.  Returns
            the value if it is not numeric, else returns None.

            :param name: Should be a string value
            :type name: str
            :raise name.Exception: if an error occurs
            :return: the byte encoded str value or None
            :rtype: byte

        '''
        temp_name = None

        try:
            if name is not None:
                name = name.lower()
                temp_name = str(name).encode(encoding='utf-8', errors='strict')
            return temp_name
        except Exception:
            raise Exception('set name failed')

    def __str__(self):
        '''

            Returns a string representation of the class

        '''
        if self.middleName is None or self.middleName == b' ':
            return f'{self.get_firstName()} {self.get_lastName()}'
        elif self.middleName == ' ':
            return f'{self.get_firstName()} {self.get_lastName()}'
        n = '{} {} {}'.format(self.get_firstName(),
                              self.get_middleName(), self.get_lastName())
        return n

    def __repr__(self):
        '''

            Returns the raw values in name.

            :returns: name values
            :rtype: str

        '''

        return f'{self.firstName} {self.middleName} {self.lastName}'



class Name:
    '''

        The name class used for name object that is created.
        @author: James R Brown

        .. autoclass:: Name
           :methods:

    '''
    def __init__(self, firstName='jane', lastName='doe', middleName=None):
        self.firstName = self._set_name(firstName)
        self.lastName = self._set_name(lastName)
        self.middleName = self._set_name(middleName)

    def get_firstName(self):
        '''

            Returns first name as a new string.

            :return: first name string
            :rtype: str
        '''
        return str(self.firstName, 'utf-8', 'strict')

    def get_lastName(self):
        '''
            Returns last name as a new string.

            :return: last name string
            :rtype: str

        '''
        return str(self.lastName, 'utf-8', 'strict')

    def get_middleName(self):
        '''
            Returns last name as a new string.

            :return: last name string
            :rtype: str

        '''
        return str(self.middleName, 'utf-8', 'strict')

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
            temp_name = str(name.lower()).encode(encoding='utf-8', errors='strict')
            return temp_name
        except Exception:
            raise Exception('set name failed')

    def __repr__(self):
        '''
            Returns str format of name depending on the value in middleName.

            :returns: name string
            :rtype: str

        '''
        if self.middleName == b'None':
            return f'{self.get_firstName()} {self.get_lastName()}'

        return '{} {} {}'.format(self.get_firstName(), self.get_middleName(),
                                 self.get_lastName()
                                 )

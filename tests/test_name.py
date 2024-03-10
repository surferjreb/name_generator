from name import Name
import pytest

'''
    Test for the Name Class
'''


@pytest.fixture
def default_name():
    '''
        Test fixture for Name Class
    '''
    return Name()


@pytest.fixture
def test_two_name():
    '''
        Test fixture for a two name value.

        :return: a tuple with str name values
        :rtype: tuple(str)

    '''
    first = 'James'
    last = 'Brown'
    return (first, last)


@pytest.fixture
def test_three_name(test_two_name):
    '''
        Test fixture for three name value.  Used to test class creation and
        the return values for those created classes.

        :return: The name witha middle name.
        :rtype: tuple(str)

    '''
    middle = 'Robert'
    return (test_two_name[0], test_two_name[1], middle)


@pytest.fixture
def test_default_name():
    '''
        Test fixture for testing the default return value of __repr__ for a
        class that is created with no values passed.

        :return: None str value __repr__ should return
        :rtype: str

    '''
    return f'{None} {None} {None}'


def test_name_class(test_two_name):
    '''
        Test the creation of the Name class.
    '''
    tn = Name(test_two_name[0], test_two_name[1])
    assert tn is not None


def test_default_name_created(default_name, test_default_name):
    '''
        Test that the default created class returns the default __repr__ value.

    '''
    assert default_name.__repr__() == test_default_name


def test_two_name_str(test_two_name):
    '''
        Test the created class returns the __str__ value of the name.
    '''
    tn = Name(test_two_name[0], test_two_name[1])

    assert tn.__str__() == '{} {}'.format(test_two_name[0],
                                          test_two_name[1],
                                          )


def test_three_name_str(default_name, test_three_name):
    '''
        Test the instanciated class returns the __str__ value of the name.
    '''
    tn = Name(test_three_name[0], test_three_name[1], test_three_name[2])

    assert tn.__str__() == '{} {} {}'.format(test_three_name[0],
                                             test_three_name[2],
                                             test_three_name[1]
                                             )


def test_set_first_name(default_name, test_two_name):
    '''
        Test setting the firstName of the default class by it returning the
        correct value.
    '''
    default_name.set_firstName(test_two_name[0])
    assert default_name.get_firstName() == test_two_name[0]


def test_set_first_fail(default_name, test_default_name):
    '''
        Test that name fails to set then returns exception
    '''
    # first, last, middle = test_default_name.split(' ')
    with pytest.raises(TypeError):
        default_name.set_firstName(1234)


def test_set_first_None(default_name):
    '''
        Test that name when set with NoneType just sets it but returns a empty
        string.
    '''

    default_name.set_firstName(None)
    assert default_name.get_firstName() == ' '


def test_set_last_name(default_name, test_two_name):
    '''
        Test setting the lastName of the default class by it returning the
        correct value.
    '''
    default_name.set_lastName(test_two_name[1])
    assert default_name.get_lastName() == test_two_name[1]


def test_set_last_fail(default_name):
    '''
        Test that name fails to set then returns exception
    '''
    # first, last, middle = test_default_name.split(' ')
    with pytest.raises(TypeError):
        default_name.set_lastName(1234)


def test_set_last_None(default_name):
    '''
        Test that name when set with NoneType just sets it but returns a empty
        string.
    '''

    default_name.set_lastName(None)
    assert default_name.get_lastName() == ' '


def test_set_middle_name(default_name, test_three_name):
    '''
        Test setting the middleName of the default class by it returning the
        correct value.
    '''
    default_name.set_middleName(test_three_name[2])
    assert default_name.get_middleName() == test_three_name[2]


def test_set_middle_fail(default_name):
    '''
        Test that name fails to set then returns exception
    '''
    # first, last, middle = test_default_name.split(' ')
    with pytest.raises(TypeError):
        default_name.set_middleName(1234)


def test_set_middle_None(default_name):
    '''
        Test that name when set with NoneType just sets it but returns a empty
        string.
    '''

    default_name.set_middleName(None)
    assert default_name.get_middleName() == ' '

from name import Name
from names import Names
import pytest


'''
    Tests the Names Class
'''


@pytest.fixture
def name_ob():
    '''
       Test name object created for test.
    '''
    n = Name('jane', 'doe', 'l')
    return n


@pytest.fixture
def test_names_list():
    '''
        Test names object created for test
    '''
    n = Names()
    return n


def test_names_creation(test_names_list):
    '''
        Tests that the names class is created when called.
    '''

    assert test_names_list is not None


def test_add_name(test_names_list, name_ob):
    '''
        Tests that a name can be added to the name list.
    '''
    test_names_list.add_name(name_ob)
    assert len(test_names_list.get_names()) == 1


def test_get_name(test_names_list, name_ob):
    '''
        Tests that a names can be added to the list and retrieved.
    '''
    test_names_list.add_name(name_ob)

    assert test_names_list.get_names()[0].__str__() == name_ob.__str__()

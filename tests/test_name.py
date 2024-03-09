from name import Name
import pytest


@pytest.fixture
def default_name():
    return Name()


@pytest.fixture
def test_name():
    first = 'James'
    middle = 'Robert'
    last = 'Brown'
    return (first, middle, last)


@pytest.fixture
def test_default():
    return f'{None} {None} {None}'


def test_create_name(default_name, test_name):
    tn = Name(test_name[0], test_name[2], test_name[1])
    assert tn.__str__() == '{} {} {}'.format(test_name[0],
                                             test_name[1],
                                             test_name[2]
                                             )


def test_default_name_created(default_name, test_default):
    assert default_name.__repr__() == test_default

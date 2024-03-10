from name_gen import NameGen
import pytest


'''
    This is a test for the NameGen class.
'''


@pytest.fixture
def test_name_gen():
    ng = NameGen()
    return ng


def test_class_creation(test_name_gen):
    assert test_name_gen is not None


def test_class_default_amount(test_name_gen):
    ng = test_name_gen
    assert ng.amount == 100


def test_class_default_bool(test_name_gen):
    ng = test_name_gen
    assert ng.unique is False


def test_class_default_names(test_name_gen):
    ng = test_name_gen
    assert ng.names is not None


def test_generate_names(test_name_gen):
    ng = test_name_gen
    ng.generate_names()

    assert len(ng.names.get_names()) == 100

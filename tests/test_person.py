import pytest

from hrank._30_days_of_code._05_class_vs_instance import Person


def test_person_creation(capsys):
    human = Person(initial_age=12)
    assert human.age == 12
    human.am_i_old()
    assert capsys.readouterr().out == 'You are young.\n'

    human.year_passes()
    assert human.age == 13
    human.am_i_old()
    assert capsys.readouterr().out == 'You are a teenager.\n'

    human.year_passes()
    human.year_passes()
    human.year_passes()
    human.year_passes()
    human.year_passes()
    assert human.age == 18
    human.am_i_old()
    assert capsys.readouterr().out == 'You are old.\n'

from models.container import Scamp
from scamp import generatePeople, checkActivity, reset, mainprocess
import pytest
import copy

test_cases = generatePeople()

def test_valid_cases_created():
    for case in test_cases:
        for item in case:
            assert isinstance(item, int)

def test_valid_checkActivity():
    updated_count, updated_idx = checkActivity(0, 0, test_cases, 0)
    assert updated_count > 0 and (updated_idx >= 0 and updated_idx < len(test_cases))

def test_valid_reset():
    test_cases_1 =  copy.deepcopy(test_cases)
    test_cases_2 = reset(0, test_cases_1, 1)
    assert test_cases[1] == test_cases_2[1]

def test_valid_reset1():
    test_cases_1 =  copy.deepcopy(test_cases)
    test_cases_2 = reset(0, test_cases_1, 1)
    assert test_cases[0] != test_cases_2[0] and test_cases[2] == test_cases_2[2] and test_cases[3] != test_cases_2[3]

def test_valid_main():
    test_cases_1 = mainprocess()
    assert test_cases != test_cases_1
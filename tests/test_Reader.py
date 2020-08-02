#  testing
import pytest

# base
import os
import sys
import json
import pandas as pd
import datetime

# internal
from etl_project_template.data_handling import Reader


# mock data
mock_data = {}


@pytest.fixture
def my_reader():
    
    return Reader()


def test_func(my_reader):
    arg = 'some_val'

    # desired result
    desired_result = {}

    assert my_reader.func(arg) == desired_result


def test__private_func(my_reader):
    arg = 'some_val'
    
    # desired result
    desired_result = {}

    assert my_reader._private_func(arg) == desired_result




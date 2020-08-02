#  testing
import pytest

# base
import os
import sys
import json
import pandas as pd
import datetime

# internal
from etl_project_template.data_handling import Writer


# mock data
mock_data = {}


@pytest.fixture
def my_writer():
    
    return Writer()


def test_func(my_class_name1):
    arg = 'some_val'

    # desired result
    desired_result = {}

    assert my_writer.func(arg) == desired_result


def test__private_func(my_class_name1):
    arg = 'some_val'
    
    # desired result
    desired_result = {}

    assert my_writer._private_func(arg) == desired_result

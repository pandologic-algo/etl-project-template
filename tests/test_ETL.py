#  testing
import pytest

# base
import os
import sys
import json
import pandas as pd
import datetime

# internal
from etl_project_template.etl import ETL


@pytest.fixture
def my_etl():
    return ETL()


def test_run(my_etl):
    assert my_etl.run() == True

# test_write_data.py
# Author: Paramveer Singh
# 11 December 2024

# Tests write_data.py in various use cases and incorrect inputs

import pytest
import os
import pandas as pd
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.write_data import write_data


# Test input data
PATH = './test_data/'

simple_dataframe = pd.DataFrame(
    {
        'x': [i for i in range(10)],
        'y': [i**2 for i in range(10)]
    }
)

multi_type_dataframe = pd.DataFrame(
    {
        'floats': [-0.1, 0.34, 0.42, 1.34],
        'ints': [1, 2, 3, 4],
        'strings': ['A', 'B', 'B', 'A']
    }
)

empty_df = pd.DataFrame({'x': [], 'y': []})

wrong_type = {'x': [0.1, 0.2],  'y': ['hit', 'miss']}

# `write_data` should return a integer status code
# with 0 signifying success and other numbers signifying errors
# The function will write a CSV and it must be tested that the output is a proper CSV
# and matches the original DataFrame
def test_write_data_success():
    filename = 'simple_dataframe.csv'

    status = write_data(simple_dataframe, PATH, filename)
    
    # Test if the returned value was int and was successful
    assert isinstance(status, int), 'Did not return integer'
    assert status == 0, 'CSV write has failed!'

    # Test if the file was created and named correctly
    file_path = os.path.join(PATH, filename)
    assert os.path.isfile(file_path)

    # Check if outputted CSV is the same as the test input
    file_df = pd.read_csv(file_path)
    pd.testing.assert_frame_equal(simple_dataframe.reset_index(drop=True), file_df)

# `write_data` should also be able to handle columns of different dtypes
def test_write_data_dtypes_success():
    filename = 'multi_type_dataframe.csv'

    status = write_data(multi_type_dataframe, PATH, filename)

    # Test if the returned value was int and was succesful
    assert isinstance(status, int), 'Did not return integer'
    assert status == 0, 'CSV write has failed!'

    # Test if the file was created and named correctly
    file_path = os.path.join(PATH, filename)
    assert os.path.isfile(file_path)

    # Check if outputted CSV is the same as the test input
    file_df = pd.read_csv(file_path)
    pd.testing.assert_frame_equal(multi_type_dataframe.reset_index(drop=True), file_df)
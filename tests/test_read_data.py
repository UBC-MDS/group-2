# test_read_data.py
# Author: Paramveer Singh
# 15 December 2024

# This file tests the read_data function to test for
# erroneous filenames and non-existent paths

import pytest
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.read_data import read_data

import pandas as pd

TEST_PATH = './tests/test_data/'

os.makedirs(TEST_PATH, exist_ok=True)

dummy_data = pd.DataFrame({
        'x': [2*i for i in range(10)],
    })
dummy_data['y'] = dummy_data['x'] ** 2
    
dummy_data.to_csv(os.path.join(TEST_PATH, 'dummy.csv'), index=False)

# Test if the data read back in is the same as the data written out
def test_read_data_success():
    
    df = read_data(os.path.join(TEST_PATH, 'dummy.csv'))

    pd.testing.assert_frame_equal(dummy_data.reset_index(drop=True), df)

# Test if the function throws a FileNotFoundError for non-existent directory or file
def test_read_data_missing_dir():

    with pytest.raises(FileNotFoundError):
        read_data(os.path.join('./tests/test_data_dummy', 'dummy.csv'))

# Test if the function throws a ValueError for filename not ending in .csv
def test_read_data_wrong_ext():

    with pytest.raises(ValueError):
        read_data(os.path.join(TEST_PATH, 'dummy.txt'))

def test_clean():
    os.remove(os.path.join(TEST_PATH, 'dummy.csv'))
    os.removedirs(TEST_PATH)
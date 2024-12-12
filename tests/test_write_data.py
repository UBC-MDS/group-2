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
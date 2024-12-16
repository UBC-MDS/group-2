# read_data.py
# Author: Paramveer Singh
# 15 Decemeber 2024

import os
import pandas as pd

def read_data(filepath: str) -> pd.DataFrame:
    """
    Reads and returns data as a pandas DataFrame from a CSV
    and throws errors when given a non-existent directory or incorrect filename

    Parameters
    ----------
    filepath : str
        The path to the data file
    
    Returns
    -------
    pd.DataFrame
        The loaded in data from the file

    Example
    -------
    >>> raw_data = read_data('./data/raw/wine_quality.csv')
    """
    if not os.path.basename(filepath).endswith('.csv'):
        raise ValueError('Filename does not end with .csv')

    data = pd.read_csv(filepath)

    return data

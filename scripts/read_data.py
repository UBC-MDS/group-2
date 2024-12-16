# read_data.py
# Author: Paramveer Singh
# 5 December 2024

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import click
import pandas as pd
from sklearn.model_selection import train_test_split
from src.read_data import read_data

@click.command()
@click.argument('cleaned_data_path',
                default='./data/processed/cleaned_wine_quality.csv',
                type=str)
@click.argument('processed_data_path',
                default='./data/processed',
                type=str)
@click.option('--seed',
              default=522,
              type=int,
              help='Random seed used to separate data')
@click.option('--test_size',
              default=0.2,
              type=float,
              help='Proportion of data to use in test set')
def read_split_data(cleaned_data_path, processed_data_path, seed, test_size):
    """
    Reads cleaned data from CLEANED_DATA_PATH and splits it into
    training and test sets and stores that at the folder
    specified by PROCESSED_DATA_PATH. The data will be output as
    training_set.csv and test_set.csv

    CLEANED_DATA_PATH is the relative path to the validated data CSV file.
    PROCESSED_DATA_PATH is the relative path to the folder where split data is stored.

    By default, it reads from the data/raw folder and stores data splits in data/processed.
    The random seed is 522 by default and yields an 80:20 split for training and test.
    """
    # Make sure folder exists for output
    os.makedirs(processed_data_path, exist_ok=True)

    # Read data to split into training and test sets
    cleaned_data = read_data(cleaned_data_path)

    train_df, test_df = train_test_split(cleaned_data, test_size=test_size, random_state=seed)

    # Store the training and test sets
    train_df.to_csv(os.path.join(processed_data_path, 'training_set.csv'), index=False)
    test_df.to_csv(os.path.join(processed_data_path, 'test_set.csv'), index=False)

if __name__ == '__main__':
    read_split_data()
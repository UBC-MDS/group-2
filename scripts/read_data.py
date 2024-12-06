# read_data.py
# Author: Paramveer Singh
# 5 December 2024

import os
import click
import pandas as pd
from sklearn.model_selection import train_test_split

@click.command()
@click.argument('raw_data_path',
                default='./data/raw/wine_quality.csv',
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
def read_split_data(raw_data_path, processed_data_path, seed, test_size):
    """
    Reads raw data from RAW_DATA_PATH and splits it into
    training and test sets and stores that at the folder
    specified by PROCESSED_DATA_PATH. The data will be output as
    training_set.csv and testing_set.csv

    RAW_DATA_PATH is the relative path to the raw data CSV file.
    PROCESSED_DATA_PATH is the relative path to the folder where split data is stored.

    By default, it reads from the data/raw folder and stores data splits in data/processed.
    The random seed is 522 by default and yields an 80:20 split for training and test.
    """
    # Make sure folder exists for output
    os.makedirs(processed_data_path, exist_ok=True)

    # Read data to split into training and test sets
    raw_data = pd.read_csv(raw_data_path)

    train_df, test_df = train_test_split(raw_data, test_size=test_size, random_state=seed)

    # Store the training and test sets
    train_df.to_csv(os.path.join(processed_data_path, 'training_set.csv'), index=False)
    test_df.to_csv(os.path.join(processed_data_path, 'testing_set.csv'), index=False)

if __name__ == '__main__':
    read_split_data()
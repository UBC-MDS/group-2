# data_download.py
# Author: Paramveer Singh
# 3 December 2024

import os
import click
import pandas as pd
from ucimlrepo import fetch_ucirepo

@click.command()
@click.option('--id', default=186, type=int, help='UCI repo ID of dataset')
@click.option('--raw_data_out',
              default='../data/raw/',
              type=str,
              help='Relative path save the raw data to')
def load_save_data(id, raw_data_out):
    """
    Get the dataset from UCI repo and save locally
    """
    # Fetch the data
    uci_data = fetch_ucirepo(id=id)
    raw_data = uci_data.data.original

    # Ensure the specified directories exist
    os.makedirs(raw_data_out, exist_ok=True)

    # reorder columns
    raw_data['quality'] = raw_data.pop('quality')

    # Save data into the folder
    raw_data.to_csv(os.path.join(raw_data_out, 'wine_quality.csv'), index=False)

if __name__ == '__main__':
    load_save_data()
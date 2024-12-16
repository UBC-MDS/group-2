# validate_raw_data.py
# Author: Zoe Ren
# 14 December 2024
# Run by following command: python /scripts/validate_raw_data.py --input-path "./data/raw/wine_quality.csv" --processed-data-path "./data/processed"

import os, sys
import click
import pandas as pd
import pandera as pa
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.data_validation import (
    create_directory, 
    validate_and_clean_data, 
    save_data)

from src.read_data import read_data

@click.command()
@click.option(
    "--input_path",
    default="./data/raw/wine_quality.csv",
    help="Path to the input CSV file.",
    type=click.Path(exists=True, dir_okay=False),
)
@click.option(
    "--processed_data_path",
    default="./data/processed",
    help="Path to save the processed data.",
    type=click.Path(file_okay=False),
)
def validate_raw_data(input_path, processed_data_path):
    """
    Script to validate and clean wine quality data.
    Data validation done by pandera before data splitting. 
    """
    # Make sure folder exists for output
    create_directory(processed_data_path)
    
    # Read the data
    print(f"Reading data from {input_path}...")
    raw_data = pd.read_csv(input_path)

    # Define the schema for validation
    schema = pa.DataFrameSchema(
        {
            "color": pa.Column(str, pa.Check.isin(["red", "white"])),
            "fixed_acidity": pa.Column(float, pa.Check.between(0, 16), nullable=True),
            "volatile_acidity": pa.Column(float, pa.Check.between(0, 1.8), nullable=True),
            "citric_acid": pa.Column(float, pa.Check.between(0, 1.4), nullable=True),
            "residual_sugar": pa.Column(float, pa.Check.between(0, 30), nullable=True),
            "chlorides": pa.Column(float, pa.Check.between(0, 0.7), nullable=True),
            "free_sulfur_dioxide": pa.Column(float, pa.Check.between(0, 160), nullable=True),
            "total_sulfur_dioxide": pa.Column(float, pa.Check.between(0, 400), nullable=True),
            "density": pa.Column(float, pa.Check.between(0, 1.5), nullable=True),
            "pH": pa.Column(float, pa.Check.between(0, 5), nullable=True),
            "sulphates": pa.Column(float, pa.Check.between(0, 2.5), nullable=True),
            "alcohol": pa.Column(float, pa.Check.between(9, 15), nullable=True),
            "quality": pa.Column(float, pa.Check.between(1, 10), nullable=True),
        },
        checks=[
            pa.Check(lambda df: ~df.duplicated().any(), error="Duplicate rows found."),
            pa.Check(lambda df: ~(df.isna().all(axis=1)).any(), error="Empty rows found."),
        ],
        drop_invalid_rows=True,
    )

    # Validate and clean the data
    print("Validating and cleaning data through pandera...")
    try:
        clean_data = validate_and_clean_data(raw_data, schema)
        print("Validation successful.")
    except pa.errors.SchemaErrors as e:
        print("Validation failed. Errors:")
        print(e.failure_cases)
        return

    # Save cleaned data
    output_file = os.path.join(processed_data_path, "cleaned_wine_quality.csv")
    save_data(clean_data, output_file)
    print(f"Processed data saved to {output_file}")
    print(f"Data validation is done.")


if __name__ == "__main__":
    validate_raw_data()

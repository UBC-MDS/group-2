import os
import pandas as pd
import pandera as pa


def create_directory(path):
    """
    Ensure a directory exists. If not, create it.

    Parameters
    ----------
    path (str): The path of the directory to create. If the directory already exists, no action is taken.

    Returns
    -------
    None

    """
    os.makedirs(path, exist_ok=True)


def read_data(input_path):
    """
    Read data from a CSV file.

    Parameters
    ----------
    input_path (str): The file path to the input CSV file. 

    Returns
    -------
    pandas.DataFrame: A DataFrame containing the contents of the CSV file.
    """
    return pd.read_csv(input_path)


def define_schema():
    """
    Define a Pandera schema for validating wine quality data.
    This schema enforces data types, acceptable ranges, and checks for duplicate or invalid rows.

    Parameters
    ----------
    None

    Returns
    -------
    pandera.DataFrameSchema: A schema object that can be used to validate a pandas DataFrame.

    Schema Rules:
        - Columns:
            - "color": Must be "red" or "white".
            - "fixed_acidity": Float values between 0 and 16 (nullable).
            - "volatile_acidity": Float values between 0 and 1.8 (nullable).
            - "citric_acid": Float values between 0 and 1.4 (nullable).
            - "residual_sugar": Float values between 0 and 30 (nullable).
            - "chlorides": Float values between 0 and 0.7 (nullable).
            - "free_sulfur_dioxide": Float values between 0 and 160 (nullable).
            - "total_sulfur_dioxide": Float values between 0 and 400 (nullable).
            - "density": Float values between 0 and 1.5 (nullable).
            - "pH": Float values between 0 and 5 (nullable).
            - "sulphates": Float values between 0 and 2.5 (nullable).
            - "alcohol": Float values between 9 and 15 (nullable).
            - "quality": Float values between 1 and 10 (nullable).
        - Additional Checks:
            - No duplicate rows allowed.
            - No rows with all columns as NaN allowed. 
    """
    return pa.DataFrameSchema(
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


def validate_and_clean_data(data, schema):
    """
    Validate and clean data using a Pandera schema.
    Any rows that fail the validation rules are dropped, along with duplicate and completely empty rows.

    Parameters
    ----------
    data (pandas.DataFrame): The input DataFrame to validate.
    schema (pandera.DataFrameSchema): The schema to validate the DataFrame against.
    
    Returns
    -------
    pandas.DataFrame: The validated and cleaned DataFrame.
    """
    return schema.validate(data, lazy=True).drop_duplicates().dropna(how="all")


def save_data(data, output_path):
    """
    Save cleaned data to a CSV file.

    Parameters
    ----------
    data (pandas.DataFrame): The DataFrame to save.
    output_path (str): The file path where the CSV file will be saved.

    Returns
    -------
    None
    """
    if data is None or data.empty:
        raise ValueError("The provided DataFrame is empty and cannot be saved.")
    data.to_csv(output_path, index=False)
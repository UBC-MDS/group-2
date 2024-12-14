import sys
import os
import pandas as pd
import pandera as pa
import pytest
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.data_validation import (
    create_directory, 
    read_data, 
    define_schema, 
    save_data)


def test_create_directory(tmp_path):
    """
    Test that the create_directory function successfully creates a directory.
    """
    path = tmp_path / "test_dir"  # Create a temporary directory path
    create_directory(path)  # Call the function to create the directory
    assert os.path.exists(path)  # Assert that the directory exists


def test_read_data(tmp_path):
    """
    Test that the read_data function reads a CSV file correctly.
    """
    # Create a temporary CSV file
    test_file = tmp_path / "test.csv"
    df = pd.DataFrame({"col1": [1, 2, 3]})
    df.to_csv(test_file, index=False)

    # Read the CSV file using the read_data function
    result = read_data(test_file)

    # Assert that the read DataFrame is equal to the original
    pd.testing.assert_frame_equal(result, df)

    # Test invalid input with pytest.raises
    with pytest.raises(ValueError):
        read_data(None)  # Pass invalid input to trigger a ValueError


def test_define_schema():
    """
    Test that the define_schema function returns a valid Pandera schema.
    """
    schema = define_schema()  # Call the function to define the schema
    assert isinstance(schema, pa.DataFrameSchema)  # Assert that the result is a Pandera schema


def test_save_data(tmp_path):
    """
    Test that the save_data function saves a DataFrame to a CSV file correctly.
    """
    # Create a sample DataFrame
    df = pd.DataFrame({"col1": [1, 2, 3]})
    output_file = tmp_path / "output.csv"  # Create a temporary output file path

    # Save the DataFrame using the save_data function
    save_data(df, output_file)

    # Assert that the output file exists
    assert os.path.exists(output_file)

    # Read the output file and assert it matches the input DataFrame
    result = pd.read_csv(output_file)
    pd.testing.assert_frame_equal(result, df)

    # Test invalid input with pytest.raises
    empty_df = pd.DataFrame()
    with pytest.raises(ValueError):
        save_data(empty_df, output_file)

    with pytest.raises(ValueError):
        save_data(None, output_file)  # Pass invalid input to trigger a ValueError

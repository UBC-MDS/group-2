# validate_training_data.py
# Author: Zoe Ren
# 7 December 2024
# Run by following command: python ./scripts/validate_training_data.py --input-path "./data/processed/training_set.csv" --output-path "./results"

import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import click
from deepchecks.tabular import Dataset
from deepchecks.tabular.checks import FeatureLabelCorrelation, FeatureFeatureCorrelation


@click.command()
@click.option(
    "--input-path",
    default="./data/processed/training_set.csv",
    help="Path to the training set CSV file.",
    type=click.Path(exists=True, dir_okay=False),
)
@click.option(
    "--output-path",
    default="./results",
    help="Path to save the results.",
    type=click.Path(file_okay=False),
)
def validate_training_data(input_path, output_path):
    """
    Script to validate training data and check correlations.
    Validate the raw data is step 1 of data validation done by pandera before data splitting. 
    Validate the training data is step 2 of data validation done by deepchecks after data splitting.
    Data info and data shape will be saved to output.
    """
    # Make sure the output folder exists
    os.makedirs(output_path, exist_ok=True)

    # Load data
    train_df = pd.read_csv(input_path)

    # Check data info and save
    print("# Check data info")
    info_output = os.path.join(output_path, "data_info.txt")
    with open(info_output, "w") as f:
        f.write(f"Training data shape: {train_df.shape}\n")
        f.write('-'*50 + "\n")
        train_df.info(buf=f)
    print(f"Data info saved to {info_output}")

    # Data description and save
    print("# Data description")
    description_output = os.path.join(output_path, "data_description.csv")
    train_df.describe().to_csv(description_output)
    print(f"Data description saved to {description_output}")

    # Perform DeepChecks
    print("# DeepCheck")

    # Create Dataset object
    train_ds = Dataset(train_df, label="quality", cat_features=["color"])

    # Check 1: Feature-Label correlations
    check_feat_lab = FeatureLabelCorrelation()
    feat_lab_result = check_feat_lab.run(dataset=train_ds)

    # Save feature-label correlation results
    feat_lab_output = os.path.join(output_path, "feature_label_correlation.json")
    feat_lab_result.value.to_json(feat_lab_output)
    print(f"Feature-Label Correlation saved to {feat_lab_output}")

    # Plot Feature-Label Correlation
    feat_lab_plot_path = os.path.join(output_path, "feature_label_correlation.png")
    feat_lab_result.value.plot(kind='bar', title='Feature-Label Correlation')
    plt.savefig(feat_lab_plot_path)
    print(f"Feature-Label Correlation plot saved to {feat_lab_plot_path}")
    plt.clf()

    # Check for correlations > 0.9 in feature-label relationships
    for feature, value in feat_lab_result.value.items():
        if abs(value) > 0.9:
            raise ValueError(f"Feature-Label correlation exceeds 0.9 for feature: {feature}")

    # Check 2: Feature-Feature correlations
    check_feat_feat = FeatureFeatureCorrelation()
    feat_feat_result = check_feat_feat.run(dataset=train_ds)

    # Save feature-feature correlation results
    correlation_matrix = feat_feat_result.value
    feat_feat_output = os.path.join(output_path, "feature_feature_correlation.csv")
    correlation_matrix.to_csv(feat_feat_output)
    print(f"Feature-Feature Correlation matrix saved to {feat_feat_output}")

    # Plot Feature-Feature Correlation Heatmap
    feat_feat_plot_path = os.path.join(output_path, "feature_feature_correlation_heatmap.png")
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm", cbar=True)
    plt.title("Feature-Feature Correlation Heatmap")
    plt.savefig(feat_feat_plot_path)
    print(f"Feature-Feature Correlation heatmap saved to {feat_feat_plot_path}")
    plt.clf()

    # Check for correlations > 0.9 in feature-feature relationships
    np.fill_diagonal(correlation_matrix.values, 0)  # Exclude diagonal
    if (np.abs(correlation_matrix) > 0.9).any().any():
        raise ValueError("Feature-Feature correlation exceeds the maximum acceptable threshold of 0.9")

    print("All correlation checks passed successfully!")


if __name__ == "__main__":
    validate_training_data()

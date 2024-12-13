import pandas as pd
import altair as alt
import os
import click
from src.eda_utils import (
    create_quality_distribution_plot,
    create_wine_quality_proportion_plot,
    create_sulfur_dioxide_scatter,
    create_correlation_matrix,
    create_boxplots_by_color,
    create_quality_distribution_bar
)

@click.command()
@click.argument("input_data", type=click.Path(exists=True))
@click.argument("output_dir", type=click.Path())
def eda(input_data, output_dir):
    """Perform exploratory data analysis on wine dataset.

    Parameters
    ----------
    input_data : str
        Path to input CSV file
    output_dir : str
        Directory to save output plots
    """
    # Create output dir if needed
    os.makedirs(output_dir, exist_ok=True)

    # Read data
    train_df = pd.read_csv(input_data)

    # Generate and save plots
    plots = {
        "dist_wine_scores_by_feature.png": create_quality_distribution_plot(train_df),
        "density_red_vs_white.png": create_wine_quality_proportion_plot(train_df),
        "total_vs_free_sulfur_dioxide.png": create_sulfur_dioxide_scatter(train_df),
        "feature_corrs.png": create_correlation_matrix(train_df),
        "red_vs_white_all_features.png": create_boxplots_by_color(train_df),
        "dist_wine_scores.png": create_quality_distribution_bar(train_df)
    }

    # Save all plots
    for filename, plot in plots.items():
        path = os.path.join(output_dir, filename)
        plot.save(path)
        print(f"Saved plot to {path}")

if __name__ == "__main__":
    eda()
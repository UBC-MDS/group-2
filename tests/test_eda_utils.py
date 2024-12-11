import pytest
import pandas as pd
import altair as alt
from src.eda_utils import (
    create_quality_distribution_plot,
    create_wine_quality_proportion_plot,
    create_sulfur_dioxide_scatter,
    create_correlation_matrix,
    create_boxplots_by_color,
    create_quality_distribution_bar
)

@pytest.fixture
def sample_wine_df():
    """Creates a sample wine DataFrame for testing.
    
    Returns
    -------
    pandas.DataFrame
        Sample wine data
    """
    return pd.DataFrame({
        'fixed_acidity': [7.4, 7.8, 7.3, 7.2],
        'volatile_acidity': [0.7, 0.88, 0.65, 0.71],
        'citric_acid': [0, 0, 0.1, 0.1],
        'quality': [5, 6, 7, 5],
        'color': ['red', 'white', 'red', 'white']
    })

def test_create_quality_distribution_plot(sample_wine_df):
    """Tests quality distribution plot creation."""
    plot = create_quality_distribution_plot(sample_wine_df)
    assert isinstance(plot, alt.Chart)
    
    with pytest.raises(TypeError):
        create_quality_distribution_plot([1, 2, 3])

def test_create_wine_quality_proportion_plot(sample_wine_df):
    """Tests wine quality proportion plot creation."""
    plot = create_wine_quality_proportion_plot(sample_wine_df)
    assert isinstance(plot, alt.Chart)
    
    with pytest.raises(ValueError):
        bad_df = sample_wine_df.drop(['color', 'quality'], axis=1)
        create_wine_quality_proportion_plot(bad_df)

def test_create_sulfur_dioxide_scatter(sample_wine_df):
    """Tests sulfur dioxide scatter plot creation."""
    plot = create_sulfur_dioxide_scatter(sample_wine_df)
    assert isinstance(plot, alt.Chart)
    
    with pytest.raises(ValueError):
        bad_df = sample_wine_df.drop(['free_sulfur_dioxide', 'total_sulfur_dioxide'], axis=1)
        create_sulfur_dioxide_scatter(bad_df)

def test_create_correlation_matrix(sample_wine_df):
    """Tests correlation matrix plot creation."""
    plot = create_correlation_matrix(sample_wine_df)
    assert isinstance(plot, alt.Chart)
    
    with pytest.raises(TypeError):
        create_correlation_matrix([1, 2, 3])

def test_create_boxplots_by_color(sample_wine_df):
    """Tests boxplots creation for wine features."""
    plot = create_boxplots_by_color(sample_wine_df)
    assert isinstance(plot, alt.VConcatChart)
    
    with pytest.raises(ValueError):
        bad_df = sample_wine_df.drop('color', axis=1)
        create_boxplots_by_color(bad_df)

def test_create_quality_distribution_bar(sample_wine_df):
    """Tests quality distribution bar chart creation."""
    plot = create_quality_distribution_bar(sample_wine_df)
    assert isinstance(plot, alt.Chart)
    
    with pytest.raises(ValueError):
        bad_df = sample_wine_df.drop('quality', axis=1)
        create_quality_distribution_bar(bad_df)
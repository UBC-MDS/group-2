import pandas as pd
import altair as alt
import altair_ally as aly

def create_quality_distribution_plot(df, color_column='quality'):
    """Creates a distribution plot for wine quality scores.
    
    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame containing wine features
    color_column : str
        Column for coloring (default: quality)
        
    Returns
    -------
    altair.Chart
        Distribution plot
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("df must be a DataFrame")
        
    aly.alt.data_transformers.enable('vegafusion')
    return aly.dist(df, color=color_column)

def create_wine_quality_proportion_plot(df):
    """Creates a line plot showing quality score proportions by wine color."""
    if 'color' not in df.columns or 'quality' not in df.columns:
        raise ValueError("Missing required columns")

    # Calculate proportions
    props = (df.groupby(['color', 'quality'])
             .size()
             .reset_index(name='count'))
    props['proportion'] = props.groupby('color')['count'].transform(lambda x: x/x.sum())

    # Create plot
    chart = alt.Chart(props).mark_line(
        point=True,
        tension=0.7,
        strokeWidth=2
    ).encode(
        x=alt.X('quality:Q', title='Quality Score'),
        y=alt.Y('proportion:Q', 
                axis=alt.Axis(format='.0%'),
                title='Proportion of Wines'),
        color=alt.Color('color:N', 
                       scale=alt.Scale(domain=['red', 'white']),
                       title='Wine Color')
    ).properties(
        width=500,
        height=300,
        title='Wine Quality Distribution by Color'
    )
    
    return chart

def create_correlation_matrix(df):
    """Creates a correlation matrix visualization for numerical features.
    
    Parameters
    ----------
    df : pandas.DataFrame
        Wine feature data
        
    Returns
    -------
    altair.Chart
        Correlation matrix plot
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("df must be a DataFrame")
    
    return aly.corr(df)

def create_sulfur_dioxide_scatter(df, sample_size=None):
    """Creates a scatter plot for sulfur dioxide measurements."""
    if not isinstance(df, pd.DataFrame):
        raise TypeError("df must be a DataFrame")
        
    if sample_size is not None:
        if not isinstance(sample_size, int) or sample_size <= 0:
            raise ValueError("sample_size must be a positive integer")
        if sample_size < len(df):
            import warnings
            warnings.warn(f"Sampling {sample_size} points from {len(df)} total points")
    
    cols = ['free_sulfur_dioxide', 'total_sulfur_dioxide']
    plot_df = df[cols].sample(sample_size) if sample_size else df[cols]
    
    base = alt.Chart(plot_df).properties(
        width=500,
        height=300
    )
    
    points = base.mark_circle(size=60).encode(
        x=alt.X('free_sulfur_dioxide', title='Free Sulfur Dioxide'),
        y=alt.Y('total_sulfur_dioxide', title='Total Sulfur Dioxide')
    )
    
    line = base.mark_line(color='red', size=2).encode(
        x='free_sulfur_dioxide',
        y='total_sulfur_dioxide'
    ).transform_regression('free_sulfur_dioxide', 'total_sulfur_dioxide')
    
    return points + line

def create_boxplots_by_color(df):
    """Creates box plots for numerical features grouped by wine color.
    
    Parameters
    ----------
    df : pandas.DataFrame
        Wine data with 'color' column
        
    Returns
    -------
    altair.Chart
        Grid of box plots
    """
    if 'color' not in df.columns:
        raise ValueError("Missing 'color' column")

    # Get numerical columns except the target variable
    num_cols = df.select_dtypes(include=['float64', 'int64']).columns
    num_cols = [col for col in num_cols if col != 'quality']

    # Create box plots
    plots = []
    for col in num_cols:
        plot = alt.Chart(df).mark_boxplot().encode(
            x=alt.X(col + ':Q', scale=alt.Scale(zero=False)),
            y='color:N',
            color='color:N'
        ).properties(
            title=col,
            width=250,
            height=80
        )
        plots.append(plot)

    return alt.vconcat(*[alt.hconcat(*plots[i:i + 2]) for i in range(0, len(plots), 2)])

def create_quality_distribution_bar(df):
    """Creates a bar chart showing wine quality score distribution.
    
    Parameters
    ----------
    df : pandas.DataFrame
        Wine data with 'quality' column
        
    Returns
    -------
    altair.Chart
        Bar chart
    """
    if 'quality' not in df.columns:
        raise ValueError("Missing 'quality' column")

    # Calculate quality distribution
    quality_counts = df['quality'].value_counts()
    plot_df = pd.DataFrame({
        'quality': quality_counts.index,
        'percentage': (quality_counts.values / len(df) * 100).round(1)
    }).sort_values('quality')

    # Create bar chart
    return alt.Chart(plot_df).mark_bar().encode(
        x='quality:O',
        y='percentage:Q',
        tooltip=['quality:O', alt.Tooltip('percentage:Q', format='.1f')]
    ).properties(
        width=350,
        height=200,
        title='Wine Quality Distribution'
    )
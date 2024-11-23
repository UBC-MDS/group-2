# Title:
Analysis of Wine Quality and Prediction Using Logistic Regression

# Contributors:
Alix, Paramveer, Susannah, Zoe

# Project Summary:
This project aims to analyze and predict the quality of wine based on various physicochemical properties. Using the UCI Wine Quality dataset, we conduct data preprocessing, exploratory data analysis, and build machine learning models to predict wine quality. The dataset includes multiple features, such as acidity, alcohol content, and sugar levels, which are critical in determining the quality score of wines. The project utilizes cross-validation and hyperparameter tuning to optimize model performance.

# Data Analysis:
Dataset:
The dataset was sourced from the UCI Machine Learning Repository.

Preprocessing:
Standardization of numerical features.
One-hot encoding for binary categorical features (e.g., color).

Exploratory Data Analysis:
Distribution of wine quality scores.
Correlation heatmaps to identify relationships between features.
Key insights on influential features.

Modeling:
Logistic regression was used as the base model.
RandomizedSearchCV was applied for hyperparameter optimization.
The model was evaluated using metrics such as accuracy, precision, recall, and F1-score.

# List of Dependencies:
- `conda` (version 24.9.1 or higher)
- `conda-lock` (version 2.5.7 or higher)
- Python package `ucimlrepo` (version 0.0.7)
- `jupyterlab` (version 4.2.0 or higher)
- `nb_conda_kernels` (version 2.5.1 or higher)
- Python and packages listed in [`environment.yml`](https://github.com/UBC-MDS/group-2/blob/main/environment.yml)
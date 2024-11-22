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
channels:
  - conda-forge
  - pytorch
  - anaconda
  - plotly
  - defaults
dependencies:
  - python=3.12.0
  - pandas=2.2.3
  - numpy=1.26.4
  - scikit-learn=1.5.2
  - altair=5.4.1
  - jupyterlab=4.2.6
  - jupyterlab_server=2.27.3
  - jupyter_server=2.14.2
  - jupyter_core=5.7.2
  - jupyter_client=8.6.3
  - ipykernel=6.29.5
  - nb_conda_kernels=2.5.1
  - matplotlib=3.9.2
  - scipy=1.14.1
  - vega_datasets
  - graphviz
  - python-graphviz
  - eli5
  - shap
  - jinja2
  - lightgbm
  - spacy
  - xgboost
  - catboost
  - nltk
  - imbalanced-learn
  - torchvision
  - torchaudio
  - pytorch
  - autograd
  - plotly
  - panel
  - watchfiles
  - wikipedia
  - requests
  - pip=24.3.1
  - vl-convert-python>=1.6.0
  - pip:
    - altair-ally>=0.1.1
    - ucimlrepo==0.0.7
    - vegafusion==1.6.9
    - vegafusion-python-embed==1.6.9
    - mglearn
    - spacymoji
    - otter-grader>=6.0
    - transformers
    - datasets
    - ultralytics
    - psutil>=5.7.2
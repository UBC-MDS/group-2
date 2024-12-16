import click
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.data_validation import save_data
from src.find_best_model import find_best_model
from src.read_data import read_data

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression

import scipy.stats as stats

from sklearn.metrics import accuracy_score


import warnings
warnings.filterwarnings('ignore', category=FutureWarning)

@click.command()
@click.option('--training_data', type=str, help="Path to training data")
@click.option('--test_data', type=str, help="Path to test data")
@click.option('--results_to', type=str, help="Path to directory where the model's best parameter and accuracy score will be written to")
@click.option('--plots_to', type=str, help="Path to directory where the model's analysis plots will be written to")
@click.option('--model_to', type=str, help='Path to directory where the tuned model is stored')
@click.option('--seed', type=int, help="Random seed", default=522)
def model_and_result(training_data, test_data, results_to, plots_to, model_to, seed):
    '''Fits a wine quality logistic regression model to the training data 
    and evaluates the model on the test data with accuracy score.'''
    np.random.seed(seed)

    # Read in training and test data
    train_df = read_data(training_data)
    test_df = read_data(test_data)

    os.makedirs(results_to, exist_ok=True)
    os.makedirs(plots_to, exist_ok=True)
    os.makedirs(model_to, exist_ok=True)

    # Split dataset
    X_train, X_test, y_train, y_test = (train_df.drop(columns='quality'), test_df.drop(columns='quality'),
                                        train_df['quality'], test_df['quality']
                                        )
    
    numeric_features = X_train.select_dtypes(include='number').columns.tolist()
    binary_features = ['color']
    
    # Make column transformer
    preprocessor = make_column_transformer(
        (OneHotEncoder(drop='if_binary'), binary_features),
        (StandardScaler(), numeric_features)
    )
    
    # Make pipeline using StandardScaler and LogisticRegression
    model = make_pipeline(
        preprocessor,
        LogisticRegression(multi_class='multinomial', solver='lbfgs', max_iter=2000)
    )

    # Find best performing model through randomized search and fit it using X_train and y_train
    random_search = find_best_model(X_train, y_train, model, stats.uniform(0.001, 100), 3, 50, 'accuracy', 42)

    # Save the tuned model to output location
    model_path = os.path.join(model_to, 'tuned_model.pickle')

    with open(model_path, 'wb') as f:
        pickle.dump(random_search, f)
        print(f'Tunded model output to {model_path}')

    # Best parameters
    print("Best Parameters:", random_search.best_params_)

    # Evaluate
    y_pred = random_search.predict(X_test)
    test_acc = accuracy_score(y_test, y_pred)

    # Save best parameter and accuracy scores
    model_results = pd.DataFrame({'best_C': [random_search.best_params_['logisticregression__C']], 'accuracy': [test_acc]})
    output_file = os.path.join(results_to, "model_results.csv")
    save_data(model_results, output_file)

    # Plot bar graphs for Logistic Regression coefficients
    logreg = random_search.best_estimator_.named_steps['logisticregression']
    coefficients = logreg.coef_
    class_labels = logreg.classes_
    for i, class_label in enumerate(class_labels):
        plt.figure(figsize=(10, 6))
        sorted_indices = np.argsort(coefficients[i])
        sorted_features = np.array(list(X_train))[sorted_indices]
        sorted_coefs = coefficients[i][sorted_indices]

        plt.barh(sorted_features, sorted_coefs, color='skyblue')
        plt.xlabel('Coefficient Value')
        plt.ylabel('Feature')
        plt.title(f'Feature Coefficients for Wine Quality {class_label}')
        plt.tight_layout()

        # Save the plot
        filename = f'wine_quality_{class_label}_coefficients.png'
        filepath = os.path.join(plots_to, filename)
        plt.savefig(filepath, dpi=300)
        plt.close()

        print(f"Plot saved as {filepath}")

if __name__ == '__main__':
    model_and_result()
# -



import sklearn, numpy
import pandas as pd
from sklearn.model_selection import RandomizedSearchCV

def find_best_model(X_train, y_train, model, range, cv, n_iter, scoring_metric, seed=None):
    """Finds the best C parameter for Logistic Regression within a pipeline and return the pipeline
    
    Parameters
    ----------
    X_train : pd.DataFrame
        Training set feature values as a dataframe to fit tuned model on
    y_train: pd.Series
        Target variable values of the training set
    model : sklearn.pipeline.Pipeline
        Pipeline containing logistic regression
    range : numpy.array or scipy.stats.uniform
        Values of C to search from
    cv : int
        Number of folds in cross-validation when doing random search
    n_iter : int
        Number of total search iterations to perform
    scoring_metric : str
        Metric to evaluate the model on when doing random search
    seed : int
        Number to determine random state of RandomizedSearchCV (for reproducible results)
        
    Returns
    -------
    sklearn.model_selection.RandomizedSearchCV
        RandomizedSearchCV object after being tuned on C value of Logistic Regression and fitted on X_train, y_train
    """
    if not isinstance(X_train, pd.DataFrame):
        raise TypeError("X_train must be a pandas data frame")
    
    if not isinstance(y_train, pd.Series):
        raise TypeError("X_train must be a pandas series")
    
    if not isinstance(model, sklearn.pipeline.Pipeline):
        raise TypeError("model must be a sklearn Pipeline")
    
    if (not isinstance(range, numpy.ndarray) and not hasattr(range, "rvs")):
        raise TypeError("range must be a numpy array or scipy.stats.rv_continuous object")
    
    if not isinstance(cv, int):
        raise TypeError("cv must be an integer")
    
    if not isinstance(n_iter, int):
        raise TypeError("n_iter must be an integer")
    
    if not isinstance(scoring_metric, str):
        raise TypeError("scoring_metric must be a string")
    
    if not isinstance(seed, int):
        raise TypeError("seed must be an integer")
        
    tuned_model = RandomizedSearchCV(model, param_distributions={'logisticregression__C': range},
                                       cv=cv,
                                       n_iter=n_iter,
                                       scoring=scoring_metric,
                                       random_state=seed)
    tuned_model.fit(X_train, y_train)
    return tuned_model

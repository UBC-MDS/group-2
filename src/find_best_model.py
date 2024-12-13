import sklearn, numpy, scipy
from sklearn.model_selection import RandomizedSearchCV

def find_best_model(model, range, cv, n_iter, scoring_metric, seed=None):
    """Finds the best C parameter for Logistic Regression within a pipeline and return the pipeline
    
    Parameters
    ----------
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
    sklearn.pipeline.Pipeline
        Pipeline containing the best performing Logistic Regression tuned on C
    """
    if not isinstance(model, sklearn.pipeline.Pipeline):
        raise TypeError("model must be a sklearn Pipeline")
    
    if (not isinstance(range, numpy.ndarray) and not isinstance(range, type(scipy.stats.uniform))):
        raise TypeError("range must be a numpy array or scipy.stats.uniform object")
    
    if not isinstance(cv, int):
        raise TypeError("cv must be an integer")
    
    if not isinstance(n_iter, int):
        raise TypeError("n_iter must be an integer")
    
    if not isinstance(scoring_metric, str):
        raise TypeError("scoring_metric must be a string")
    
    if not isinstance(n_iter, int):
        raise TypeError("seed must be an integer")
        
    return RandomizedSearchCV(model, param_distributions={'logisticregression__C': range},
                                       cv=cv,
                                       n_iter=n_iter,
                                       scoring=scoring_metric,
                                       random_state=seed)

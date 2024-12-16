# Issues Addressed from Feedback and Peer Review

Note: We found there are many duplicated issues mentioned by multiple peer reviewers, including but not limited to: including author full names, plot image size adjustments, elaboration on interpretation of model results, and explanation of why further machine learing methods were not tried despite low accuracy score from the model. We have listed below changes based on the unique reviews we have received for conciseness and clarity.

## Expand on model results analysis and conclusion

This issue was based on Milestone 1 instuctor feedback and 3 unique peer reviews.

By adding plots showing Logistic Regression coefficients across 7 wine quality score classes, we reinstate the potential lack of linearity in the problem as it is currently presented, given existing features. We clarified reasons why we are hesitant to apply further machine learning methods, such as including F1, recall scores, or choosing a different, non-linear model, as we need better understanding of the data and what factors contribute to wine quality for red and white wines in real life. Without such understanding, we might incur risks of creating less effective features / models or increase possibilities of overfitting in the future.

[Changes can be found in this commit.](https://github.com/UBC-MDS/wine-quality-regressor-group-2/commit/83f242190b96a2b6cd2269380d224060fba22619)

## Add bar plots to show coefficients found by logistic regression

This issue was based on a unique peer review.

We added bar plots showing feature coefficients from logistic regression for each wine quality class, generated png files in appropriate directory, and updated scripts and Makefile.

[Changes can be found in this commit.](https://github.com/UBC-MDS/wine-quality-regressor-group-2/commit/e57f3f91fc2f6178ab918765ff792ebc7202990a)

## Remove commented code in model_and_results.py

This issue was based on a unique peer review.

[Changes can be found in this commit.](https://github.com/UBC-MDS/wine-quality-regressor-group-2/commit/64ea5df99d77b40d095f081705712fdd41f6db7d)

## Include author full names instead of first names only

This issue was based on a unique peer review.

[Changes can be found in this commit.](https://github.com/UBC-MDS/wine-quality-regressor-group-2/commit/e4c8b3ba198df9152ee66ebf02696874ac785b5a)

## Add hyperlink to CONTRIBUTING.md in README(Zoe Ren-sgdkd)

This issue was based on a unique peer review.

I add hyperlink for license and contributing files.

[Changes can be found in this commit.](https://github.com/UBC-MDS/wine-quality-regressor-group-2/commit/2becbaf6902d36735200d0f4ed479eeac56272e0)

## Explain features(Zoe Ren-sgdkd)

This issue was based on a unique peer review.

I add a Variable section to explain the features.

[Changes can be found in this commit.](https://github.com/UBC-MDS/wine-quality-regressor-group-2/commit/4998937fd7f9dc89ea8ebcbab1c71a362d1ee349)

## State research question(Zoe Ren-sgdkd)

This issue was based on a unique peer review.

I add a Core Hypothesis section to clearly state the research question.

[Changes can be found in this commit.](https://github.com/UBC-MDS/wine-quality-regressor-group-2/commit/89a5bea59c14b052789c6203d7a357688bfae76b)

## 'Why is it important'(Zoe Ren-sgdkd)

This issue was based on a unique peer review.

I add a Importance section to explain the importance of this model.

[Changes can be found in this commit.](https://github.com/UBC-MDS/wine-quality-regressor-group-2/commit/bf1f01c7c855d1f202f33352c2ae37702e121728)

## Save model as pickle

This issue was based on a unique peer review.

The reviewer suggested saving the final tuned model as a pickle file and changes were made so that our script saves this model in `results/models/` directory for use by another user.

[Changes can be found in this commit.](https://github.com/UBC-MDS/wine-quality-regressor-group-2/commit/4026d568c9934c242b83af4c39d25017d02bc254)

## Reorganize boxplots for easier viewing

This issue was based on a unique peer review.

It was suggested that the number of columns presented in the boxplots comparing the
distributions of the various numerical features between the two types of wines to be reduced from three to two columns.

[Changes can be found in this commit.](https://github.com/UBC-MDS/wine-quality-regressor-group-2/commit/788af37afba3339024771c16093d87b6ef6dbf4d)

## Make plots more human-readable

This issue was based on a unique peer review.

The reviewer mentioned the axes of the plots should be more human-readable. Some of the plots were changed to have better axis titles and titles; however, this could not
be done for all of the plots due to the nature of their generation using Altair Ally. We might look into removing the underscores in feature names in the future if we decide to further improve the project.

[Changes can be found in this commit.](https://github.com/UBC-MDS/wine-quality-regressor-group-2/commit/f6dbdfa6882a2cf1fa0eab2732dadb147819fb01)

## Issues we did not choose to address

Below are several issues we did not address given the limited length of our project duration. However, they do provide value for improvements, and if we choose to continue to work on this project in the future, we would consider addressing them at that point.

### Make a Github page for the report

Since our current README.md links to our PDF report which is relatively readable for human eyes, we are leaving this issue unaddressed for now.

### Numbering scripts in `scripts` directory

Since there are only 5 scripts, we think it is okay to leave them as is. If there are additional scripts added in the future, numbering them may be a good idea to keep scripts more organized.
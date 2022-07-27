# Summary of 10_RandomForest_GoldenFeatures

[<< Go back](../README.md)


## Random Forest
- **n_jobs**: -1
- **criterion**: gini
- **max_features**: 0.7
- **min_samples_split**: 30
- **max_depth**: 7
- **eval_metric_name**: logloss
- **num_class**: 5
- **explain_level**: 1

## Validation
 - **validation_type**: split
 - **train_ratio**: 0.9
 - **shuffle**: True
 - **stratify**: True

## Optimized metric
logloss

## Training time

4.1 seconds

### Metric details
|           |   0 |         1 |         2 |        3 |         4 |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|----:|----------:|----------:|---------:|----------:|-----------:|------------:|---------------:|----------:|
| precision |   0 |  0.4      |  0.454545 | 0.333333 |  0.727273 |   0.474576 |    0.38303  |       0.444992 |   1.22514 |
| recall    |   0 |  0.470588 |  0.588235 | 0.222222 |  0.666667 |   0.474576 |    0.389542 |       0.474576 |   1.22514 |
| f1-score  |   0 |  0.432432 |  0.512821 | 0.266667 |  0.695652 |   0.474576 |    0.381514 |       0.454528 |   1.22514 |
| support   |   4 | 17        | 17        | 9        | 12        |   0.474576 |   59        |      59        |   1.22514 |


## Confusion matrix
|              |   Predicted as 0 |   Predicted as 1 |   Predicted as 2 |   Predicted as 3 |   Predicted as 4 |
|:-------------|-----------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| Labeled as 0 |                0 |                4 |                0 |                0 |                0 |
| Labeled as 1 |                0 |                8 |                7 |                0 |                2 |
| Labeled as 2 |                0 |                6 |               10 |                1 |                0 |
| Labeled as 3 |                0 |                2 |                4 |                2 |                1 |
| Labeled as 4 |                0 |                0 |                1 |                3 |                8 |

## Learning curves
![Learning curves](learning_curves.png)

## Permutation-based Importance
![Permutation-based Importance](permutation_importance.png)
## Confusion Matrix

![Confusion Matrix](confusion_matrix.png)


## Normalized Confusion Matrix

![Normalized Confusion Matrix](confusion_matrix_normalized.png)


## ROC Curve

![ROC Curve](roc_curve.png)


## Precision Recall Curve

![Precision Recall Curve](precision_recall_curve.png)



[<< Go back](../README.md)

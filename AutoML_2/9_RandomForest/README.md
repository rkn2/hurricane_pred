# Summary of 9_RandomForest

[<< Go back](../README.md)


## Random Forest
- **n_jobs**: -1
- **criterion**: gini
- **max_features**: 0.5
- **min_samples_split**: 20
- **max_depth**: 4
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

2.3 seconds

### Metric details
|           |   0 |         1 |         2 |        3 |         4 |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|----:|----------:|----------:|---------:|----------:|-----------:|------------:|---------------:|----------:|
| precision |   0 |  0.470588 |  0.384615 | 0.428571 |  0.666667 |   0.457627 |    0.390088 |       0.447383 |    1.2795 |
| recall    |   0 |  0.470588 |  0.588235 | 0.333333 |  0.5      |   0.457627 |    0.378431 |       0.457627 |    1.2795 |
| f1-score  |   0 |  0.470588 |  0.465116 | 0.375    |  0.571429 |   0.457627 |    0.376427 |       0.443036 |    1.2795 |
| support   |   4 | 17        | 17        | 9        | 12        |   0.457627 |   59        |      59        |    1.2795 |


## Confusion matrix
|              |   Predicted as 0 |   Predicted as 1 |   Predicted as 2 |   Predicted as 3 |   Predicted as 4 |
|:-------------|-----------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| Labeled as 0 |                0 |                1 |                3 |                0 |                0 |
| Labeled as 1 |                0 |                8 |                8 |                1 |                0 |
| Labeled as 2 |                0 |                4 |               10 |                1 |                2 |
| Labeled as 3 |                0 |                3 |                2 |                3 |                1 |
| Labeled as 4 |                0 |                1 |                3 |                2 |                6 |

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

# Summary of 8_LightGBM

[<< Go back](../README.md)


## LightGBM
- **n_jobs**: -1
- **objective**: multiclass
- **num_leaves**: 95
- **learning_rate**: 0.05
- **feature_fraction**: 1.0
- **bagging_fraction**: 1.0
- **min_data_in_leaf**: 10
- **metric**: multi_logloss
- **custom_eval_metric_name**: None
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

5.7 seconds

### Metric details
|           |   0 |         1 |         2 |        3 |         4 |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|----:|----------:|----------:|---------:|----------:|-----------:|------------:|---------------:|----------:|
| precision |   0 |  0.52381  |  0.4375   | 0.3      |  0.666667 |   0.491525 |    0.385595 |       0.458343 |   1.30672 |
| recall    |   0 |  0.647059 |  0.411765 | 0.333333 |  0.666667 |   0.491525 |    0.411765 |       0.491525 |   1.30672 |
| f1-score  |   0 |  0.578947 |  0.424242 | 0.315789 |  0.666667 |   0.491525 |    0.397129 |       0.472819 |   1.30672 |
| support   |   4 | 17        | 17        | 9        | 12        |   0.491525 |   59        |      59        |   1.30672 |


## Confusion matrix
|              |   Predicted as 0 |   Predicted as 1 |   Predicted as 2 |   Predicted as 3 |   Predicted as 4 |
|:-------------|-----------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| Labeled as 0 |                0 |                1 |                1 |                1 |                1 |
| Labeled as 1 |                0 |               11 |                4 |                1 |                1 |
| Labeled as 2 |                0 |                6 |                7 |                2 |                2 |
| Labeled as 3 |                0 |                2 |                4 |                3 |                0 |
| Labeled as 4 |                0 |                1 |                0 |                3 |                8 |

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

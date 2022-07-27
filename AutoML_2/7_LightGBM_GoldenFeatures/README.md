# Summary of 7_LightGBM_GoldenFeatures

[<< Go back](../README.md)


## LightGBM
- **n_jobs**: -1
- **objective**: multiclass
- **num_leaves**: 63
- **learning_rate**: 0.05
- **feature_fraction**: 0.9
- **bagging_fraction**: 1.0
- **min_data_in_leaf**: 20
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

2.9 seconds

### Metric details
|           |   0 |         1 |         2 |        3 |     4 |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|----:|----------:|----------:|---------:|------:|-----------:|------------:|---------------:|----------:|
| precision |   0 |  0.434783 |  0.5      | 0.285714 |  0.75 |   0.491525 |    0.394099 |       0.46547  |    1.2152 |
| recall    |   0 |  0.588235 |  0.470588 | 0.222222 |  0.75 |   0.491525 |    0.406209 |       0.491525 |    1.2152 |
| f1-score  |   0 |  0.5      |  0.484848 | 0.25     |  0.75 |   0.491525 |    0.39697  |       0.474448 |    1.2152 |
| support   |   4 | 17        | 17        | 9        | 12    |   0.491525 |   59        |      59        |    1.2152 |


## Confusion matrix
|              |   Predicted as 0 |   Predicted as 1 |   Predicted as 2 |   Predicted as 3 |   Predicted as 4 |
|:-------------|-----------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| Labeled as 0 |                0 |                2 |                2 |                0 |                0 |
| Labeled as 1 |                1 |               10 |                4 |                1 |                1 |
| Labeled as 2 |                0 |                5 |                8 |                2 |                2 |
| Labeled as 3 |                0 |                6 |                1 |                2 |                0 |
| Labeled as 4 |                0 |                0 |                1 |                2 |                9 |

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

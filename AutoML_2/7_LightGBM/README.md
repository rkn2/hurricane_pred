# Summary of 7_LightGBM

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
|           |   0 |         1 |         2 |        3 |         4 |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|----:|----------:|----------:|---------:|----------:|-----------:|------------:|---------------:|----------:|
| precision |   0 |  0.434783 |  0.533333 | 0.333333 |  0.692308 |   0.491525 |    0.398751 |       0.470604 |   1.21232 |
| recall    |   0 |  0.588235 |  0.470588 | 0.222222 |  0.75     |   0.491525 |    0.406209 |       0.491525 |   1.21232 |
| f1-score  |   0 |  0.5      |  0.5      | 0.266667 |  0.72     |   0.491525 |    0.397333 |       0.475254 |   1.21232 |
| support   |   4 | 17        | 17        | 9        | 12        |   0.491525 |   59        |      59        |   1.21232 |


## Confusion matrix
|              |   Predicted as 0 |   Predicted as 1 |   Predicted as 2 |   Predicted as 3 |   Predicted as 4 |
|:-------------|-----------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| Labeled as 0 |                0 |                2 |                1 |                0 |                1 |
| Labeled as 1 |                2 |               10 |                3 |                1 |                1 |
| Labeled as 2 |                0 |                6 |                8 |                1 |                2 |
| Labeled as 3 |                0 |                5 |                2 |                2 |                0 |
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

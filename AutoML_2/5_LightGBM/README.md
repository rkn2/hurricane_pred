# Summary of 5_LightGBM

[<< Go back](../README.md)


## LightGBM
- **n_jobs**: -1
- **objective**: multiclass
- **num_leaves**: 15
- **learning_rate**: 0.05
- **feature_fraction**: 0.8
- **bagging_fraction**: 0.5
- **min_data_in_leaf**: 50
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

3.8 seconds

### Metric details
|           |   0 |         1 |         2 |        3 |         4 |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|----:|----------:|----------:|---------:|----------:|-----------:|------------:|---------------:|----------:|
| precision |   0 |  0.473684 |  0.615385 | 0.416667 |  0.642857 |   0.525424 |    0.429719 |       0.508109 |   1.20088 |
| recall    |   0 |  0.529412 |  0.470588 | 0.555556 |  0.75     |   0.525424 |    0.461111 |       0.525424 |   1.20088 |
| f1-score  |   0 |  0.5      |  0.533333 | 0.47619  |  0.692308 |   0.525424 |    0.440366 |       0.511188 |   1.20088 |
| support   |   4 | 17        | 17        | 9        | 12        |   0.525424 |   59        |      59        |   1.20088 |


## Confusion matrix
|              |   Predicted as 0 |   Predicted as 1 |   Predicted as 2 |   Predicted as 3 |   Predicted as 4 |
|:-------------|-----------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| Labeled as 0 |                0 |                2 |                0 |                1 |                1 |
| Labeled as 1 |                1 |                9 |                3 |                2 |                2 |
| Labeled as 2 |                0 |                6 |                8 |                1 |                2 |
| Labeled as 3 |                0 |                2 |                2 |                5 |                0 |
| Labeled as 4 |                0 |                0 |                0 |                3 |                9 |

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

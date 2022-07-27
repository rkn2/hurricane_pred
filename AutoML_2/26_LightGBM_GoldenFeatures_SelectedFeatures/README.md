# Summary of 26_LightGBM_GoldenFeatures_SelectedFeatures

[<< Go back](../README.md)


## LightGBM
- **n_jobs**: -1
- **objective**: multiclass
- **num_leaves**: 15
- **learning_rate**: 0.05
- **feature_fraction**: 0.5
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

2.9 seconds

### Metric details
|           |   0 |         1 |         2 |        3 |         4 |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|----:|----------:|----------:|---------:|----------:|-----------:|------------:|---------------:|----------:|
| precision |   0 |  0.5      |  0.75     | 0.454545 |  0.714286 |   0.576271 |    0.483766 |       0.574785 |   1.14142 |
| recall    |   0 |  0.588235 |  0.529412 | 0.555556 |  0.833333 |   0.576271 |    0.501307 |       0.576271 |   1.14142 |
| f1-score  |   0 |  0.540541 |  0.62069  | 0.5      |  0.769231 |   0.576271 |    0.486092 |       0.567317 |   1.14142 |
| support   |   4 | 17        | 17        | 9        | 12        |   0.576271 |   59        |      59        |   1.14142 |


## Confusion matrix
|              |   Predicted as 0 |   Predicted as 1 |   Predicted as 2 |   Predicted as 3 |   Predicted as 4 |
|:-------------|-----------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| Labeled as 0 |                0 |                2 |                0 |                1 |                1 |
| Labeled as 1 |                2 |               10 |                2 |                2 |                1 |
| Labeled as 2 |                0 |                6 |                9 |                1 |                1 |
| Labeled as 3 |                0 |                2 |                1 |                5 |                1 |
| Labeled as 4 |                0 |                0 |                0 |                2 |               10 |

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

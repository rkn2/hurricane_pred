# Summary of 29_RandomForest_GoldenFeatures_SelectedFeatures

[<< Go back](../README.md)


## Random Forest
- **n_jobs**: -1
- **criterion**: entropy
- **max_features**: 0.7
- **min_samples_split**: 40
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

0.9 seconds

### Metric details
|           |   0 |         1 |         2 |        3 |    4 |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|----:|----------:|----------:|---------:|-----:|-----------:|------------:|---------------:|----------:|
| precision |   0 |  0.4      |  0.526316 | 0.333333 |  0.5 |   0.457627 |    0.35193  |       0.419447 |   1.20157 |
| recall    |   0 |  0.588235 |  0.588235 | 0.111111 |  0.5 |   0.457627 |    0.357516 |       0.457627 |   1.20157 |
| f1-score  |   0 |  0.47619  |  0.555556 | 0.166667 |  0.5 |   0.457627 |    0.339683 |       0.424401 |   1.20157 |
| support   |   4 | 17        | 17        | 9        | 12   |   0.457627 |   59        |      59        |   1.20157 |


## Confusion matrix
|              |   Predicted as 0 |   Predicted as 1 |   Predicted as 2 |   Predicted as 3 |   Predicted as 4 |
|:-------------|-----------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| Labeled as 0 |                0 |                4 |                0 |                0 |                0 |
| Labeled as 1 |                0 |               10 |                5 |                0 |                2 |
| Labeled as 2 |                0 |                5 |               10 |                0 |                2 |
| Labeled as 3 |                0 |                5 |                1 |                1 |                2 |
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

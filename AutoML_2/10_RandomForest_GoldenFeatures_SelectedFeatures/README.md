# Summary of 10_RandomForest_GoldenFeatures_SelectedFeatures

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

1.0 seconds

### Metric details
|           |   0 |         1 |         2 |        3 |         4 |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|----:|----------:|----------:|---------:|----------:|-----------:|------------:|---------------:|----------:|
| precision |   0 |  0.5      |  0.526316 | 0.5      |  0.5      |   0.508475 |    0.405263 |       0.473684 |   1.20007 |
| recall    |   0 |  0.529412 |  0.588235 | 0.444444 |  0.583333 |   0.508475 |    0.429085 |       0.508475 |   1.20007 |
| f1-score  |   0 |  0.514286 |  0.555556 | 0.470588 |  0.538462 |   0.508475 |    0.415778 |       0.489562 |   1.20007 |
| support   |   4 | 17        | 17        | 9        | 12        |   0.508475 |   59        |      59        |   1.20007 |


## Confusion matrix
|              |   Predicted as 0 |   Predicted as 1 |   Predicted as 2 |   Predicted as 3 |   Predicted as 4 |
|:-------------|-----------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| Labeled as 0 |                0 |                2 |                2 |                0 |                0 |
| Labeled as 1 |                0 |                9 |                4 |                1 |                3 |
| Labeled as 2 |                0 |                4 |               10 |                0 |                3 |
| Labeled as 3 |                0 |                2 |                2 |                4 |                1 |
| Labeled as 4 |                0 |                1 |                1 |                3 |                7 |

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

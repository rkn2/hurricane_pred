# Summary of 21_NeuralNetwork

[<< Go back](../README.md)


## Neural Network
- **n_jobs**: -1
- **dense_1_size**: 64
- **dense_2_size**: 16
- **learning_rate**: 0.05
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

1.5 seconds

### Metric details
|           |   0 |   1 |         2 |        3 |         4 |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|----:|----:|----------:|---------:|----------:|-----------:|------------:|---------------:|----------:|
| precision |   0 |   0 |  0.351351 | 1        |  0.421053 |    0.40678 |    0.354481 |       0.339417 |   1.42816 |
| recall    |   0 |   0 |  0.764706 | 0.333333 |  0.666667 |    0.40678 |    0.352941 |       0.40678  |   1.42816 |
| f1-score  |   0 |   0 |  0.481481 | 0.5      |  0.516129 |    0.40678 |    0.299522 |       0.319979 |   1.42816 |
| support   |   4 |  17 | 17        | 9        | 12        |    0.40678 |   59        |      59        |   1.42816 |


## Confusion matrix
|              |   Predicted as 0 |   Predicted as 1 |   Predicted as 2 |   Predicted as 3 |   Predicted as 4 |
|:-------------|-----------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| Labeled as 0 |                0 |                0 |                4 |                0 |                0 |
| Labeled as 1 |                0 |                0 |               11 |                0 |                6 |
| Labeled as 2 |                0 |                0 |               13 |                0 |                4 |
| Labeled as 3 |                0 |                0 |                5 |                3 |                1 |
| Labeled as 4 |                0 |                0 |                4 |                0 |                8 |

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

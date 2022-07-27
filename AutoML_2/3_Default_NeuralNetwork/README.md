# Summary of 3_Default_NeuralNetwork

[<< Go back](../README.md)


## Neural Network
- **n_jobs**: -1
- **dense_1_size**: 32
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

1.7 seconds

### Metric details
|           |   0 |         1 |         2 |        3 |         4 |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|----:|----------:|----------:|---------:|----------:|-----------:|------------:|---------------:|----------:|
| precision |   0 |  0.294118 |  0.380952 | 0.222222 |  0.583333 |   0.372881 |    0.296125 |       0.347054 |   1.63409 |
| recall    |   0 |  0.294118 |  0.470588 | 0.222222 |  0.583333 |   0.372881 |    0.314052 |       0.372881 |   1.63409 |
| f1-score  |   0 |  0.294118 |  0.421053 | 0.222222 |  0.583333 |   0.372881 |    0.304145 |       0.358608 |   1.63409 |
| support   |   4 | 17        | 17        | 9        | 12        |   0.372881 |   59        |      59        |   1.63409 |


## Confusion matrix
|              |   Predicted as 0 |   Predicted as 1 |   Predicted as 2 |   Predicted as 3 |   Predicted as 4 |
|:-------------|-----------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| Labeled as 0 |                0 |                2 |                1 |                1 |                0 |
| Labeled as 1 |                0 |                5 |               11 |                0 |                1 |
| Labeled as 2 |                0 |                4 |                8 |                2 |                3 |
| Labeled as 3 |                0 |                5 |                1 |                2 |                1 |
| Labeled as 4 |                0 |                1 |                0 |                4 |                7 |

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

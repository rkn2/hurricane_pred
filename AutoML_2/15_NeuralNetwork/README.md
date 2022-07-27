# Summary of 15_NeuralNetwork

[<< Go back](../README.md)


## Neural Network
- **n_jobs**: -1
- **dense_1_size**: 64
- **dense_2_size**: 32
- **learning_rate**: 0.08
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

1.6 seconds

### Metric details
|           |   0 |         1 |         2 |        3 |         4 |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|----:|----------:|----------:|---------:|----------:|-----------:|------------:|---------------:|----------:|
| precision |   0 |  0.357143 |  0.285714 | 0.2      |  0.666667 |   0.338983 |    0.301905 |       0.351332 |   4.79667 |
| recall    |   0 |  0.294118 |  0.470588 | 0.111111 |  0.5      |   0.338983 |    0.275163 |       0.338983 |   4.79667 |
| f1-score  |   0 |  0.322581 |  0.355556 | 0.142857 |  0.571429 |   0.338983 |    0.278484 |       0.33341  |   4.79667 |
| support   |   4 | 17        | 17        | 9        | 12        |   0.338983 |   59        |      59        |   4.79667 |


## Confusion matrix
|              |   Predicted as 0 |   Predicted as 1 |   Predicted as 2 |   Predicted as 3 |   Predicted as 4 |
|:-------------|-----------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| Labeled as 0 |                0 |                2 |                2 |                0 |                0 |
| Labeled as 1 |                2 |                5 |               10 |                0 |                0 |
| Labeled as 2 |                1 |                3 |                8 |                3 |                2 |
| Labeled as 3 |                0 |                2 |                5 |                1 |                1 |
| Labeled as 4 |                0 |                2 |                3 |                1 |                6 |

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

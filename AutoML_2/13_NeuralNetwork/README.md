# Summary of 13_NeuralNetwork

[<< Go back](../README.md)


## Neural Network
- **n_jobs**: -1
- **dense_1_size**: 32
- **dense_2_size**: 4
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

1.4 seconds

### Metric details
|           |   0 |         1 |         2 |        3 |         4 |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|----:|----------:|----------:|---------:|----------:|-----------:|------------:|---------------:|----------:|
| precision |   0 |  0.4      |  0.333333 | 0.111111 |  0.5      |   0.338983 |    0.268889 |       0.329944 |   3.16825 |
| recall    |   0 |  0.470588 |  0.411765 | 0.111111 |  0.333333 |   0.338983 |    0.265359 |       0.338983 |   3.16825 |
| f1-score  |   0 |  0.432432 |  0.368421 | 0.111111 |  0.4      |   0.338983 |    0.262393 |       0.329059 |   3.16825 |
| support   |   4 | 17        | 17        | 9        | 12        |   0.338983 |   59        |      59        |   3.16825 |


## Confusion matrix
|              |   Predicted as 0 |   Predicted as 1 |   Predicted as 2 |   Predicted as 3 |   Predicted as 4 |
|:-------------|-----------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| Labeled as 0 |                0 |                2 |                1 |                0 |                1 |
| Labeled as 1 |                1 |                8 |                6 |                1 |                1 |
| Labeled as 2 |                0 |                5 |                7 |                4 |                1 |
| Labeled as 3 |                0 |                4 |                3 |                1 |                1 |
| Labeled as 4 |                0 |                1 |                4 |                3 |                4 |

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

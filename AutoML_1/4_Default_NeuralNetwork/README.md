# Summary of 4_Default_NeuralNetwork

[<< Go back](../README.md)


## Neural Network
- **n_jobs**: -1
- **dense_1_size**: 32
- **dense_2_size**: 16
- **learning_rate**: 0.05
- **num_class**: 5
- **explain_level**: 2

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
|           |   0 |         1 |         2 |        3 |         4 |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|----:|----------:|----------:|---------:|----------:|-----------:|------------:|---------------:|----------:|
| precision |   0 |  0.428571 |  0.3      | 0.181818 |  0.583333 |   0.355932 |    0.298745 |       0.356306 |   4.30916 |
| recall    |   0 |  0.352941 |  0.352941 | 0.222222 |  0.583333 |   0.355932 |    0.302288 |       0.355932 |   4.30916 |
| f1-score  |   0 |  0.387097 |  0.324324 | 0.2      |  0.583333 |   0.355932 |    0.298951 |       0.354138 |   4.30916 |
| support   |   4 | 17        | 17        | 9        | 12        |   0.355932 |   59        |      59        |   4.30916 |


## Confusion matrix
|              |   Predicted as 0 |   Predicted as 1 |   Predicted as 2 |   Predicted as 3 |   Predicted as 4 |
|:-------------|-----------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| Labeled as 0 |                0 |                0 |                3 |                0 |                1 |
| Labeled as 1 |                1 |                6 |                8 |                1 |                1 |
| Labeled as 2 |                0 |                5 |                6 |                4 |                2 |
| Labeled as 3 |                1 |                2 |                3 |                2 |                1 |
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

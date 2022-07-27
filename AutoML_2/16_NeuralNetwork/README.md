# Summary of 16_NeuralNetwork

[<< Go back](../README.md)


## Neural Network
- **n_jobs**: -1
- **dense_1_size**: 32
- **dense_2_size**: 32
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
|           |   0 |         1 |         2 |        3 |         4 |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|----:|----------:|----------:|---------:|----------:|-----------:|------------:|---------------:|----------:|
| precision |   0 |  0.411765 |  0.4375   | 0.272727 |  0.571429 |   0.423729 |    0.338684 |       0.402529 |   4.68189 |
| recall    |   0 |  0.411765 |  0.411765 | 0.333333 |  0.666667 |   0.423729 |    0.364706 |       0.423729 |   4.68189 |
| f1-score  |   0 |  0.411765 |  0.424242 | 0.3      |  0.615385 |   0.423729 |    0.350278 |       0.411809 |   4.68189 |
| support   |   4 | 17        | 17        | 9        | 12        |   0.423729 |   59        |      59        |   4.68189 |


## Confusion matrix
|              |   Predicted as 0 |   Predicted as 1 |   Predicted as 2 |   Predicted as 3 |   Predicted as 4 |
|:-------------|-----------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| Labeled as 0 |                0 |                2 |                1 |                1 |                0 |
| Labeled as 1 |                1 |                7 |                5 |                1 |                3 |
| Labeled as 2 |                0 |                5 |                7 |                3 |                2 |
| Labeled as 3 |                0 |                2 |                3 |                3 |                1 |
| Labeled as 4 |                0 |                1 |                0 |                3 |                8 |

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

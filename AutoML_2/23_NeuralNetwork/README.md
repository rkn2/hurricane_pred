# Summary of 23_NeuralNetwork

[<< Go back](../README.md)


## Neural Network
- **n_jobs**: -1
- **dense_1_size**: 32
- **dense_2_size**: 16
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

1.8 seconds

### Metric details
|           |   0 |         1 |         2 |   3 |         4 |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|----:|----------:|----------:|----:|----------:|-----------:|------------:|---------------:|----------:|
| precision |   0 |  0.3125   |  0.428571 |   0 |  0.538462 |   0.389831 |    0.255907 |       0.323047 |   1.61772 |
| recall    |   0 |  0.588235 |  0.352941 |   0 |  0.583333 |   0.389831 |    0.304902 |       0.389831 |   1.61772 |
| f1-score  |   0 |  0.408163 |  0.387097 |   0 |  0.56     |   0.389831 |    0.271052 |       0.343041 |   1.61772 |
| support   |   4 | 17        | 17        |   9 | 12        |   0.389831 |   59        |      59        |   1.61772 |


## Confusion matrix
|              |   Predicted as 0 |   Predicted as 1 |   Predicted as 2 |   Predicted as 3 |   Predicted as 4 |
|:-------------|-----------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| Labeled as 0 |                0 |                2 |                2 |                0 |                0 |
| Labeled as 1 |                0 |               10 |                5 |                0 |                2 |
| Labeled as 2 |                0 |                9 |                6 |                0 |                2 |
| Labeled as 3 |                0 |                6 |                1 |                0 |                2 |
| Labeled as 4 |                0 |                5 |                0 |                0 |                7 |

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

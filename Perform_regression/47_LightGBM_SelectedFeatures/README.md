# Summary of 47_LightGBM_SelectedFeatures

[<< Go back](../README.md)


## LightGBM
- **n_jobs**: -1
- **objective**: regression
- **num_leaves**: 63
- **learning_rate**: 0.05
- **feature_fraction**: 1.0
- **bagging_fraction**: 0.8
- **min_data_in_leaf**: 10
- **metric**: rmse
- **custom_eval_metric_name**: None
- **explain_level**: 1

## Validation
 - **validation_type**: kfold
 - **k_folds**: 5
 - **shuffle**: True

## Optimized metric
rmse

## Training time

8.5 seconds

### Metric details:
| Metric   |       Score |
|:---------|------------:|
| MAE      | 0.698973    |
| MSE      | 0.830315    |
| RMSE     | 0.911216    |
| R2       | 0.441472    |
| MAPE     | 3.69454e+14 |



## Learning curves
![Learning curves](learning_curves.png)

## Permutation-based Importance
![Permutation-based Importance](permutation_importance.png)
## True vs Predicted

![True vs Predicted](true_vs_predicted.png)


## Predicted vs Residuals

![Predicted vs Residuals](predicted_vs_residuals.png)



[<< Go back](../README.md)

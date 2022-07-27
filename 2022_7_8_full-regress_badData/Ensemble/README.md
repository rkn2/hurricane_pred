# Summary of Ensemble

[<< Go back](../README.md)


## Ensemble structure
| Model                             |   Weight |
|:----------------------------------|---------:|
| 11_RandomForest_GoldenFeatures    |        1 |
| 1_DecisionTree                    |        1 |
| 23_CatBoost_SelectedFeatures      |        6 |
| 25_Xgboost_SelectedFeatures       |        2 |
| 4_Default_Xgboost_categorical_mix |        1 |
| 7_CatBoost_SelectedFeatures       |       14 |

### Metric details:
| Metric   |       Score |
|:---------|------------:|
| MAE      | 0.145885    |
| MSE      | 0.103977    |
| RMSE     | 0.322455    |
| R2       | 0.930508    |
| MAPE     | 3.28568e+13 |



## Learning curves
![Learning curves](learning_curves.png)
## True vs Predicted

![True vs Predicted](true_vs_predicted.png)


## Predicted vs Residuals

![Predicted vs Residuals](predicted_vs_residuals.png)



[<< Go back](../README.md)

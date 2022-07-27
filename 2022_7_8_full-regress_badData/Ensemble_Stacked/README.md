# Summary of Ensemble_Stacked

[<< Go back](../README.md)


## Ensemble structure
| Model                                       |   Weight |
|:--------------------------------------------|---------:|
| 1_DecisionTree                              |        1 |
| 23_CatBoost_SelectedFeatures                |        4 |
| 23_CatBoost_SelectedFeatures_Stacked        |        5 |
| 24_RandomForest_GoldenFeatures_Stacked      |        7 |
| 2_Linear                                    |        1 |
| 5_Default_CatBoost_SelectedFeatures_Stacked |       10 |
| 7_CatBoost_SelectedFeatures                 |       21 |
| 8_CatBoost_SelectedFeatures_Stacked         |       10 |
| Ensemble                                    |        1 |

### Metric details:
| Metric   |       Score |
|:---------|------------:|
| MAE      | 0.152724    |
| MSE      | 0.100889    |
| RMSE     | 0.31763     |
| R2       | 0.932572    |
| MAPE     | 2.96874e+13 |



## Learning curves
![Learning curves](learning_curves.png)
## True vs Predicted

![True vs Predicted](true_vs_predicted.png)


## Predicted vs Residuals

![Predicted vs Residuals](predicted_vs_residuals.png)



[<< Go back](../README.md)

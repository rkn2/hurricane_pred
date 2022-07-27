# Summary of 2_DecisionTree

[<< Go back](../README.md)


## Decision Tree
- **n_jobs**: -1
- **criterion**: mse
- **max_depth**: 3
- **explain_level**: 2

## Validation
 - **validation_type**: split
 - **train_ratio**: 0.75
 - **shuffle**: True

## Optimized metric
rmse

## Training time

10.1 seconds

### Metric details:
| Metric   |       Score |
|:---------|------------:|
| MAE      | 0.780634    |
| MSE      | 0.926479    |
| RMSE     | 0.962538    |
| R2       | 0.371656    |
| MAPE     | 4.57892e+14 |



## Learning curves
![Learning curves](learning_curves.png)

## Decision Tree 

### Tree #1
![Tree 1](learner_fold_0_tree.svg)

### Rules

if (mindist > 10.468) and (building_type_SingleFamily > 0.5) and (foundation_type_WoodPiers_le_8ft <= 0.5) then response: 1.661 | based on 277 samples

if (mindist <= 10.468) and (year_built <= 1996.5) and (wall_cladding_FiberCementBoard <= 0.5) then response: 3.797 | based on 64 samples

if (mindist > 10.468) and (building_type_SingleFamily <= 0.5) and (roof_substrate_type_Unknown <= 0.5) then response: 2.597 | based on 62 samples

if (mindist <= 10.468) and (year_built > 1996.5) and (wall_substrate_Woodsheathingcontinuous > 0.5) then response: 2.375 | based on 16 samples

if (mindist > 10.468) and (building_type_SingleFamily <= 0.5) and (roof_substrate_type_Unknown > 0.5) then response: 1.357 | based on 14 samples

if (mindist > 10.468) and (building_type_SingleFamily > 0.5) and (foundation_type_WoodPiers_le_8ft > 0.5) then response: 3.667 | based on 6 samples

if (mindist <= 10.468) and (year_built > 1996.5) and (wall_substrate_Woodsheathingcontinuous <= 0.5) then response: 0.0 | based on 1 samples

if (mindist <= 10.468) and (year_built <= 1996.5) and (wall_cladding_FiberCementBoard > 0.5) then response: 1.0 | based on 1 samples





## Permutation-based Importance
![Permutation-based Importance](permutation_importance.png)
## True vs Predicted

![True vs Predicted](true_vs_predicted.png)


## Predicted vs Residuals

![Predicted vs Residuals](predicted_vs_residuals.png)



## SHAP Importance
![SHAP Importance](shap_importance.png)

## SHAP Dependence plots

### Dependence (Fold 1)
![SHAP Dependence from Fold 1](learner_fold_0_shap_dependence.png)

## SHAP Decision plots

### Top-10 Worst decisions (Fold 1)
![SHAP worst decisions from fold 1](learner_fold_0_shap_worst_decisions.png)
### Top-10 Best decisions (Fold 1)
![SHAP best decisions from fold 1](learner_fold_0_shap_best_decisions.png)

[<< Go back](../README.md)

# Summary of 2_DecisionTree

[<< Go back](../README.md)


## Decision Tree
- **n_jobs**: -1
- **criterion**: mse
- **max_depth**: 3
- **explain_level**: 2

## Validation
 - **validation_type**: kfold
 - **k_folds**: 5
 - **shuffle**: True

## Optimized metric
rmse

## Training time

21.4 seconds

### Metric details:
| Metric   |     Score |
|:---------|----------:|
| MAE      | 0.790036  |
| MSE      | 0.993011  |
| RMSE     | 0.996499  |
| R2       | 0.336331  |
| MAPE     | 4.886e+14 |



## Learning curves
![Learning curves](learning_curves.png)

## Decision Tree 

### Tree #1
![Tree 1](learner_fold_0_tree.svg)

### Rules

if (mindist > 10.507) and (year_built > 1995.5) and (roof_substrate_type > 1.5) then response: 1.507 | based on 211 samples

if (mindist > 10.507) and (year_built <= 1995.5) and (Buildinglong <= -85.373) then response: 2.434 | based on 122 samples

if (mindist <= 10.507) and (year_built <= 1996.5) and (wall_structure > 6.0) then response: 3.836 | based on 73 samples

if (mindist > 10.507) and (year_built <= 1995.5) and (Buildinglong > -85.373) then response: 1.595 | based on 42 samples

if (mindist <= 10.507) and (year_built > 1996.5) and (hazards_present > 1.0) then response: 2.867 | based on 15 samples

if (mindist > 10.507) and (year_built > 1995.5) and (roof_substrate_type <= 1.5) then response: 2.857 | based on 7 samples

if (mindist <= 10.507) and (year_built <= 1996.5) and (wall_structure <= 6.0) then response: 2.5 | based on 2 samples

if (mindist <= 10.507) and (year_built > 1996.5) and (hazards_present <= 1.0) then response: 0.0 | based on 1 samples




### Tree #2
![Tree 2](learner_fold_1_tree.svg)

### Rules

if (mindist > 10.486) and (year_built > 1995.5) and (roof_substrate_type > 2.5) then response: 1.524 | based on 212 samples

if (mindist > 10.486) and (year_built <= 1995.5) and (Buildinglong <= -85.048) then response: 2.297 | based on 155 samples

if (mindist <= 10.486) and (year_built <= 1996.5) and (hazards_present <= 19.5) then response: 3.783 | based on 69 samples

if (mindist <= 10.486) and (year_built > 1996.5) and (hazards_present > 1.0) then response: 2.737 | based on 19 samples

if (mindist > 10.486) and (year_built > 1995.5) and (roof_substrate_type <= 2.5) then response: 2.75 | based on 8 samples

if (mindist > 10.486) and (year_built <= 1995.5) and (Buildinglong > -85.048) then response: 0.875 | based on 8 samples

if (mindist <= 10.486) and (year_built > 1996.5) and (hazards_present <= 1.0) then response: 0.0 | based on 1 samples

if (mindist <= 10.486) and (year_built <= 1996.5) and (hazards_present > 19.5) then response: 1.0 | based on 1 samples




### Tree #3
![Tree 3](learner_fold_2_tree.svg)

### Rules

if (mindist > 10.564) and (year_built > 1995.5) and (Buildinglong <= -85.377) then response: 1.645 | based on 172 samples

if (mindist > 10.564) and (year_built <= 1995.5) and (foundation_type <= 8.5) then response: 2.031 | based on 160 samples

if (mindist <= 10.564) and (hazards_present <= 12.5) and (hazards_present > 3.5) then response: 3.903 | based on 62 samples

if (mindist > 10.564) and (year_built > 1995.5) and (Buildinglong > -85.377) then response: 1.0 | based on 38 samples

if (mindist <= 10.564) and (hazards_present > 12.5) and (roof_cover <= 2.5) then response: 2.722 | based on 18 samples

if (mindist > 10.564) and (year_built <= 1995.5) and (foundation_type > 8.5) then response: 3.333 | based on 12 samples

if (mindist <= 10.564) and (hazards_present > 12.5) and (roof_cover > 2.5) then response: 3.667 | based on 9 samples

if (mindist <= 10.564) and (hazards_present <= 12.5) and (hazards_present <= 3.5) then response: 2.667 | based on 3 samples




### Tree #4
![Tree 4](learner_fold_3_tree.svg)

### Rules

if (mindist > 10.507) and (year_built > 1995.5) and (roof_substrate_type > 3.0) then response: 1.536 | based on 209 samples

if (mindist > 10.507) and (year_built <= 1995.5) and (Buildinglong <= -85.373) then response: 2.4 | based on 120 samples

if (mindist <= 10.507) and (year_built <= 1996.5) and (hazards_present <= 21.0) then response: 3.764 | based on 72 samples

if (mindist > 10.507) and (year_built <= 1995.5) and (Buildinglong > -85.373) then response: 1.523 | based on 44 samples

if (mindist <= 10.507) and (year_built > 1996.5) and (hazards_present > 1.0) then response: 2.737 | based on 19 samples

if (mindist > 10.507) and (year_built > 1995.5) and (roof_substrate_type <= 3.0) then response: 2.75 | based on 8 samples

if (mindist <= 10.507) and (year_built > 1996.5) and (hazards_present <= 1.0) then response: 0.0 | based on 1 samples

if (mindist <= 10.507) and (year_built <= 1996.5) and (hazards_present > 21.0) then response: 1.0 | based on 1 samples




### Tree #5
![Tree 5](learner_fold_4_tree.svg)

### Rules

if (mindist > 11.174) and (year_built <= 1995.5) and (hazards_present > 0.5) then response: 2.229 | based on 179 samples

if (mindist > 11.174) and (year_built > 1995.5) and (mindist > 18.747) then response: 1.785 | based on 121 samples

if (mindist > 11.174) and (year_built > 1995.5) and (mindist <= 18.747) then response: 1.282 | based on 78 samples

if (mindist <= 11.174) and (year_built <= 1996.5) and (hazards_present <= 20.5) then response: 3.771 | based on 70 samples

if (mindist <= 11.174) and (year_built > 1996.5) and (hazards_present > 1.5) then response: 2.667 | based on 21 samples

if (mindist > 11.174) and (year_built <= 1995.5) and (hazards_present <= 0.5) then response: 0.0 | based on 3 samples

if (mindist <= 11.174) and (year_built > 1996.5) and (hazards_present <= 1.5) then response: 0.0 | based on 1 samples

if (mindist <= 11.174) and (year_built <= 1996.5) and (hazards_present > 20.5) then response: 1.0 | based on 1 samples





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
### Dependence (Fold 2)
![SHAP Dependence from Fold 2](learner_fold_1_shap_dependence.png)
### Dependence (Fold 3)
![SHAP Dependence from Fold 3](learner_fold_2_shap_dependence.png)
### Dependence (Fold 4)
![SHAP Dependence from Fold 4](learner_fold_3_shap_dependence.png)
### Dependence (Fold 5)
![SHAP Dependence from Fold 5](learner_fold_4_shap_dependence.png)

## SHAP Decision plots

### Top-10 Worst decisions (Fold 1)
![SHAP worst decisions from fold 1](learner_fold_0_shap_worst_decisions.png)
### Top-10 Worst decisions (Fold 2)
![SHAP worst decisions from fold 2](learner_fold_1_shap_worst_decisions.png)
### Top-10 Worst decisions (Fold 3)
![SHAP worst decisions from fold 3](learner_fold_2_shap_worst_decisions.png)
### Top-10 Worst decisions (Fold 4)
![SHAP worst decisions from fold 4](learner_fold_3_shap_worst_decisions.png)
### Top-10 Worst decisions (Fold 5)
![SHAP worst decisions from fold 5](learner_fold_4_shap_worst_decisions.png)
### Top-10 Best decisions (Fold 1)
![SHAP best decisions from fold 1](learner_fold_0_shap_best_decisions.png)
### Top-10 Best decisions (Fold 2)
![SHAP best decisions from fold 2](learner_fold_1_shap_best_decisions.png)
### Top-10 Best decisions (Fold 3)
![SHAP best decisions from fold 3](learner_fold_2_shap_best_decisions.png)
### Top-10 Best decisions (Fold 4)
![SHAP best decisions from fold 4](learner_fold_3_shap_best_decisions.png)
### Top-10 Best decisions (Fold 5)
![SHAP best decisions from fold 5](learner_fold_4_shap_best_decisions.png)

[<< Go back](../README.md)

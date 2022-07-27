# Summary of 20_DecisionTree

[<< Go back](../README.md)


## Decision Tree
- **n_jobs**: -1
- **criterion**: mse
- **max_depth**: 2
- **explain_level**: 2

## Validation
 - **validation_type**: kfold
 - **k_folds**: 5
 - **shuffle**: False

## Optimized metric
rmse

## Training time

53.6 seconds

### Metric details:
| Metric   |       Score |
|:---------|------------:|
| MAE      | 0.829302    |
| MSE      | 1.07092     |
| RMSE     | 1.03485     |
| R2       | 0.279624    |
| MAPE     | 5.35063e+14 |



## Learning curves
![Learning curves](learning_curves.png)

## Decision Tree 

### Tree #1
![Tree 1](learner_fold_0_tree.svg)

### Rules

if (mindist > 10.287) and (foundation_type_WoodPiers_le_8ft <= 0.5) then response: 1.787 | based on 375 samples

if (mindist <= 10.287) and (year_built <= 2003.5) then response: 3.688 | based on 77 samples

if (mindist > 10.287) and (foundation_type_WoodPiers_le_8ft > 0.5) then response: 3.667 | based on 9 samples

if (mindist <= 10.287) and (year_built > 2003.5) then response: 2.111 | based on 9 samples




### Tree #2
![Tree 2](learner_fold_1_tree.svg)

### Rules

if (mindist > 10.468) and (building_type_SingleFamily > 0.5) then response: 1.699 | based on 312 samples

if (mindist > 10.468) and (building_type_SingleFamily <= 0.5) then response: 2.412 | based on 80 samples

if (mindist <= 10.468) and (year_built <= 1996.5) then response: 3.793 | based on 58 samples

if (mindist <= 10.468) and (year_built > 1996.5) then response: 2.55 | based on 20 samples




### Tree #3
![Tree 3](learner_fold_2_tree.svg)

### Rules

if (mindist > 10.271) and (year_built > 1995.5) then response: 1.569 | based on 218 samples

if (mindist > 10.271) and (year_built <= 1995.5) then response: 2.199 | based on 166 samples

if (mindist <= 10.271) and (year_built <= 1996.5) then response: 3.809 | based on 68 samples

if (mindist <= 10.271) and (year_built > 1996.5) then response: 2.556 | based on 18 samples




### Tree #4
![Tree 4](learner_fold_3_tree.svg)

### Rules

if (mindist > 10.446) and (year_built > 1995.5) then response: 1.573 | based on 211 samples

if (mindist > 10.446) and (year_built <= 1995.5) then response: 2.179 | based on 173 samples

if (mindist <= 10.446) and (year_built <= 1995.0) then response: 3.771 | based on 70 samples

if (mindist <= 10.446) and (year_built > 1995.0) then response: 2.647 | based on 17 samples




### Tree #5
![Tree 5](learner_fold_4_tree.svg)

### Rules

if (mindist > 10.468) and (building_type_SingleFamily > 0.5) then response: 1.673 | based on 306 samples

if (mindist > 10.468) and (building_type_SingleFamily <= 0.5) then response: 2.605 | based on 76 samples

if (mindist <= 10.468) and (year_built <= 2003.5) then response: 3.747 | based on 75 samples

if (mindist <= 10.468) and (year_built > 2003.5) then response: 2.214 | based on 14 samples





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

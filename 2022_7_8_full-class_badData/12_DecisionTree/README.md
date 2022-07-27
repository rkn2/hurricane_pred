# Summary of 12_DecisionTree

[<< Go back](../README.md)


## Decision Tree
- **n_jobs**: -1
- **criterion**: gini
- **max_depth**: 4
- **num_class**: 5
- **explain_level**: 2

## Validation
 - **validation_type**: kfold
 - **k_folds**: 5
 - **shuffle**: True
 - **stratify**: True

## Optimized metric
logloss

## Training time

152.3 seconds

### Metric details
|           |         0 |          1 |          2 |         3 |          4 |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|----------:|-----------:|-----------:|----------:|-----------:|-----------:|------------:|---------------:|----------:|
| precision |  0.970588 |   0.957831 |   0.87931  |  0.896907 |   0.933884 |   0.920608 |    0.927704 |       0.921848 |  0.535536 |
| recall    |  0.942857 |   0.919075 |   0.916168 |  0.935484 |   0.91129  |   0.920608 |    0.924975 |       0.920608 |  0.535536 |
| f1-score  |  0.956522 |   0.938053 |   0.897361 |  0.915789 |   0.922449 |   0.920608 |    0.926035 |       0.9209   |  0.535536 |
| support   | 35        | 173        | 167        | 93        | 124        |   0.920608 |  592        |     592        |  0.535536 |


## Confusion matrix
|              |   Predicted as 0 |   Predicted as 1 |   Predicted as 2 |   Predicted as 3 |   Predicted as 4 |
|:-------------|-----------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| Labeled as 0 |               33 |                2 |                0 |                0 |                0 |
| Labeled as 1 |                1 |              159 |               11 |                2 |                0 |
| Labeled as 2 |                0 |                4 |              153 |                4 |                6 |
| Labeled as 3 |                0 |                1 |                3 |               87 |                2 |
| Labeled as 4 |                0 |                0 |                7 |                4 |              113 |

## Learning curves
![Learning curves](learning_curves.png)

## Decision Tree 

### Tree #1
![Tree 1](learner_fold_0_tree.svg)

### Rules

if (wind_damage_rating > 1.5) and (wind_damage_rating <= 2.5) and (surge_damage_rating <= 2.5) and (Unnamed0 <= 720.0) then class: 2 (proba: 92.86%) | based on 126 samples

if (wind_damage_rating <= 1.5) and (wind_damage_rating > 0.5) and (surge_damage_rating <= 1.5) and (Unnamed0 > 9.0) then class: 1 (proba: 98.41%) | based on 126 samples

if (wind_damage_rating > 1.5) and (wind_damage_rating > 2.5) and (wind_damage_rating <= 3.5) and (surge_damage_rating <= 3.5) then class: 3 (proba: 90.41%) | based on 73 samples

if (wind_damage_rating <= 1.5) and (wind_damage_rating <= 0.5) and (wind_damage_rating <= -0.5) then class: 4 (proba: 100.0%) | based on 49 samples

if (wind_damage_rating > 1.5) and (wind_damage_rating > 2.5) and (wind_damage_rating > 3.5) and (mindist <= 32.574) then class: 4 (proba: 91.49%) | based on 47 samples

if (wind_damage_rating <= 1.5) and (wind_damage_rating <= 0.5) and (wind_damage_rating > -0.5) and (surge_damage_rating <= 0.5) then class: 0 (proba: 96.3%) | based on 27 samples

if (wind_damage_rating <= 1.5) and (wind_damage_rating > 0.5) and (surge_damage_rating > 1.5) and (surge_damage_rating <= 4.0) then class: 2 (proba: 85.71%) | based on 7 samples

if (wind_damage_rating > 1.5) and (wind_damage_rating <= 2.5) and (surge_damage_rating > 2.5) and (surge_damage_rating <= 3.5) then class: 3 (proba: 100.0%) | based on 4 samples

if (wind_damage_rating <= 1.5) and (wind_damage_rating <= 0.5) and (wind_damage_rating > -0.5) and (surge_damage_rating > 0.5) then class: 1 (proba: 50.0%) | based on 4 samples

if (wind_damage_rating > 1.5) and (wind_damage_rating <= 2.5) and (surge_damage_rating > 2.5) and (surge_damage_rating > 3.5) then class: 4 (proba: 100.0%) | based on 3 samples

if (wind_damage_rating > 1.5) and (wind_damage_rating > 2.5) and (wind_damage_rating <= 3.5) and (surge_damage_rating > 3.5) then class: 4 (proba: 100.0%) | based on 2 samples

if (wind_damage_rating > 1.5) and (wind_damage_rating <= 2.5) and (surge_damage_rating <= 2.5) and (Unnamed0 > 720.0) then class: 1 (proba: 100.0%) | based on 2 samples

if (wind_damage_rating > 1.5) and (wind_damage_rating > 2.5) and (wind_damage_rating > 3.5) and (mindist > 32.574) then class: 3 (proba: 100.0%) | based on 1 samples

if (wind_damage_rating <= 1.5) and (wind_damage_rating > 0.5) and (surge_damage_rating > 1.5) and (surge_damage_rating > 4.0) then class: 4 (proba: 100.0%) | based on 1 samples

if (wind_damage_rating <= 1.5) and (wind_damage_rating > 0.5) and (surge_damage_rating <= 1.5) and (Unnamed0 <= 9.0) then class: 2 (proba: 100.0%) | based on 1 samples




### Tree #2
![Tree 2](learner_fold_1_tree.svg)

### Rules

if (wind_damage_rating <= 1.5) and (wind_damage_rating > 0.5) and (surge_damage_rating <= 1.5) and (Unnamed0 > 14.5) then class: 1 (proba: 98.44%) | based on 128 samples

if (wind_damage_rating > 1.5) and (wind_damage_rating <= 2.5) and (surge_damage_rating <= 2.5) and (Unnamed0 <= 720.0) then class: 2 (proba: 95.16%) | based on 124 samples

if (wind_damage_rating > 1.5) and (wind_damage_rating > 2.5) and (wind_damage_rating <= 3.5) and (surge_damage_rating <= 3.5) then class: 3 (proba: 91.67%) | based on 72 samples

if (wind_damage_rating <= 1.5) and (wind_damage_rating <= 0.5) and (wind_damage_rating <= -0.5) then class: 4 (proba: 100.0%) | based on 50 samples

if (wind_damage_rating > 1.5) and (wind_damage_rating > 2.5) and (wind_damage_rating > 3.5) and (mindist <= 33.425) then class: 4 (proba: 88.89%) | based on 45 samples

if (wind_damage_rating <= 1.5) and (wind_damage_rating <= 0.5) and (wind_damage_rating > -0.5) and (surge_damage_rating <= 0.5) then class: 0 (proba: 100.0%) | based on 27 samples

if (wind_damage_rating > 1.5) and (wind_damage_rating <= 2.5) and (surge_damage_rating > 2.5) and (surge_damage_rating > 3.5) then class: 4 (proba: 100.0%) | based on 5 samples

if (wind_damage_rating <= 1.5) and (wind_damage_rating > 0.5) and (surge_damage_rating > 1.5) and (year_built > 1982.5) then class: 2 (proba: 100.0%) | based on 5 samples

if (wind_damage_rating <= 1.5) and (wind_damage_rating <= 0.5) and (wind_damage_rating > -0.5) and (surge_damage_rating > 0.5) then class: 1 (proba: 80.0%) | based on 5 samples

if (wind_damage_rating > 1.5) and (wind_damage_rating <= 2.5) and (surge_damage_rating > 2.5) and (surge_damage_rating <= 3.5) then class: 3 (proba: 100.0%) | based on 3 samples

if (wind_damage_rating <= 1.5) and (wind_damage_rating > 0.5) and (surge_damage_rating <= 1.5) and (Unnamed0 <= 14.5) then class: 2 (proba: 66.67%) | based on 3 samples

if (wind_damage_rating > 1.5) and (wind_damage_rating > 2.5) and (wind_damage_rating <= 3.5) and (surge_damage_rating > 3.5) then class: 4 (proba: 100.0%) | based on 2 samples

if (wind_damage_rating > 1.5) and (wind_damage_rating <= 2.5) and (surge_damage_rating <= 2.5) and (Unnamed0 > 720.0) then class: 1 (proba: 100.0%) | based on 2 samples

if (wind_damage_rating > 1.5) and (wind_damage_rating > 2.5) and (wind_damage_rating > 3.5) and (mindist > 33.425) then class: 3 (proba: 100.0%) | based on 1 samples

if (wind_damage_rating <= 1.5) and (wind_damage_rating > 0.5) and (surge_damage_rating > 1.5) and (year_built <= 1982.5) then class: 3 (proba: 100.0%) | based on 1 samples




### Tree #3
![Tree 3](learner_fold_2_tree.svg)

### Rules

if (wind_damage_rating <= 1.5) and (surge_damage_rating <= 3.5) and (wind_damage_rating > 0.5) and (surge_damage_rating <= 1.5) then class: 1 (proba: 96.92%) | based on 130 samples

if (wind_damage_rating > 1.5) and (wind_damage_rating <= 2.5) and (surge_damage_rating <= 2.5) and (Buildinglat <= 30.454) then class: 2 (proba: 93.5%) | based on 123 samples

if (wind_damage_rating > 1.5) and (wind_damage_rating > 2.5) and (wind_damage_rating <= 3.5) and (surge_damage_rating <= 3.5) then class: 3 (proba: 91.03%) | based on 78 samples

if (wind_damage_rating <= 1.5) and (surge_damage_rating > 3.5) then class: 4 (proba: 100.0%) | based on 51 samples

if (wind_damage_rating > 1.5) and (wind_damage_rating > 2.5) and (wind_damage_rating > 3.5) and (Buildinglong > -85.672) then class: 4 (proba: 90.48%) | based on 42 samples

if (wind_damage_rating <= 1.5) and (surge_damage_rating <= 3.5) and (wind_damage_rating <= 0.5) and (surge_damage_rating <= 0.5) then class: 0 (proba: 96.3%) | based on 27 samples

if (wind_damage_rating > 1.5) and (wind_damage_rating <= 2.5) and (surge_damage_rating > 2.5) and (surge_damage_rating > 3.5) then class: 4 (proba: 100.0%) | based on 5 samples

if (wind_damage_rating <= 1.5) and (surge_damage_rating <= 3.5) and (wind_damage_rating > 0.5) and (surge_damage_rating > 1.5) then class: 2 (proba: 100.0%) | based on 5 samples

if (wind_damage_rating <= 1.5) and (surge_damage_rating <= 3.5) and (wind_damage_rating <= 0.5) and (surge_damage_rating > 0.5) then class: 1 (proba: 60.0%) | based on 5 samples

if (wind_damage_rating > 1.5) and (wind_damage_rating > 2.5) and (wind_damage_rating > 3.5) and (Buildinglong <= -85.672) then class: 2 (proba: 66.67%) | based on 3 samples

if (wind_damage_rating > 1.5) and (wind_damage_rating > 2.5) and (wind_damage_rating <= 3.5) and (surge_damage_rating > 3.5) then class: 4 (proba: 100.0%) | based on 2 samples

if (wind_damage_rating > 1.5) and (wind_damage_rating <= 2.5) and (surge_damage_rating > 2.5) and (surge_damage_rating <= 3.5) then class: 3 (proba: 100.0%) | based on 2 samples

if (wind_damage_rating > 1.5) and (wind_damage_rating <= 2.5) and (surge_damage_rating <= 2.5) and (Buildinglat > 30.454) then class: 1 (proba: 100.0%) | based on 1 samples




### Tree #4
![Tree 4](learner_fold_3_tree.svg)

### Rules

if (wind_damage_rating <= 1.5) and (surge_damage_rating <= 4.0) and (wind_damage_rating > 0.5) and (surge_damage_rating <= 1.5) then class: 1 (proba: 96.09%) | based on 128 samples

if (wind_damage_rating > 1.5) and (wind_damage_rating <= 2.5) and (surge_damage_rating <= 2.5) and (Buildinglat <= 30.454) then class: 2 (proba: 92.68%) | based on 123 samples

if (wind_damage_rating > 1.5) and (wind_damage_rating > 2.5) and (wind_damage_rating <= 3.5) and (surge_damage_rating <= 3.5) then class: 3 (proba: 90.54%) | based on 74 samples

if (wind_damage_rating <= 1.5) and (surge_damage_rating > 4.0) then class: 4 (proba: 100.0%) | based on 49 samples

if (wind_damage_rating > 1.5) and (wind_damage_rating > 2.5) and (wind_damage_rating > 3.5) and (roof_shape <= 8.5) then class: 4 (proba: 90.48%) | based on 42 samples

if (wind_damage_rating <= 1.5) and (surge_damage_rating <= 4.0) and (wind_damage_rating <= 0.5) and (surge_damage_rating <= 0.5) then class: 0 (proba: 96.3%) | based on 27 samples

if (wind_damage_rating <= 1.5) and (surge_damage_rating <= 4.0) and (wind_damage_rating > 0.5) and (surge_damage_rating > 1.5) then class: 2 (proba: 87.5%) | based on 8 samples

if (wind_damage_rating > 1.5) and (wind_damage_rating > 2.5) and (wind_damage_rating > 3.5) and (roof_shape > 8.5) then class: 2 (proba: 50.0%) | based on 6 samples

if (wind_damage_rating <= 1.5) and (surge_damage_rating <= 4.0) and (wind_damage_rating <= 0.5) and (surge_damage_rating > 0.5) then class: 1 (proba: 80.0%) | based on 5 samples

if (wind_damage_rating > 1.5) and (wind_damage_rating <= 2.5) and (surge_damage_rating > 2.5) and (Unnamed0 <= 313.0) then class: 4 (proba: 100.0%) | based on 4 samples

if (wind_damage_rating > 1.5) and (wind_damage_rating > 2.5) and (wind_damage_rating <= 3.5) and (surge_damage_rating > 3.5) then class: 4 (proba: 100.0%) | based on 3 samples

if (wind_damage_rating > 1.5) and (wind_damage_rating <= 2.5) and (surge_damage_rating > 2.5) and (Unnamed0 > 313.0) then class: 3 (proba: 100.0%) | based on 3 samples

if (wind_damage_rating > 1.5) and (wind_damage_rating <= 2.5) and (surge_damage_rating <= 2.5) and (Buildinglat > 30.454) then class: 1 (proba: 100.0%) | based on 2 samples




### Tree #5
![Tree 5](learner_fold_4_tree.svg)

### Rules

if (wind_damage_rating > 1.5) and (wind_damage_rating <= 2.5) and (surge_damage_rating <= 2.5) and (Buildinglat <= 30.614) then class: 2 (proba: 93.75%) | based on 128 samples

if (wind_damage_rating <= 1.5) and (surge_damage_rating <= 4.0) and (wind_damage_rating > 0.5) and (surge_damage_rating <= 1.5) then class: 1 (proba: 96.88%) | based on 128 samples

if (wind_damage_rating > 1.5) and (wind_damage_rating > 2.5) and (wind_damage_rating <= 3.5) and (surge_damage_rating <= 3.5) then class: 3 (proba: 92.96%) | based on 71 samples

if (wind_damage_rating <= 1.5) and (surge_damage_rating > 4.0) then class: 4 (proba: 100.0%) | based on 52 samples

if (wind_damage_rating > 1.5) and (wind_damage_rating > 2.5) and (wind_damage_rating > 3.5) and (mwfrs <= 17.5) then class: 4 (proba: 93.18%) | based on 44 samples

if (wind_damage_rating <= 1.5) and (surge_damage_rating <= 4.0) and (wind_damage_rating <= 0.5) and (surge_damage_rating <= 0.5) then class: 0 (proba: 96.43%) | based on 28 samples

if (wind_damage_rating <= 1.5) and (surge_damage_rating <= 4.0) and (wind_damage_rating > 0.5) and (surge_damage_rating > 1.5) then class: 2 (proba: 83.33%) | based on 6 samples

if (wind_damage_rating <= 1.5) and (surge_damage_rating <= 4.0) and (wind_damage_rating <= 0.5) and (surge_damage_rating > 0.5) then class: 1 (proba: 60.0%) | based on 5 samples

if (wind_damage_rating > 1.5) and (wind_damage_rating <= 2.5) and (surge_damage_rating > 2.5) and (surge_damage_rating <= 3.5) then class: 3 (proba: 100.0%) | based on 4 samples

if (wind_damage_rating > 1.5) and (wind_damage_rating > 2.5) and (wind_damage_rating <= 3.5) and (surge_damage_rating > 3.5) then class: 4 (proba: 100.0%) | based on 3 samples

if (wind_damage_rating > 1.5) and (wind_damage_rating <= 2.5) and (surge_damage_rating > 2.5) and (surge_damage_rating > 3.5) then class: 4 (proba: 100.0%) | based on 3 samples

if (wind_damage_rating > 1.5) and (wind_damage_rating > 2.5) and (wind_damage_rating > 3.5) and (mwfrs > 17.5) then class: 3 (proba: 100.0%) | based on 1 samples

if (wind_damage_rating > 1.5) and (wind_damage_rating <= 2.5) and (surge_damage_rating <= 2.5) and (Buildinglat > 30.614) then class: 1 (proba: 100.0%) | based on 1 samples





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



## SHAP Importance
![SHAP Importance](shap_importance.png)

## SHAP Dependence plots

### Dependence 0 (Fold 1)
![SHAP Dependence from fold 1](learner_fold_0_shap_dependence_class_0.png)
### Dependence 1 (Fold 1)
![SHAP Dependence from fold 1](learner_fold_0_shap_dependence_class_1.png)
### Dependence 2 (Fold 1)
![SHAP Dependence from fold 1](learner_fold_0_shap_dependence_class_2.png)
### Dependence 3 (Fold 1)
![SHAP Dependence from fold 1](learner_fold_0_shap_dependence_class_3.png)
### Dependence 4 (Fold 1)
![SHAP Dependence from fold 1](learner_fold_0_shap_dependence_class_4.png)
### Dependence 0 (Fold 2)
![SHAP Dependence from fold 2](learner_fold_1_shap_dependence_class_0.png)
### Dependence 1 (Fold 2)
![SHAP Dependence from fold 2](learner_fold_1_shap_dependence_class_1.png)
### Dependence 2 (Fold 2)
![SHAP Dependence from fold 2](learner_fold_1_shap_dependence_class_2.png)
### Dependence 3 (Fold 2)
![SHAP Dependence from fold 2](learner_fold_1_shap_dependence_class_3.png)
### Dependence 4 (Fold 2)
![SHAP Dependence from fold 2](learner_fold_1_shap_dependence_class_4.png)
### Dependence 0 (Fold 3)
![SHAP Dependence from fold 3](learner_fold_2_shap_dependence_class_0.png)
### Dependence 1 (Fold 3)
![SHAP Dependence from fold 3](learner_fold_2_shap_dependence_class_1.png)
### Dependence 2 (Fold 3)
![SHAP Dependence from fold 3](learner_fold_2_shap_dependence_class_2.png)
### Dependence 3 (Fold 3)
![SHAP Dependence from fold 3](learner_fold_2_shap_dependence_class_3.png)
### Dependence 4 (Fold 3)
![SHAP Dependence from fold 3](learner_fold_2_shap_dependence_class_4.png)
### Dependence 0 (Fold 4)
![SHAP Dependence from fold 4](learner_fold_3_shap_dependence_class_0.png)
### Dependence 1 (Fold 4)
![SHAP Dependence from fold 4](learner_fold_3_shap_dependence_class_1.png)
### Dependence 2 (Fold 4)
![SHAP Dependence from fold 4](learner_fold_3_shap_dependence_class_2.png)
### Dependence 3 (Fold 4)
![SHAP Dependence from fold 4](learner_fold_3_shap_dependence_class_3.png)
### Dependence 4 (Fold 4)
![SHAP Dependence from fold 4](learner_fold_3_shap_dependence_class_4.png)
### Dependence 0 (Fold 5)
![SHAP Dependence from fold 5](learner_fold_4_shap_dependence_class_0.png)
### Dependence 1 (Fold 5)
![SHAP Dependence from fold 5](learner_fold_4_shap_dependence_class_1.png)
### Dependence 2 (Fold 5)
![SHAP Dependence from fold 5](learner_fold_4_shap_dependence_class_2.png)
### Dependence 3 (Fold 5)
![SHAP Dependence from fold 5](learner_fold_4_shap_dependence_class_3.png)
### Dependence 4 (Fold 5)
![SHAP Dependence from fold 5](learner_fold_4_shap_dependence_class_4.png)

## SHAP Decision plots

### Worst decisions for selected sample 1 (Fold 1)
![SHAP worst decisions from Fold 1](learner_fold_0_sample_0_worst_decisions.png)
### Worst decisions for selected sample 1 (Fold 2)
![SHAP worst decisions from Fold 2](learner_fold_1_sample_0_worst_decisions.png)
### Worst decisions for selected sample 1 (Fold 3)
![SHAP worst decisions from Fold 3](learner_fold_2_sample_0_worst_decisions.png)
### Worst decisions for selected sample 1 (Fold 4)
![SHAP worst decisions from Fold 4](learner_fold_3_sample_0_worst_decisions.png)
### Worst decisions for selected sample 1 (Fold 5)
![SHAP worst decisions from Fold 5](learner_fold_4_sample_0_worst_decisions.png)
### Worst decisions for selected sample 2 (Fold 1)
![SHAP worst decisions from Fold 1](learner_fold_0_sample_1_worst_decisions.png)
### Worst decisions for selected sample 2 (Fold 2)
![SHAP worst decisions from Fold 2](learner_fold_1_sample_1_worst_decisions.png)
### Worst decisions for selected sample 2 (Fold 3)
![SHAP worst decisions from Fold 3](learner_fold_2_sample_1_worst_decisions.png)
### Worst decisions for selected sample 2 (Fold 4)
![SHAP worst decisions from Fold 4](learner_fold_3_sample_1_worst_decisions.png)
### Worst decisions for selected sample 2 (Fold 5)
![SHAP worst decisions from Fold 5](learner_fold_4_sample_1_worst_decisions.png)
### Worst decisions for selected sample 3 (Fold 1)
![SHAP worst decisions from Fold 1](learner_fold_0_sample_2_worst_decisions.png)
### Worst decisions for selected sample 3 (Fold 2)
![SHAP worst decisions from Fold 2](learner_fold_1_sample_2_worst_decisions.png)
### Worst decisions for selected sample 3 (Fold 3)
![SHAP worst decisions from Fold 3](learner_fold_2_sample_2_worst_decisions.png)
### Worst decisions for selected sample 3 (Fold 4)
![SHAP worst decisions from Fold 4](learner_fold_3_sample_2_worst_decisions.png)
### Worst decisions for selected sample 3 (Fold 5)
![SHAP worst decisions from Fold 5](learner_fold_4_sample_2_worst_decisions.png)
### Worst decisions for selected sample 4 (Fold 1)
![SHAP worst decisions from Fold 1](learner_fold_0_sample_3_worst_decisions.png)
### Worst decisions for selected sample 4 (Fold 2)
![SHAP worst decisions from Fold 2](learner_fold_1_sample_3_worst_decisions.png)
### Worst decisions for selected sample 4 (Fold 3)
![SHAP worst decisions from Fold 3](learner_fold_2_sample_3_worst_decisions.png)
### Worst decisions for selected sample 4 (Fold 4)
![SHAP worst decisions from Fold 4](learner_fold_3_sample_3_worst_decisions.png)
### Worst decisions for selected sample 4 (Fold 5)
![SHAP worst decisions from Fold 5](learner_fold_4_sample_3_worst_decisions.png)
### Best decisions for selected sample 1 (Fold 1)
![SHAP best decisions from Fold 1](learner_fold_0_sample_0_best_decisions.png)
### Best decisions for selected sample 1 (Fold 2)
![SHAP best decisions from Fold 2](learner_fold_1_sample_0_best_decisions.png)
### Best decisions for selected sample 1 (Fold 3)
![SHAP best decisions from Fold 3](learner_fold_2_sample_0_best_decisions.png)
### Best decisions for selected sample 1 (Fold 4)
![SHAP best decisions from Fold 4](learner_fold_3_sample_0_best_decisions.png)
### Best decisions for selected sample 1 (Fold 5)
![SHAP best decisions from Fold 5](learner_fold_4_sample_0_best_decisions.png)
### Best decisions for selected sample 2 (Fold 1)
![SHAP best decisions from Fold 1](learner_fold_0_sample_1_best_decisions.png)
### Best decisions for selected sample 2 (Fold 2)
![SHAP best decisions from Fold 2](learner_fold_1_sample_1_best_decisions.png)
### Best decisions for selected sample 2 (Fold 3)
![SHAP best decisions from Fold 3](learner_fold_2_sample_1_best_decisions.png)
### Best decisions for selected sample 2 (Fold 4)
![SHAP best decisions from Fold 4](learner_fold_3_sample_1_best_decisions.png)
### Best decisions for selected sample 2 (Fold 5)
![SHAP best decisions from Fold 5](learner_fold_4_sample_1_best_decisions.png)
### Best decisions for selected sample 3 (Fold 1)
![SHAP best decisions from Fold 1](learner_fold_0_sample_2_best_decisions.png)
### Best decisions for selected sample 3 (Fold 2)
![SHAP best decisions from Fold 2](learner_fold_1_sample_2_best_decisions.png)
### Best decisions for selected sample 3 (Fold 3)
![SHAP best decisions from Fold 3](learner_fold_2_sample_2_best_decisions.png)
### Best decisions for selected sample 3 (Fold 4)
![SHAP best decisions from Fold 4](learner_fold_3_sample_2_best_decisions.png)
### Best decisions for selected sample 3 (Fold 5)
![SHAP best decisions from Fold 5](learner_fold_4_sample_2_best_decisions.png)
### Best decisions for selected sample 4 (Fold 1)
![SHAP best decisions from Fold 1](learner_fold_0_sample_3_best_decisions.png)
### Best decisions for selected sample 4 (Fold 2)
![SHAP best decisions from Fold 2](learner_fold_1_sample_3_best_decisions.png)
### Best decisions for selected sample 4 (Fold 3)
![SHAP best decisions from Fold 3](learner_fold_2_sample_3_best_decisions.png)
### Best decisions for selected sample 4 (Fold 4)
![SHAP best decisions from Fold 4](learner_fold_3_sample_3_best_decisions.png)
### Best decisions for selected sample 4 (Fold 5)
![SHAP best decisions from Fold 5](learner_fold_4_sample_3_best_decisions.png)

[<< Go back](../README.md)

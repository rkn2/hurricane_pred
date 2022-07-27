# Summary of 11_DecisionTree

[<< Go back](../README.md)


## Decision Tree
- **n_jobs**: -1
- **criterion**: gini
- **max_depth**: 2
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

145.0 seconds

### Metric details
|           |   0 |          1 |          2 |   3 |          4 |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|----:|-----------:|-----------:|----:|-----------:|-----------:|------------:|---------------:|----------:|
| precision |   0 |   0.451493 |   0.283784 |   0 |   0.757895 |   0.432432 |    0.298634 |       0.370742 |   1.31839 |
| recall    |   0 |   0.699422 |   0.377246 |   0 |   0.580645 |   0.432432 |    0.331463 |       0.432432 |   1.31839 |
| f1-score  |   0 |   0.548753 |   0.323907 |   0 |   0.657534 |   0.432432 |    0.306039 |       0.389461 |   1.31839 |
| support   |  35 | 173        | 167        |  93 | 124        |   0.432432 |  592        |     592        |   1.31839 |


## Confusion matrix
|              |   Predicted as 0 |   Predicted as 1 |   Predicted as 2 |   Predicted as 3 |   Predicted as 4 |
|:-------------|-----------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| Labeled as 0 |                0 |               18 |               17 |                0 |                0 |
| Labeled as 1 |                0 |              121 |               50 |                0 |                2 |
| Labeled as 2 |                0 |               94 |               63 |                5 |                5 |
| Labeled as 3 |                0 |               29 |               48 |                0 |               16 |
| Labeled as 4 |                0 |                6 |               44 |                2 |               72 |

## Learning curves
![Learning curves](learning_curves.png)

## Decision Tree 

### Tree #1
![Tree 1](learner_fold_0_tree.svg)

### Rules

if (mindist > 10.507) and (year_built > 1995.5) then class: 1 (proba: 45.75%) | based on 212 samples

if (mindist > 10.507) and (year_built <= 1995.5) then class: 2 (proba: 29.48%) | based on 173 samples

if (mindist <= 10.507) and (year_built <= 1996.5) then class: 4 (proba: 80.0%) | based on 70 samples

if (mindist <= 10.507) and (year_built > 1996.5) then class: 2 (proba: 44.44%) | based on 18 samples




### Tree #2
![Tree 2](learner_fold_1_tree.svg)

### Rules

if (mindist > 10.316) and (year_built > 1995.75) then class: 1 (proba: 45.41%) | based on 218 samples

if (mindist > 10.316) and (year_built <= 1995.75) then class: 2 (proba: 30.72%) | based on 166 samples

if (mindist <= 10.316) and (hazards_present <= 14.0) then class: 4 (proba: 88.52%) | based on 61 samples

if (mindist <= 10.316) and (hazards_present > 14.0) then class: 3 (proba: 39.29%) | based on 28 samples




### Tree #3
![Tree 3](learner_fold_2_tree.svg)

### Rules

if (mindist > 10.507) and (year_built > 1995.5) then class: 1 (proba: 44.44%) | based on 225 samples

if (mindist > 10.507) and (year_built <= 1995.5) then class: 2 (proba: 28.66%) | based on 157 samples

if (mindist <= 10.507) and (year_built <= 1988.5) then class: 4 (proba: 87.5%) | based on 64 samples

if (mindist <= 10.507) and (year_built > 1988.5) then class: 3 (proba: 35.71%) | based on 28 samples




### Tree #4
![Tree 4](learner_fold_3_tree.svg)

### Rules

if (mindist > 10.564) and (year_built > 1995.5) then class: 1 (proba: 44.98%) | based on 209 samples

if (mindist > 10.564) and (year_built <= 1995.5) then class: 2 (proba: 30.11%) | based on 176 samples

if (mindist <= 10.564) and (year_built <= 1995.0) then class: 4 (proba: 82.86%) | based on 70 samples

if (mindist <= 10.564) and (year_built > 1995.0) then class: 2 (proba: 36.84%) | based on 19 samples




### Tree #5
![Tree 5](learner_fold_4_tree.svg)

### Rules

if (mindist > 10.507) and (year_built > 1995.5) then class: 1 (proba: 45.63%) | based on 206 samples

if (mindist > 10.507) and (year_built <= 1995.5) then class: 2 (proba: 28.98%) | based on 176 samples

if (mindist <= 10.507) and (mindist <= 9.188) then class: 4 (proba: 89.8%) | based on 49 samples

if (mindist <= 10.507) and (mindist > 9.188) then class: 4 (proba: 46.51%) | based on 43 samples





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

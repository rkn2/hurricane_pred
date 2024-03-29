# -*- coding: utf-8 -*-
"""2023_6_7_tornado_featureImp

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CCyNW603elJpEVqSYvEuU6ll7vLL-XW9
"""

#pip install mljar-supervised

#pip install requests


import requests
#get data
url = 'https://pennstateoffice365-my.sharepoint.com/:x:/g/personal/rjn5308_psu_edu/EZCyXNvyWkJOtNgrYNgGjAIBoQgwq6iGQhdpwLZ96xp6WQ?e=X93gFP&download=1'
r = requests.get(url)
r.status_code

with open('data.csv', 'w') as fid:

    fid.write(r.text)

import pandas as pd
import re
# scikit learn utilites
from sklearn.datasets import load_digits
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
# mljar-supervised package
from supervised.automl import AutoML

#read data into pandas and view
data = pd.read_csv('data.csv')

data = data.rename(columns = lambda x:re.sub('[^A-Za-z0-9_]+', '', x)) # issue with json

#only needed for regression
# Define the mapping dictionary
status_mapping = {
    'undamaged': 0,
    'minor': 1,
    'moderate': 2,
    'severe': 3,
    'destroyed': 4
}

# Update the values in the 'status_u' column
data['status_u'] = data['status_u'].map(status_mapping)

y = data['status_u']



# Drop columns containing the word "status"
columns_to_drop = [column for column in data.columns if 'status' in column]
data = data.drop(columns=columns_to_drop)

# Drop columns containing the word "rating"
columns_to_drop = [column for column in data.columns if 'rating' in column]
data = data.drop(columns=columns_to_drop)

X = data
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.2, random_state=42, stratify=y)

y_train.value_counts().plot(kind='bar',color='green')
y_test.value_counts().plot(kind='bar', color='blue')

""""# regression
"""

automl = AutoML(
    results_path='2023_6_8_reg_noStatus',
    #ml_task='multiclass_classification',
    ml_task = 'regression',
   #algorithms=["CatBoost", "Xgboost", "LightGBM", "Random Forest", "Linear", "Decision Tree"],
    explain_level=2,
    hill_climbing_steps=2,
    top_models_to_improve=2,
    golden_features=True,  # on / off when needed
    features_selection=True,
    stack_models=False,
    train_ensemble=False,
    mix_encoding=True,
    validation_strategy={
        "validation_type": "kfold",
        "k_folds": 5,
        "shuffle": True,
        "stratify": True,
    }
)

automl.fit(X_train, y_train)

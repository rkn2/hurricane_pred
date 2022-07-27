# pip install mljar-supervised
#or
# conda install -c conda-forge mljar-supervised
# pip install requests

import requests
import re
import pandas as pd
from sklearn.model_selection import train_test_split
from supervised.automl import AutoML


#get data
url = 'https://pennstateoffice365-my.sharepoint.com/:x:/g/personal/rjn5308_psu_edu/EZ-qWOeA5jxNkKXpwdWk_CoB-rCxrvsYcdhHaqzLfWruAQ?e=6inkuL&download=1'
r = requests.get(url)
r.status_code
with open('data.csv', 'w') as fid:
    fid.write(r.text)

#read data into pandas and view
data = pd.read_csv('data_og.csv')
data = data.rename(columns = lambda x:re.sub('[^A-Za-z0-9_]+', '', x)) # issue with json
data.fillna(method="ffill", inplace=True)
#data.dropna(inplace=True) # NEW

y = data['status']
X = data.drop('status', axis=1, inplace=False)

# X.describe()
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.2, random_state=42)

automl = AutoML(
    results_path='2022_7_8_full-regress_badData',
    ml_task='regression',
    algorithms=["CatBoost", "Xgboost", "LightGBM", "Random Forest", "Linear", "Decision Tree"],
    explain_level= 2,
    hill_climbing_steps=2,
    top_models_to_improve=2,
    golden_features=True, #on / off when needed
    features_selection=True,
    stack_models=True,
    train_ensemble=True,
    mix_encoding=True,
    validation_strategy={
        "validation_type": "kfold",
        "k_folds": 5,
        "shuffle": True,
        "stratify": True,
    }
)

automl.fit(X_train, y_train)

predictions = automl.predict(X_test)

predict_all = automl.predict_all(X_test)

score = automl.score(X_test)

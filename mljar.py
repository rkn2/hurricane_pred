# pip install mljar-supervised
#or
# conda install -c conda-forge mljar-supervised
# pip install requests

import matplotlib.pyplot as plt
import numpy as np
import pickle
import requests
import re
import pandas as pd
from sklearn.model_selection import train_test_split
from supervised.automl import AutoML


#get data

#read data into pandas and view
#data = pd.read_csv('test.csv')

url = 'https://pennstateoffice365-my.sharepoint.com/:x:/g/personal/rjn5308_psu_edu/EZ-qWOeA5jxNkKXpwdWk_CoB-rCxrvsYcdhHaqzLfWruAQ?e=6inkuL&download=1'
r = requests.get(url)
r.status_code
with open('data.csv', 'w') as fid:
    fid.write(r.text)

#read data into pandas and view
data = pd.read_csv('data.csv')

#data = data.drop(columns=['mindist']) # dtype issue with flaml
#data2
data = data.rename(columns = lambda x:re.sub('[^A-Za-z0-9_]+', '', x)) # issue with json
#data = data.loc[:,~data.columns.duplicated()] # if duplicates

rows, columns = data.shape
cell_count = rows * columns
number_of_nulls = data.isnull().sum().sum()
percentage_of_missing = (number_of_nulls / cell_count) * 100
# print(f'Percentage of missing values: {percentage_of_missing}%')

data.fillna(method="ffill", inplace=True)
data.dropna(inplace=True) # NEW

# rows, columns = data.shape
# cell_count = rows * columns
# number_of_nulls = data.isnull().sum().sum()
# percentage_of_missing = (number_of_nulls / cell_count) * 100
# print(f'Percentage of missing values: {percentage_of_missing}%')
# data.head()

y = data['status']
X = data.drop('status', axis=1, inplace=False)
X = data.drop('Unnamed0', axis=1, inplace=False)
# X.describe()
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.2, random_state=42)

# mode='Explain' or 'Perform'
# ml_task = 'classification' or 'regression'
automl = AutoML(results_path='Perform_regression', mode='Perform', ml_task='regression')
automl.fit(X_train, y_train)

predictions = automl.predict(X_test)

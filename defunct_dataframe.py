import requests
import re
import pandas as pd
import pandas_profiling as pp # pip install pandas_profiling
import numpy as np

''' read data into pandas and view'''
url = 'https://pennstateoffice365-my.sharepoint.com/:x:/g/personal/rjn5308_psu_edu/EZ-qWOeA5jxNkKXpwdWk_CoB-rCxrvsYcdhHaqzLfWruAQ?e=6inkuL&download=1'
r = requests.get(url)
r.status_code
with open('data.csv', 'w') as fid:
    fid.write(r.text)

''' read data into pandas and view'''
data = pd.read_csv('data_og.csv')

''' remove characters that will pose issues to read in'''
data = data.rename(columns = lambda x:re.sub('[^A-Za-z0-9_]+', '', x)) # issue with json

'''describe data but include objects here'''
data.describe(include=object)












'''####################################################################################'''
'''other cleaning measures'''
#data = data.loc[:,~data.columns.duplicated()] # if duplicates

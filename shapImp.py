import os
import glob
import numpy as np
import matplotlib.pyplot as plt
import markdown
import pandas as pd
import re
from bs4 import BeautifulSoup
import shutil

foldList = [
    '/Users/rebeccanapolitano/PycharmProjects/hurricane_pred/2023_6_9_reg_noStatus_noUnc_noGolden_rand/2_DecisionTree']

# MAKE THE FEATURE PLOTS

fileList = []

# Extract the last part of each folder name
folder_names = [os.path.basename(folder_path) for folder_path in foldList]
csv_names = []

# Get the list of files matching the pattern 'learner_fold_*_importance.csv' in the specified folder
for i, folder in enumerate(foldList):
    # Create the pattern
    pattern = os.path.join(folder, 'learner_fold_*_shap_importance.csv')
    # Get the list of files matching the pattern
    files = glob.glob(pattern)
    # Remove files with 'shap' in their names
    # files = [file for file in files if 'shap' not in file]
    # Add the files to the list of files
    fileList.extend(files)

    # Create an empty DataFrame with 'feature' as the index
    df = pd.DataFrame(index=[], columns=['feature'])

    for j, file in enumerate(fileList):
        # Read the CSV file and extract the mean_importance column
        data = pd.read_csv(file)
        feature = data['feature']
        shap_importance = data['shap_importance']

        # Create a temporary DataFrame with 'feature' and 'shap_importance' columns
        temp_df = pd.DataFrame({'feature': feature, 'shap_importance_learner_' + str(j): shap_importance})

        # Merge the temporary DataFrame with the main DataFrame using 'feature' as the index
        df = pd.merge(df, temp_df, on='feature', how='outer')

    # Compute the average and standard deviation across learner columns
    learner_columns = [col for col in df.columns if 'learner' in col]
    df['average'] = df[learner_columns].mean(axis=1)
    df['dev'] = df[learner_columns].std(axis=1)

    # Calculate the average value for the feature 'random'
    random_average = df.loc[df['feature'] == 'random', 'average'].values[0]

    # Filter the DataFrame to include only rows with average greater than random_average
    filtered_df = df[df['average'] > random_average]

    # Get the feature names for the filtered rows
    feature_names = filtered_df['feature']
    num_features = len(feature_names)

    # Create equally spaced y-values
    y_values = np.arange(num_features)

    # Plot scatter plot for each filtered row
    fig, ax = plt.subplots()
    ax.errorbar(filtered_df['average'], y_values, xerr=filtered_df['dev'], fmt='o', capsize=5, color='black')
    ax.set_ylabel('Feature')
    ax.set_xlabel('Average')
    #foldName = os.path.basename(folder)
    foldName = 'Decision Tree'
    ax.set_title(foldName+' SHAP Importance (Average > Random)')

    # Set y-tick labels to feature names
    ax.set_yticks(y_values)
    ax.set_yticklabels(feature_names)
    ax.tick_params(axis='y', length=0)

    # Adjust layout to avoid cutoff of feature names
    plt.tight_layout()

    # Remove white space and make axes tight
    plt.autoscale()

    plt.show()

import os
import glob
import numpy as np
import matplotlib.pyplot as plt
import markdown
import pandas as pd
import re
from bs4 import BeautifulSoup
import shutil

experimentName = 'golden'


foldList = [
            '/Users/rebeccanapolitano/PycharmProjects/hurricane_pred/2023_6_9_reg_noStatus_noUnc_Golden_rand/5_Default_RandomForest_GoldenFeatures'
            ]

fileList = []

# Extract the last part of each folder name
folder_names = [os.path.basename(folder_path) for folder_path in foldList]
csv_names = []

# Get the list of files matching the pattern 'learner_fold_*_importance.csv' in the specified folder
for i, folder in enumerate(foldList):
    # Create the pattern
    pattern = os.path.join(folder, 'learner_fold_*_importance.csv')
    # Get the list of files matching the pattern
    files = glob.glob(pattern)
    # Remove files with 'shap' in their names
    files = [file for file in files if 'shap' not in file]
    # Add the files to the list of files
    fileList.extend(files)

    # Initialize an empty dataframe
    df = pd.DataFrame()

    # Iterate over each file and read its contents into a dataframe
    for file in fileList:
        # Read the CSV file and extract the mean_importance column
        data = pd.read_csv(file)
        mean_importance = data['mean_importance']
        # Append the mean_importance column to the main dataframe
        df = pd.concat([df, mean_importance], axis=1)

    # Calculate the mean of each row in the DataFrame
    row_mean = np.mean(df.values, axis=1)
    # Reshape the row_mean array into a column
    row_mean = np.reshape(row_mean, (-1, 1))

    # name csv file
    csv_names.append(folder_names[i] + '_row_mean.csv')

    file = csv_names[i]
    fileLoc = experimentName + '/' + file

    # if first time, we need to write the feature names too
    if i == 0:
        # Delete the folder if it already exists
        if os.path.exists(experimentName):
            shutil.rmtree(experimentName)
        # Create the folder
        os.makedirs(experimentName, exist_ok=True)
        df2 = pd.DataFrame()
        df2['feature'] = data['feature']

    df2['row_mean'] = row_mean
    df2.to_csv(fileLoc, index=False)

# Construct the pattern to match CSV files
pattern = f'{experimentName}/*.csv'

# Get a list of CSV file paths in the folder
csv_files = glob.glob(pattern)

# ^^ works

# Initialize an empty DataFrame to store the feature names and row means
synthesized_df = pd.DataFrame()

for i, file_path in enumerate(csv_files):
    # Read the CSV file into a DataFrame
    stripstring = '_row_mean.csv'
    name = os.path.basename(file_path).strip(stripstring)
    df = pd.read_csv(file_path, header=None, names=['feature', name])
    # Sort the DataFrame by the 'feature' column
    df.sort_values('feature', inplace=True)
    if i == 0:
        # take feature names and the values
        synthesized_df = synthesized_df.append(df)
    else:
        # just add the values this time
        # Concatenate the new column onto the existing DataFrame
        synthesized_df = pd.concat([synthesized_df, df[name]], axis=1)

# synthesized_df.reset_index(drop=True, inplace=True)
# synthesized_df.columns

# Threshold value
# Define the dictionary for thresholds
thresholds = {}

# Iterate over each column (dataset) in the DataFrame
for column in synthesized_df.columns:
    # Get the threshold value from the 'random' row in the current column
    threshold_value = synthesized_df.loc[synthesized_df['feature'] == 'random', column].values
    # Add the threshold value to the dictionary with the column name as the key
    thresholds[column] = threshold_value

# Drop the row where 'feature' is 'feature'
synthesized_df = synthesized_df[synthesized_df['feature'] != 'feature']
synthesized_df.dropna(inplace=True)

# Select numeric columns
numeric_columns = synthesized_df.columns[1:]

# Convert numeric columns to numeric data type
synthesized_df[numeric_columns] = synthesized_df[numeric_columns].apply(pd.to_numeric, errors='coerce')

# Set the feature names as the y-axis labels
features = synthesized_df['feature']
y_pos = np.arange(len(features))

# Set the dataset names and corresponding values
datasets = synthesized_df.columns[1:]
values = synthesized_df.iloc[:, 1:].values

thresh_row = synthesized_df['feature'] == 'random'
thresh_val = synthesized_df.loc[thresh_row, :].values[:, 1:]
above_thresh = np.any(synthesized_df.iloc[:, 1:] > thresh_val, axis=1)
filtered_df = pd.DataFrame(synthesized_df.loc[above_thresh, :].iloc[:, 1:].values, columns=datasets,
                           index=synthesized_df['feature'].loc[above_thresh])

fig, ax = plt.subplots()

filtered_df.plot.barh(ax=ax)

# Set the x-axis label
ax.set_xlabel('Values')

# Set the chart title
title = 'Feature Importance for ' + experimentName
ax.set_title(title)

# Add a legend
ax.legend()

# Adjust y-axis ticks
y_pos = np.arange(len(filtered_df))
ax.set_yticks(y_pos)
ax.set_yticklabels(filtered_df.index)

# Adjust left margin
plt.subplots_adjust(left=0.4)

# Save the plot as an image file (e.g., PNG)
png_name = experimentName + '_bars.png'
plt.savefig(png_name)

# MAKE THE TABLES

# what are the table values from each file (found in original read me)

#mainFolder = '/Users/rebeccanapolitano/PycharmProjects/hurricane_pred/2023_6_8_reg_noStatus_noUnc'
mainFolder = os.path.dirname(foldList[0])
markdown_file = mainFolder + '/README.md'

with open(markdown_file, 'r') as file:
    markdown_text = file.read()

# Convert the Markdown text to HTML
html = markdown.markdown(markdown_text)

# Find the first table using regular expressions
table_match = re.search(r'<p>(.*?)</p>', html, re.DOTALL)

if table_match is None:
    print("No table found in the Markdown file.")

# Extract the matched content
table_content = table_match.group(1)
rows = table_content.split('\n')

# Split each row into cells
data = [row.split('|') for row in rows]

# Create a DataFrame from the data
df = pd.DataFrame(data[1:], columns=data[0])
# Remove whitespace from column names
df = df.rename(columns=lambda x: x.strip())

folder_names = [str(folder).split('/')[-1] for folder in foldList]

# Create an empty DataFrame to store the selected columns
selected_columns_df = pd.DataFrame()

# Iterate over the folder names
for name_value in folder_names:
    name_value = name_value + '/'
    # Filter the DataFrame based on the presence of 'name' in the 'name' column
    selected_row = df[df['name'].str.contains(name_value)]

    if selected_row.empty:
        print(f"No row with name '{name_value}' found.")
        continue

    # Select specific columns from selected_row DataFrame
    selected_columns = selected_row[['model_type', 'metric_value', 'train_time']]

    # what are the hyperparameters for each model (found in individual read me)
    markdown_file = mainFolder + '/' + name_value + 'README.md'

    with open(markdown_file, 'r') as file:
        markdown_text = file.read()

    # Convert the Markdown text to HTML
    html = markdown.markdown(markdown_text)

    # Assuming 'html' contains the HTML content
    soup = BeautifulSoup(html, 'html.parser')

    # Find the first <ul> tag in the HTML
    ul_tag = soup.find('ul')

    # Extract the list items from the <ul> tag
    list_items = ul_tag.find_all('li')

    # Extract the text content from each list item
    result_list = ', '.join([item.text.strip() for item in list_items])

    # Append selected columns to the selected_columns_df
    selected_columns['hyperparams'] = result_list
    selected_columns_df = selected_columns_df.append(selected_columns)


# Write the selected columns to a CSV file
table_name = experimentName + '_table.csv'
selected_columns_df.to_csv(table_name, index=False)

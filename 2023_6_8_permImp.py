import pandas as pd
import os
import glob
import numpy as np
import matplotlib.pyplot as plt

experimentName = 'baseLine'

foldList = ['/Users/rebeccanapolitano/PycharmProjects/hurricane_pred/2023_6_8_reg_noStatus_noUnc/2_DecisionTree',
            '/Users/rebeccanapolitano/PycharmProjects/hurricane_pred/2023_6_8_reg_noStatus_noUnc/3_Default_Xgboost']
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
threshold = 0.005

# ---------------------------
# Drop the row where 'feature' is 'feature'
synthesized_df = synthesized_df[synthesized_df['feature'] != 'feature']
synthesized_df.dropna(inplace=True)

# Select numeric columns
numeric_columns = synthesized_df.columns[1:]

# Convert numeric columns to numeric data type
synthesized_df[numeric_columns] = synthesized_df[numeric_columns].apply(pd.to_numeric, errors='coerce')

# Check threshold condition for numeric columns
condition = synthesized_df[numeric_columns].abs() > threshold

# Filter rows based on the condition
df_filtered = synthesized_df[condition.any(axis=1)]
# ---------------------------

df = df_filtered
# Set the feature names as the y-axis labels
features = df['feature']
y_pos = np.arange(len(features))

# Set the dataset names and corresponding values
datasets = df.columns[1:]
values = df.iloc[:, 1:].values

# Set the colors for the bars
colors = ['blue', 'green', 'orange']



# Plot the horizontal bar chart
fig, ax = plt.subplots()
for i, dataset in enumerate(datasets):
    ax.barh(y_pos, values[:, i], label=dataset)

# Increase the left margin of the plot
plt.subplots_adjust(left=0.4)

# Set the y-axis labels
ax.set_yticks(y_pos)
ax.set_yticklabels(features)

# Set the x-axis label
ax.set_xlabel('Values')

# Set the chart title
ax.set_title('Horizontal Bar Chart')

# Add a legend
ax.legend()

# Show the plot
plt.show()

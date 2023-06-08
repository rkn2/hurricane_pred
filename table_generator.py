import markdown
import os
import pandas as pd
import re

foldList = ['/Users/rebeccanapolitano/PycharmProjects/hurricane_pred/2023_6_8_reg_noStatus_noUnc/2_DecisionTree',
            '/Users/rebeccanapolitano/PycharmProjects/hurricane_pred/2023_6_8_reg_noStatus_noUnc/3_Default_Xgboost']

# what are the table values from each file (found in original read me)

mainFolder = '/Users/rebeccanapolitano/PycharmProjects/hurricane_pred/2023_6_8_reg_noStatus_noUnc'
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

# need to do in a loop later PICK UP HERE BECCA - - - - - - - - -- - - -

name_value = '2_DecisionTree'

# Filter the DataFrame based on the presence of 'name' in the 'name' column
selected_row = df[df['name'].str.contains(name_value)]

if selected_row.empty:
    print(f"No row with name '{name_value}' found.")

# Select specific columns from selected_row DataFrame
selected_columns = selected_row[['model_type', 'metric_value', 'train_time']]

# Write selected columns to a CSV file
selected_columns.to_csv('data_table.csv', index=False)


# what are the hyperparameters for each model (found in individual read me)

import pandas as pd
import os

#Create a sample dataframe with column names
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']}

df = pd.DataFrame(data)

#Adding new row to df for v2
new_row_loc = {'Name': 'V2', 'Age':20,'City':'pune'}
df.loc[len(df.index)] = new_row_loc

new_row_loc2 = {'Name': 'V7', 'Age':59,'City':'vns'}
df.loc[len(df.index)] = new_row_loc2

#Ensure the "data" directory exists at the root level
data_dir = 'data'
os.makedirs(data_dir, exist_ok=True) 

#Define the path 
file_path = os.path.join(data_dir, 'sample_data.csv')
#Save the dataframe to a CSV file
df.to_csv(file_path, index=False)

print(f"CSV file saved to {file_path}")
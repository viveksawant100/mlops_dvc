import pandas as pd
import os

# Create sample dataframe with columns names 
data = {'Name': ['Ram','Sham','Gyan'], 'Age': [20,25,30], 'City': ["Pune", "Mumbai", "Patna"] }

df = pd.DataFrame(data)


# Check root directory 
data_dir= 'data'
os.makedirs(data_dir,exist_ok=True)


# Define file path 
file_path = os.path.join(data_dir, 'sample_data.csv')

# Save the dataframe to CSV file , including column names
df.to_csv(file_path, index=False)

print(f"csv file saved in {file_path}")
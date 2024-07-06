import pandas as pd

# Define the file paths
csv_file_path = r'D:\projects\hr_analytics\HR_Analytics.csv'
excel_file_path = r'D:\projects\hr_analytics\HR_Analytics.xlsx'

# Read the CSV file
df = pd.read_csv(csv_file_path)

# Write to Excel file
df.to_excel(excel_file_path, index=False)

print("Conversion complete!")

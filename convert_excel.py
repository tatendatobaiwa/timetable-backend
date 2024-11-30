import pandas as pd

# Load the Excel file
excel_file = 'timetable.xlsx'  # Replace with your Excel file path

# Read the Excel file
df = pd.read_excel(excel_file)

# Save it as a CSV file
df.to_csv('output_file.csv', index=False)  # Replace with your desired output file name

print("Excel file has been converted to CSV successfully!")

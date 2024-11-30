import pandas as pd

excel_file = 'timetable.xlsx'  # 

df = pd.read_excel(excel_file)

df.to_csv('output_file.csv', index=False)  

print("Excel file has been converted to CSV successfully!")

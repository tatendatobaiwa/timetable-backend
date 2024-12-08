import openpyxl
import pandas as pd

def excel_to_csv_with_merged_cells(input_excel, output_csv):
    # Load the workbook and select the active worksheet
    workbook = openpyxl.load_workbook(input_excel)
    sheet = workbook.active

    # Create a dictionary to store the data
    data = []

    # Iterate through rows
    for row in sheet.iter_rows():
        row_data = []
        for cell in row:
            # Check if the cell is part of a merged range
            if cell.coordinate in sheet.merged_cells:
                # Find the value of the merged cell
                for merged_range in sheet.merged_cells.ranges:
                    if cell.coordinate in merged_range:
                        # Get the top-left cell's value
                        top_left_cell = merged_range.start_cell
                        row_data.append(top_left_cell.value)
                        break
            else:
                row_data.append(cell.value)
        data.append(row_data)

    # Convert the data into a DataFrame
    df = pd.DataFrame(data)

    # Save the DataFrame to a CSV file
    df.to_csv(output_csv, index=False, header=False)
    print(f"CSV file saved: {output_csv}")

# Example usage
input_excel = "timetable.xlsx"  # Replace with your Excel file path
output_csv = "timetable.csv"    # Desired output CSV file path
excel_to_csv_with_merged_cells(input_excel, output_csv)

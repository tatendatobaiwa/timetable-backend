import csv
import json

def link_cells_to_colors(csv_file, colors_file):
    # Load the CSV data
    with open(csv_file, 'r', encoding='utf-8') as csv_in:
        csv_reader = list(csv.reader(csv_in))

    # Load the color data
    with open(colors_file, 'r', encoding='utf-8') as json_in:
        color_data = json.load(json_in)

    # Link cells to colors
    linked_data = []
    for row_idx, row in enumerate(csv_reader):
        linked_row = []
        for col_idx, cell_value in enumerate(row):
            # Get the corresponding color
            cell_color = color_data[row_idx][col_idx] if row_idx < len(color_data) and col_idx < len(color_data[row_idx]) else None
            # Create a dictionary with the value and color
            linked_row.append({"value": cell_value, "color": cell_color})
        linked_data.append(linked_row)

    return linked_data

# Example usage
linked_data = link_cells_to_colors('hhhhhhhh.csv', 'colors.json')

# Display linked data
for row in linked_data:
    print(row)

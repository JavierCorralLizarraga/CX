import pandas as pd
from openpyxl.utils import column_index_from_string

def read_excel_column(excel_filename, column_letter):
    # Read the Excel file into a DataFrame
    df = pd.read_excel(excel_filename)
    
    # Convert column letter to index
    column_index = column_index_from_string(column_letter) - 1
    
    # Extract column data
    column_data = df.iloc[:, column_index]
    
    return column_data

# Example usage:
excel_filename = "example.xlsx"
column_letter = "B"
result_column_data = read_excel_column(excel_filename, column_letter)
print(result_column_data)


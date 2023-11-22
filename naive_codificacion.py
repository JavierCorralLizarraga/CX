import os
import pandas as pd
from unidecode import unidecode

# Assume you have a function to read a specific column from Excel
def read_excel_column(file_path, column_letter):
    column_index = column_index_from_string(column_letter) - 1
    return pd.read_excel(file_path).iloc[:, column_index]

# Get the path to the 'palancas' directory within the script's directory
script_directory = os.path.dirname(os.path.realpath(__file__))
palancas_directory = os.path.join(script_directory, 'palancas')

# Count the number of .txt files in the 'palancas' directory
num_palancas = sum(1 for file in os.listdir(palancas_directory) if file.endswith(".txt"))

# Reading palancas from files in the 'palancas' directory
palancas = []
for i in range(1, num_palancas + 1):
    palanca_file_path = os.path.join(palancas_directory, f'p{i}.txt')
    with open(palanca_file_path) as file:
        palancas.append(list(map(lambda x: unidecode(x).lower(), file.read().split())))

A = 'EM'
column_letter = A

# Assume 'bbva_abc.xlsx' is the Excel file path
file_path = 'bbva_abc.xlsx'

# Reading data from Excel using the custom function
serie = read_excel_column(file_path, column_letter)
irenes = read_excel_column(file_path, 'E')

# Applying normalization in a single line
serie = serie.astype(str).apply(lambda x: unidecode(x).lower())

# Define functions
def is_nah(txt):
    return len(txt) <= 3 or 'xx' in txt or txt == '...'

def is_palanca(txt, palanca):
    return any(keyword in txt for keyword in palanca)

# Create DataFrame
df = pd.DataFrame()
df['verbalizaciones'] = serie
df['nas'] = serie.apply(is_nah)
df['irene'] = irenes
df = df.dropna()

# Check if each palanca is present in the verbalization
for i in range(num_palancas):
    df[f'p{i+1}'] = serie.apply(is_palanca, palanca=palancas[i])

# Check if none of the palancas are present
p_cols = [f'p{i+1}' for i in range(num_palancas)]
df['ninguna_palanca'] = df[p_cols].apply(lambda row: all(not val for val in row), axis=1)

# Combine all palancas into a single column
df['condensed_all'] = df[p_cols].apply(lambda row: ','.join([col for col, val in zip(p_cols, row) if val]), axis=1)

# Split the combined palancas into a list
df['cond_list'] = df['condensed_all'].apply(lambda x: x.split(','))

# Reverse the list of palancas
df['cond_rev'] = df['cond_list'].apply(lambda x: list(reversed(x)))

# Combine the reversed list into a single string
df['cond_rev1'] = df['cond_rev'].apply(lambda x: ','.join(x))

# Save the DataFrame to an Excel file
df.to_excel(f"palancas_{column_letter}.xlsx")


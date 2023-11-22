from ast import literal_eval
import pandas as pd

def verticales(input_file='pal_A.xlsx'):
    # Read Excel file
    df = pd.read_excel(input_file)

    # Convert string representation of list to actual list
    df['cond_list'] = df['cond_list'].apply(literal_eval)

    # Explode DataFrame based on 'cond_list'
    df = df.explode('cond_list', ignore_index=False)

    # Exclude the first row
    df = df.iloc[1:]

    # Calculate and save overall percentages
    porcentajes_general = df['cond_list'].value_counts(normalize=True) * 100
    porcentajes_general.to_excel('pcts_general.xlsx')

    # Filter DataFrame for irene >= 9 and calculate and save percentages
    df_aux_promotores = df[df['irene'] >= 9]
    porcentajes_promotores = df_aux_promotores['cond_list'].value_counts(normalize=True) * 100
    porcentajes_promotores.to_excel('pcts_promoters.xlsx')

    # Filter DataFrame for irene < 9 and calculate and save percentages
    df_aux_pas_det = df[df['irene'] < 9]
    porcentajes_pas_det = df_aux_pas_det['cond_list'].value_counts(normalize=True) * 100
    porcentajes_pas_det.to_excel('pcts_pas_det.xlsx')

    # Save the modified DataFrame to Excel
    df.to_excel('verticales.xlsx')

# Call the function with the default input file or provide a different file name
verticales()


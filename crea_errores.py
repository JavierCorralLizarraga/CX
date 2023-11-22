import pandas as pd

def crea_errores(irene_df, confidence_interval, total_population):
    # Calculate errors using error_muestreo function
    errors = pd.Series(
        error_muestreo(
            total_population,
            irene_df['muestra'],
            irene_df['% promotores'],
            irene_df['% detractores'],
            confidence_interval
        )
    )

    # Combine errors with the original DataFrame
    irene_df = pd.concat([irene_df, errors], axis=1)
    irene_df = irene_df.rename(columns={0: "error"})

    # Calculate upper and lower bounds of Irene plus/minus error
    irene_df['irene_mas_error'] = irene_df['irene'] + irene_df['error']
    irene_df['irene_menos_error'] = irene_df['irene'] - irene_df['error']

    return irene_df

# Example usage:
# Assuming you have an existing DataFrame named 'irene_data' with columns 'muestra', '% promotores', '% detractores', and 'irene'
irene_data = pd.DataFrame({
    'muestra': [100, 150, 200],
    '%_promotores': [20, 25, 30],
    '%_detractores': [10, 15, 18],
    'irene': [10, 10, 10],  # Assuming you have 'irene' column
})

confidence_interval = 90
total_population = 10000  # Replace with the actual total population

result_with_errors = crea_errores(irene_data, confidence_interval, total_population)
print(result_with_errors)


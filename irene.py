import pandas as pd
import numpy as np

def calc_irene(vector, nps_sets):
    # Extract sets from the dictionary
    promoter_list = nps_sets.get('promoters', [])
    detractor_list = nps_sets.get('detractors', [])
    passive_list = nps_sets.get('pasives', [])

    # Calculate counts
    promoters = sum(value in promoter_list for value in vector)
    detractors = sum(value in detractor_list for value in vector)
    pasives = sum(value in passive_list for value in vector)

    # Calculate percentages directly
    total = len(vector)
    prom_percentage = (promoters / total) * 100
    det_percentage = (detractors / total) * 100
    pas_percentage = (pasives / total) * 100

    # Calculate Irene score
    irene = prom_percentage - det_percentage

    # Create DataFrame with column names replaced
    layout = pd.DataFrame({
        'muestra': [total],
        'irene': [irene],
        '#_promotores': [promoters],
        '%_promotores': [prom_percentage],
        '#_pasivos': [pasives],
        '%_pasivos': [pas_percentage],
        '#_detractores': [detractor],
        '%_detractores': [det_percentage],
    })

    return layout

# Example usage:
nps_sets = {'promoters': [9, 10], 'detractors': [1, 2, 3, 4, 5, 6], 'pasives': [7, 8]}
nps_sets_emoji = {'promoters': [😊, 😍], 'detractors': [😡, 😟], 'pasives': [😐]}
nps_sets_ces = {'promoters': [4, 5], 'detractors': [1,2], 'pasives': [3]}
irene_result = calc_irene(my_vector, nps_sets)
print(irene_result)


from scipy.stats import norm
from math import sqrt

def error_muestreo(population, sample, promoters, detractors, confidence_interval=80, prom_detract_are_percentages=True):
    if prom_detract_are_percentages:
        # Convert percentages to fractions
        promoters /= 100
        detractors /= 100

    confidence_interval /= 100
    
    # Adjust confidence interval for two-tailed test
    confidence_interval += ((1 - confidence_interval) / 2)
    
    # Print adjusted confidence interval
    print(confidence_interval)
    
    # Calculate the common term
    common_term = norm.ppf(confidence_interval) ** 2 * (
        (promoters * (1 - promoters)) +
        (detractors * (1 - detractors)) +
        (2 * promoters * detractors)
    )

    # Calculate error based on population size
    if population <= 10000:
        # For small populations
        # print("Population <=10,000")
        error = 100 * sqrt((common_term * (population / sample - 1)) / (population - 1))
    else:
        # For large populations
        # print("Population >10,000")
        error = 100 * sqrt(common_term / sample)
    
    return error

# Example usage:
population = 15000
sample = 1000
promoters_pct = 20
detractors_pct = 10

# Using default confidence_interval=80 and assuming percentages
error_result_percentage = error_muestreo(population, sample, promoters_pct, detractors_pct)
print("Sampling Error (Percentages):", error_result_percentage)

# Assuming promoters and detractors are provided as numbers (counts)
error_result_numbers = error_muestreo(population, sample, promoters=200, detractors=100, prom_detract_are_percentages=False)
print("Sampling Error (Numbers):", error_result_numbers)


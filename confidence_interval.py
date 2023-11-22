import numpy as np
import scipy.stats

def calculate_confidence_interval(sample, promoters, detractors, m_error, population=10_001):
    # Check population size
    if population <= 10_000:
        print("Population size <= 10,000")
        
        # Calculate Z-score for small populations
        Z = np.sqrt(((sample * (m_error / 100) ** 2 * (population - 1)) /
                     (population * (((promoters / 100) * (1 - (promoters / 100))) +
                                 ((detractors / 100) * (1 - (detractors / 100))) +
                                 (2 * (promoters / 100) * (detractors / 100)))) /
                     (1 - sample / population)))
    else:
        print("Population size > 10,000")
        
        # Calculate Z-score for large populations
        Z = np.sqrt((sample /
                     (((promoters / 100) * (1 - (promoters / 100))) +
                      ((detractors / 100) * (1 - (detractors / 100))) +
                      (2 * (promoters / 100) * (detractors / 100)))) ** 2) * (m_error / 100)

    # Calculate Confidence Interval
    CI = 100 * scipy.stats.norm.cdf(Z)
    return CI

# Example usage:
sample = 500
promoters = 25
detractors = 10
m_error = 2.5
population = 15_000

confidence_interval = calculate_confidence_interval(sample, promoters, detractors, m_error, population)
print("Confidence Interval:", confidence_interval)


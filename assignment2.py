import numpy as np

def stat():
    # Load data and skip the first row (the headers)
    data = np.loadtxt('populations.txt', skiprows=1)
    
    # Hare column (index 1)
    hare = data[:, 1]
    
    # Year with the lowest hare population
    min_year_hare = data[np.argmin(hare), 0]
    
    # Average of Lynx population (index 2)
    lynx_avg = np.mean(data[:, 2])
    
    # Add a column for the sum of species (Hare + Lynx + Carrot)
    # data[:, 1:] takes all columns except the year
    species_sum = np.sum(data[:, 1:], axis=1, keepdims=True)
    new_data = np.append(data, species_sum, axis=1)
    
    # Set Carrot population (index 3) to 0 if below 40000
    new_data[new_data[:, 3] < 40000, 3] = 0
    
    return data, hare, min_year_hare, lynx_avg, new_data

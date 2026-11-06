import numpy as np

def skapa_data(antal=100):
    data = np.random.uniform(0, 100, antal)
    return data

def skapa_heltal(antal=100):
    data = np.random.randint(0, 100, antal)
    return data

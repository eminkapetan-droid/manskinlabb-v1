from data import skapa_data
from diagram import visa_histogram
data = skapa_data()
print("Antal värden:", len(data))
print("Första tio värdena:", data[:10])
visa_histogram(data)

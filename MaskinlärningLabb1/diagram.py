import matplotlib.pyplot as plt
def visa_histogram(data, titel="Histogram"):
    plt.hist(data, bins=10)
    plt.title(titel)
    plt.xlabel("Värde")
    plt.ylabel("Antal")
    plt.show()

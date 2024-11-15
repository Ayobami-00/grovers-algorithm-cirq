import matplotlib.pyplot as plt
from collections import Counter

def visualize_results(histogram):
    """
    Visualizes the measurement results.
    
    Parameters:
    histogram: A Counter or dict containing the measurement outcomes and their frequencies.
    """
    # Convert to a list of (state, frequency)
    states, counts = zip(*histogram.items())

    # Plot the histogram
    plt.bar(states, counts)
    plt.xlabel('Measured State')
    plt.ylabel('Frequency')
    plt.title("Grover's Algorithm Result")
    plt.show()

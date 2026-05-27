#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt


def frequency():
    np.random.seed(5)
    student_grades = np.random.normal(68, 15, 50)
    plt.figure(figsize=(6.4, 4.8))

    # Define bins every 10 units from 0 to 100
    bins = np.arange(0, 110, 10)

    # Plot the histogram with black outlines for the bars
    plt.hist(student_grades, bins=bins, edgecolor='black')

    # Add labels and title
    plt.xlabel('Grades')
    plt.ylabel('Number of Students')
    plt.title('Project A')

    # Set x-axis ticks to align with the bins
    plt.xticks(bins)

    # Display the plot
    plt.show()

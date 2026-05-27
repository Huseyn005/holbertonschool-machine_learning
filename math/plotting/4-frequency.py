#!/usr/bin/env python3
"""
Defines a function that plots a histogram of student grades
"""
import numpy as np
import matplotlib.pyplot as plt


def frequency():
    """
    Plots a histogram of student scores for Project A with bins every 10 units,
    black outlines on the bars, and customized axis labels and titles.
    """
    np.random.seed(5)
    student_grades = np.random.normal(68, 15, 50)
    plt.figure(figsize=(6.4, 4.8))

    # Calculate bins every 10 units based on the true range of the data
    min_grade = int(np.floor(min(student_grades) / 10) * 10)
    max_grade = int(np.ceil(max(student_grades) / 10) * 10)
    bins = np.arange(min_grade, max_grade + 10, 10)

    # Plot the histogram with black outlines
    plt.hist(student_grades, bins=bins, edgecolor='black')

    # Add descriptive labels and title
    plt.xlabel('Grades')
    plt.ylabel('Number of Students')
    plt.title('Project A')

    # Set the x-axis limits to align tightly with our dynamic bins
    plt.xlim(min_grade, max_grade)
    plt.xticks(np.arange(40, 110, 10))

    # Display the final plot layout
    plt.show()

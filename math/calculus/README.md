# Advanced Linear Algebra - Determinant

## Description
This project focuses on the implementation of core linear algebra concepts using Python without external libraries. The primary goal is to calculate the determinant of a square matrix using Laplace expansion.

## Files
* **0-determinant.py**: A function `def determinant(matrix):` that calculates the determinant of a matrix.
    * If `matrix` is not a list of lists, it raises a `TypeError`.
    * If `matrix` is not square, it raises a `ValueError`.
    * Handles the $0 \times 0$ matrix case `[[]]` by returning 1.

## Requirements
* All files are interpreted on Ubuntu 20.04 LTS using `python3` (version 3.8.10).
* All files follow `pycodestyle` (version 2.8.*).
* All modules and functions include documentation.
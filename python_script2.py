"""
Encore super simple!
"""

# Some imports
import numpy as np
import pandas as pd

# create a matrix 2 x 2
matrix = np.array([[1, 2, 3], [4, 5, 6]])

# Create a dataframe
data_frame = pd.DataFrame(matrix)

# Print stats
print("Voici des stats de bases: {}".format(data_frame.describe()))

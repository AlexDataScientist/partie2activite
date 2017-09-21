"""
Encore super simple!
"""

import numpy as np
import pandas as pd

matrix = np.array([[1, 2, 3], [4, 5, 6]])
data_frame = pd.DataFrame(matrix)
print("Voici des stats de bases: {}".format(data_frame.describe()))

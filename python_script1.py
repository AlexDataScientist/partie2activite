"""
Super simple!
"""
import numpy as np
 
a = -8 
b = 6

if a<b:
  print("Salut mec!") 
if np.abs(a) > np.abs(b):
  print("Valeur absolu de {} plus grande que valeur absolu de {}".format(a, b))

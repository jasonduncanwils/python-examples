from __future__ import division
import numpy as np
import urllib as ul
import pandas as pd

names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']

# Load CSV from URL using NumPy
url = "https://goo.gl/vhm1eU"
raw_data = ul.urlopen(url)
dataset1 = np.loadtxt(raw_data, delimiter=",")
print('====================================')
print("Rows:")
print(dataset1.shape[0])
print("Columns:")
print(dataset1.shape[1])
print("Age average:")
print(round(sum(dataset1[:, 7])/len(dataset1[:, 7]), 2))
print('====================================')
print(dataset1)
print('====================================')

# Load CSV from URL using Pandas
url = "https://goo.gl/vhm1eU"
dataset2 = pd.read_csv(url, names=names)
print('====================================')
print("Rows:")
print(dataset1.shape[0])
print("Columns:")
print(dataset1.shape[1])
print("Age average:")
print(round(sum(dataset2.age)/len(dataset2.age), 2))
print('====================================')
print(dataset2)
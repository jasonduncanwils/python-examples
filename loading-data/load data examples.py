# Load CSV (using python)
import csv
import numpy
filename = 'pima-indians-diabetes.data.csv'
raw_data = open(filename, 'rb')
reader = csv.reader(raw_data, delimiter=',', quoting=csv.QUOTE_NONE) x = list(reader)
data = numpy.array(x).astype('float')
print(data.shape)

# Load CSV
import numpy
filename = 'pima-indians-diabetes.data.csv' 
raw_data = open(filename, 'rb')
data = numpy.loadtxt(raw_data, delimiter=",") 
print(data.shape)

# Load CSV from URL using NumPy
import numpy
import urllib
url = "https://goo.gl/vhm1eU"
raw_data = urllib.urlopen(url)
dataset = numpy.loadtxt(raw_data, delimiter=",")
print(dataset.shape)

# Load CSV using Pandas
import pandas
filename = 'pima-indians-diabetes.data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class'] 
data = pandas.read_csv(filename, names=names)
print(data.shape)

# Load CSV using Pandas from URL
import pandas
url = "https://goo.gl/vhm1eU"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class'] 
data = pandas.read_csv(url, names=names)
print(data.shape)

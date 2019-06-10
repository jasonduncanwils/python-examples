break_text = "\n ------------------------------ \n"
print(break_text)

# Peek at your data
# View first 20 rows
print("peek at the data")
import pandas
url = "https://goo.gl/vhm1eU"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class'] 
data = pandas.read_csv(url, names=names)
peek = data.head(20)
print(peek)
print(break_text)

# Dimensions of your data
print("Dimensions of the data")
import pandas
url = "https://goo.gl/vhm1eU"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class'] 
data = pandas.read_csv(url, names=names)
shape = data.shape
print(shape)
print(break_text)

# Data Types for Each Attribute
print("Data Types for Each Attribute")
import pandas
url = "https://goo.gl/vhm1eU"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class'] 
data = pandas.read_csv(url, names=names)
types = data.dtypes
print(types)
print(break_text)

# Statistical Summary
print("Statistical Summary")
import pandas
url = "https://goo.gl/vhm1eU"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class'] 
data = pandas.read_csv(url, names=names)
pandas.set_option('display.width', 100)
pandas.set_option('precision', 3)
description = data.describe()
print(description)
print(break_text)

# Class Distribution
print("Class Distribution")
import pandas
url = "https://goo.gl/vhm1eU"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class'] 
data = pandas.read_csv(url, names=names)
class_counts = data.groupby('class').size()
print(class_counts)
print(break_text)

# Pairwise Pearson correlations between data
print("Pairwise Pearson correlations between data")
import pandas
url = "https://goo.gl/vhm1eU"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class'] 
data = pandas.read_csv(url, names=names)
pandas.set_option('display.width', 100)
pandas.set_option('precision', 3)
correlations = data.corr(method='pearson')
print(correlations)
print(break_text)

# Skew for each attribute
# Knowing that an attribute has a skew may allow you to perform data preparation to 
# correct the skew and later improve the accuracy of your models. Values closer to zero show less skew.
print("Skew for each attribute")
import pandas
url = "https://goo.gl/vhm1eU"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class'] data = pandas.read_csv(url, names=names)
skew = data.skew()
print(skew)
print(break_text)
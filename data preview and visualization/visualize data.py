import matplotlib.pyplot as plt
import pandas
import numpy

#------------------------------------
url = "https://goo.gl/vhm1eU"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
visualize_type = "density"
#------------------------------------

data = pandas.read_csv(url, names=names)

# Univariate Histograms
if visualize_type == "histogram":
	data.hist()
	plt.show()
# Univariate Density Plots
elif visualize_type == "density":
	data.plot(kind='density', subplots=True, layout=(3,3), sharex=False) 
	plt.show()
# Box and Whisker Plots
elif visualize_type == "box_whiskers":
	data.plot(kind='box', subplots=True, layout=(3,3), sharex=False, sharey=False) 
	plt.show()
# Correction Matrix Plot
elif visualize_type == "corr_matrix_plot":
	correlations = data.corr()
	fig = plt.figure()
	ax = fig.add_subplot(111)
	cax = ax.matshow(correlations, vmin=-1, vmax=1)
	fig.colorbar(cax)
	ticks = numpy.arange(0,9,1)
	ax.set_xticks(ticks)
	ax.set_yticks(ticks)
	ax.set_xticklabels(names)
	ax.set_yticklabels(names)
	plt.show()
# Scatter Plot Matrix
elif visualize_type == "scatter":
	scatter_matrix(data)
	plt.show()
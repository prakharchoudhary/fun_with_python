# We will use the Wine dataset.

import pandas as pd
df_wine = pd.read_csv(
	'https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data',
	header=None)
#################################################################################
# process the dataset into 70:30 train-test split and scale using Standardization
#################################################################################

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

X, y= df_wine.iloc[:, 1:].values, df_wine.iloc[:, 0].values 
X_train, X_test, y_train, y_test = train_test_split(X, y,
													test_size=0.3,
													random_state=0
													)
sc = StandardScaler()
X_train_std = sc.fit_transform(X_train)
X_test_std = sc.fit_transform(X_test)

#################################################################################
# Construct the covariance matrix
#################################################################################

import numpy as np
import matplotlib.pyplot as plt

cov_mat = np.cov(X_train_std.T)							# compute the covariance matrix of the standardized training dataset
eigen_vals, eigen_vecs = np.linalg.eig(cov_mat)			# to obtain the eigenpairs of the Wine covariance matrix
# print('\nEigenvalues \n%s' % eigen_vals)

def var_exp_ratio(eigen_vals, eigen_vecs):
	tot = sum(eigen_vals)
	var_exp = [(i/tot) for i in sorted(eigen_vals, reverse=True)]
	cum_var_exp = np.cumsum(var_exp)					# calculate the cumulative sum of explained variances
	plt.bar(range(1,14), var_exp, alpha=0.5, align='center',
			label='individual explained variance')
	plt.step(range(1,14), cum_var_exp, where='mid',
			label='individual explained variance')
	plt.ylabel('Explained variance ratio')
	plt.xlabel('Principal components')
	plt.legend(loc='best')
	# plt.show()
	plt.savefig('./explained-variance-ratio.png', dpi=250)

#################################################################################
# FEATURE TRANSFORMATION
'''
Goals:
1. Sort the eigenpairs by descending order of values.
2. Construct a projection matrix from the selected eigenvectors.
3. use the projection matrix to transform the data onto the lower-dimensional subspace.
'''
#################################################################################


eigen_pairs = [(np.abs(eigen_vals[i]), eigen_vecs[:,i])
				for i in range(len(eigen_vals))]

eigen_pairs.sort(reverse=True)


'''
NOTE:
-> 	we collect the two eigenvectors that correspond to the two largest values to
	capture about 60 percent of the variance in this dataset.

->	In practice, the number of principal components has to be determined from a 
trade-off between computational efficiency and the performance of the classifier. 	
'''

w = np.hstack((eigen_pairs[0][1][:, np.newaxis], eigen_pairs[1][1][:, np.newaxis]))
# using above code, we have created a 13 * 2 dimensional projection matrix W from the top two eigenvectors.

# -> transforming the total 124x13-dimensional training set into 13x2-dimensional training set.
X_train_pca = X_train_std.dot(w)

def plot_pca_transform(X_train_pca):
	colors = ['r', 'b', 'g']
	markers = ['s', 'x', 'o']
	for l, c, m in zip(np.unique(y_train), colors, markers):
		plt.scatter(X_train_pca[y_train==l, 0],
					X_train_pca[y_train==l, 1],
					c=c, label=l, marker=m)
	plt.xlabel('PC 1')
	plt.ylabel('PC 2')
	plt.legend(loc='lower left')
	plt.savefig('./pca-transform-features.png', dpi=250)

def main():

	opt_string = '''
	Enter your choice:
	1. Export an explaned variance ratio chart for the features.
	2. Export the best two pca transformed features plotted on a chart. 
	'''
	while True:
		option = int(raw_input(opt_string))
		if option == 1:
			var_exp_ratio(eigen_vals, eigen_vecs)
			return
		elif option == 2:
			plot_pca_transform(X_train_pca)
			return
		else:
			print("Wrong choice! Choose 1 or 2.")
			continue

if __name__ == '__main__':
	main()
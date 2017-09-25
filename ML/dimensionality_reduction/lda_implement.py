# We will use the Wine dataset.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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
# Computing Scatter Matrices
#################################################################################
np.set_printoptions(precision=4)
mean_vecs = []
for label in range(1,4):
	mean_vecs.append(np.mean(
					X_train_std[y_train==label], axis=0))
	print('MV %s: %s\n'% (label, mean_vecs[label-1]))

d = 13 # number of features

#within-class scatter matrxi: S_W
S_W = np.zeros((d, d))
for label, mv in zip(range(1,4), mean_vecs):
	class_scatter = np.zeros((d, d))
	for row in X[y == label]:
		row, mv = row.reshape(d, 1), mv.reshape(d, 1)
		class_scatter += (row-mv).dot((row-mv).T)
	S_W += class_scatter

print('Within-class scatter matrix: %sx%s' % (S_W.shape[0], S_W.shape[1]))
print('Class label distribution: %s' % np.bincount(y_train)[1:])

d = 13 # number of features
S_W = np.zeros((d, d))
for label, mv in zip(range(1, 4), mean_vecs):
	class_scatter = np.cov(X_train_std[y_train==label].T)
	S_W += class_scatter
print('Scaled within-class scatter matrix: %sx%s' % (S_W.shape[0], S_W.shape[1]))

# Between-class matrix: S_B
mean_overall = np.mean(X_train_std, axis=0)
d = 13 # number of features
S_B = np.zeros((d, d))
for i,mean_vec in enumerate(mean_vecs):
	n = X[y==i+1, :].shape[0]
	mean_vec = mean_vec.reshape(d, 1)
	mean_overall = mean_overall.reshape(d, 1)
S_B += n * (mean_vec - mean_overall).dot((mean_vec - mean_overall).T)
print('Between-class scatter matrix: %sx%s' % (S_B.shape[0], S_B.shape[1]))

#################################################################################
# FEATURE TRANSFORMATION
#################################################################################

eigen_vals, eigen_vecs = np.linalg.eig(np.linalg.inv(S_W).dot(S_B))
eigen_pairs = [(np.abs(eigen_vals[i]), eigen_vecs[:,i]) for i in range(len(eigen_vals))]
eigen_pairs = sorted(eigen_pairs, key=lambda k: k[0], reverse=True)
print('Eigenvalues in decreasing order:\n')
for eigen_val in eigen_pairs:
	print(eigen_val[0])

##################################
#### explained-varince-ratio(lda)
##################################
def exp_var_ratio(eigen_vals):
	tot = sum(eigen_vals.real)
	discr = [(i/tot) for i in sorted(eigen_vals.real, reverse=True)]
	cum_discr = np.cumsum(discr)
	plt.bar(range(1, 14), discr, alpha=0.5, align='center', 
			label='individual "discriminability"')
	plt.step(range(1, 14), cum_discr, where='mid',
			label='cumulative "discriminability"')
	plt.ylabel('"discriminability" ratio')
	plt.xlabel('Linear Discriminants')
	plt.ylim([-0.1, 1.1])
	plt.legend(loc='best')
	plt.savefig('./chart/explained-varince-ratio(lda).png', dpi=200)
	# plt.show()

'''
stack the two most discriminative eigenvector columns to create the
transformation matrix W
'''
w = np.hstack((eigen_pairs[0][1][:, np.newaxis].real,
				eigen_pairs[1][1][:, np.newaxis].real))

######################################################
### Projecting samples onto the new feature space ####
'''
						X' = XW
'''
######################################################
def lda_transform_plot(X_train_std):	
	X_train_lda = X_train_std.dot(w)
	colors = ['r', 'b', 'g']
	markers = ['s', 'x', 'o']
	for l, c, m in zip(np.unique(y_train), colors, markers):
		plt.scatter(X_train_lda[y_train==l, 0],
					X_train_lda[y_train==l, 1],
					c=c, label=l, marker=m)
	plt.xlabel('LD 1')
	plt.ylabel('LD 2')
	plt.legend(loc='upper right')
	# plt.show()
	plt.savefig('./chart/lda-transform-features.png', dpi=250)


options = '''
Enter your choice:
1. Export the explained variance ratio plot.
2. Export the lda transform plot.
'''

def main():
	print(options)
	while True:
		option = int(raw_input("----> "))
		if option == 1:
			exp_var_ratio(eigen_vals)
			return
		elif option == 2:
			lda_transform_plot(X_train_std)
			return
		else:
			print("Wrong choice. Try again.\n")

if __name__ == '__main__':
	main()

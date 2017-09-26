"""
Seperating cocentric circles
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
from rbf_kernel_pca import rbf_kernel_pca
from sklearn.datasets import make_circles
from sklearn.decomposition import PCA

options = '''
Enter your choice:
1. Export the half moons plot.
2. Export standard pca transform of the data.
3. EXport rbf kernel pca transform of the data.
'''


def show_moons(X, y):
	plt.scatter(X[y==0, 0], X[y==0, 1],
				color='red', marker='^', alpha=0.5)
	plt.scatter(X[y==1, 0], X[y==1, 1],
				color='blue', marker='o', alpha=0.5)
	# plt.show()
	plt.savefig('./charts/circles.png', dpi=200)
	plt.gcf().clear()

def scikit_std_pca(X, y):
	scikit_pca = PCA(n_components=2)
	X_spca = scikit_pca.fit_transform(X)
	fig, ax = plt.subplots(nrows=1,ncols=2, figsize=(7,3))

	ax[0].scatter(X_spca[y==0, 0], X_spca[y==0, 1],
				color='red', marker='^', alpha=0.5)
	ax[0].scatter(X_spca[y==1, 0], X_spca[y==1, 1],
				color='blue', marker='o', alpha=0.5)
	ax[1].scatter(X_spca[y==0, 0], np.zeros((500,1))+0.02,
				color='red', marker='^', alpha=0.5)
	ax[1].scatter(X_spca[y==1, 0], np.zeros((500,1))-0.02,
				color='blue', marker='o', alpha=0.5)
	ax[0].set_xlabel('PC1')
	ax[0].set_ylabel('PC2')
	ax[1].set_ylim([-1, 1])
	ax[1].set_yticks([])
	ax[1].set_xlabel('PC1')
	plt.savefig('./charts/std-pca-circles.png', dpi=200)
	plt.gcf().clear()

def kernel_pca_unfold(X, y):
	X_kpca = rbf_kernel_pca(X, gamma=15, n_components=2)
	fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(7,3))
	ax[0].scatter(X_kpca[y==0, 0], X_kpca[y==0, 1],
				color='red', marker='^', alpha=0.5)
	ax[0].scatter(X_kpca[y==1, 0], X_kpca[y==1, 1],
				color='blue', marker='o', alpha=0.5)
	ax[1].scatter(X_kpca[y==0, 0], np.zeros((500,1))+0.02,
				color='red', marker='^', alpha=0.5)
	ax[1].scatter(X_kpca[y==1, 0], np.zeros((500,1))-0.02,
				color='blue', marker='o', alpha=0.5)

	ax[0].set_xlabel('PC1')
	ax[0].set_ylabel('PC2')
	ax[1].set_ylim([-1, 1])
	ax[1].set_yticks([])
	ax[1].set_xlabel('PC1')
	plt.savefig('./charts/kernel-pca-circles.png', dpi=200)
	plt.gcf().clear()

def main():
	X, y = make_circles(n_samples=1000, random_state=123, noise=0.1, factor=0.2)
	while True:
		print(options)
		opt = int(raw_input('------>'))
		if opt == 1:
			show_moons(X, y)
			return 
		elif opt == 2:
			scikit_std_pca(X, y)
			return 
		elif opt == 3:
			kernel_pca_unfold(X, y)
			return 
		else:	print("Wrong choice\n"); continue
if __name__ == '__main__':
	main()
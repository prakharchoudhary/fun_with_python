"""
Projecting new points
"""
import numpy as np
from rbf_kernel_pca import rbf_kernel_pca
from sklearn.datasets import make_moons
import matplotlib.pyplot as plt

X, y = make_moons(n_samples=100, random_state=123)
alphas, lambdas = rbf_kernel_pca(X, gamma=15, n_components=1, eig=True)
x_new = X[25]
x_proj = alphas[25]	# original projection

def project_x(x_new, X, gamma, alphas, lambdas):
	pair_dist = np.array([np.sum(x_new-row)**2 
								for row in X])
	k = np.exp(-gamma * pair_dist)
	return k.dot(alphas / lambdas)

x_reproj = project_x(x_new, X,
			gamma=15, alphas=alphas, lambdas=lambdas)

plt.scatter(alphas[y==0, 0], np.zeros((50)),
			color='red', marker='^',alpha=0.5)
plt.scatter(alphas[y==1, 0], np.zeros((50)),
			color='blue', marker='o', alpha=0.5)
plt.scatter(x_proj, 0, color='black',
			label='original projection of point X[25]',
			marker='^', s=100)
plt.scatter(x_reproj, 0, color='green',
			label='remapped point X[25]',
			marker='x', s=500)
plt.legend(scatterpoints=1)
# plt.show()
plt.savefig('./charts/projecting-new-points.png', dpi=200)
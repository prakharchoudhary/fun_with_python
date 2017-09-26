"""
Implementing PCA from the sklearn library.
"""
from matplotlib import pyplot as plt
from sklearn.datasets import make_moons
from sklearn.decomposition import KernelPCA

X, y = make_moons(n_samples=100, random_state=123)
scikit_kpca = KernelPCA(n_components=2,
				kernel='rbf', gamma=15)
X_sklearnpca = scikit_kpca.fit_transform(X)

#### plotting the graph #####

plt.scatter(X_sklearnpca[y==0, 0], X_sklearnpca[y==0, 1],
			color='red', marker='^', alpha=0.5)
plt.scatter(X_sklearnpca[y==1, 0], X_sklearnpca[y==1, 1],
			color='blue', marker='o', alpha=0.5)
plt.xlabel('PC1')
plt.ylabel('PC2')
# plt.show()
plt.savefig('./charts/scikit-kernel-pca.png', dpi=200)

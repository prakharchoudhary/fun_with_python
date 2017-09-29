import numpy as np
from numpy.random import seed

class AdalineSGD(object):
	"""
	ADAptive LInear NEuron Classifier using Stochastic Gradient Descent
	
	Parameters
	-------------------------------------------------------------------

	eta: float
		Learning Rate (between 0.0 and 1.0)

	n_iter: int
		Passes over the training data


	Attributes
	-------------------------------------------------------------------

	w_: 1-d array
		Weights after fitting
	
	errors_ : list
		Number of misclassifications in every epoch

	shuffle : bool (default: True)
		Shuffles training data every epoch if True to prevent cycles.
	
	random_state : int (default: None)
		Set random state for shuffling and initializing the weights.
	"""

	def __init__(self, eta=0.01, n_iter=10,
					shuffle=True, random_state=None):
		
		self.eta = eta
		self.n_iter = n_iter
		self.w_initialized = True
		self.shuffle = shuffle
		if random_state:
			seed(random_state)

	def fit(self, X, y):
		"""Fit training data without reinitializing the weights."""
		
		if not self.w_initialized:
			self._initialize_weights(X.shape[1])

		if y.ravel().shape[0] > 1:
			for xi, target in zip(X, y):
				self._update_weights(xi, target)

		else:
			self._update_weights(X, y)

		return self

	def shuffle(self, X, y):
		"""Shuffle training data"""
		
		r = np.random.permutation(len(y))
		return X[r], y[r]

	def _initialize_weights(self, m):
		"""Initialize weights to zero"""

		self.w_ = np.zeros(1 + m)
		self.w_initialized = True

	def _update_weights(self, xi, target):
		"""Apply Adaline learning rule to update the weights"""

		output = self.net_input(xi)
		error = target - output
		self.w_[1:] += self.eta * xi.dot(error)
		self.w_[0] += self.eta * error
		cost = 0.5 * error**2
		return cost

	def net_input(self, X):
		"""Calculate net input"""

		return np.dot(X, self.w_[1:]) + self.w_[0]

	def activation(self, X):
		"""Computer linear activation"""

		return self.net_input(X)

	def predict(self, X):
		"""Return class label after unit step"""

		return np.where(self.activation(X) >= 0.0, 1,-1)

		 



import math
from matplotlib import pyplot as plt
import numpy as np
from scipy.misc import comb

def ensemble_error(n_classifier, error):
	k_start = math.ceil(n_classifier / 2.0)
	probs = [comb(n_classifier, k) * error**k * (1-error)**(n_classifier-k)
			for k in range(int(k_start), n_classifier+1)]
	return sum(probs)

print("Printing for an ensemble of 11 base classifiers each with error rate 0.25\n%f" 
	% ensemble_error(n_classifier=11, error=0.25))

def ensemble_error_visualize():
	error_range = np.arange(0.0, 1.01, 0.01)
	ens_errors = [ensemble_error(n_classifier=11, error=error)
				 for error in error_range]
	plt.plot(error_range, ens_errors,
			label='Ensemble error',
			linewidth=2)
	plt.plot(error_range, error_range,
		linestyle='--', label='Base error',
		linewidth=2)
	plt.xlabel('Base Error')
	plt.ylabel('Base/Ensemble error')
	plt.legend(loc='upper left')
	plt.grid()
	# plt.show()
	plt.savefig('./charts/ensemble-error-rates.png', dpi=200)

if __name__ == '__main__':
	ensemble_error_visualize()
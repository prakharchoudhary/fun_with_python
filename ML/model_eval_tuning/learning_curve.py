from load_breast_cancer_data import load_data
import matplotlib.pyplot as plt
import numpy as np
import os
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import learning_curve

# load and split the dataset
X_train, X_test, y_train, y_test = load_data()

pipe_lr = Pipeline([
			('scl', StandardScaler()),
			('clf', LogisticRegression(
							penalty='l2', random_state=0))])

train_sizes, train_scores, test_scores = \
			learning_curve(estimator=pipe_lr,
							X=X_train,
							y=y_train,
							train_sizes=np.linspace(0.1, 1.0, 10),
							# ---> use 10 evenly spaced relative
							# 	   intervals for the training set sizes.
							cv=10,
							n_jobs=1)
train_mean = np.mean(train_scores, axis=1)
train_std = np.std(train_scores, axis=1)
test_mean = np.mean(test_scores, axis=1)
test_std = np.std(test_scores, axis=1)

########### plotting for train_data #############
plt.plot(train_sizes, train_mean,
		color='blue', marker='o',
		markersize=5,
		label='training accuracy')
plt.fill_between(train_sizes,
				train_mean + train_std,
				train_mean - train_std,
				alpha=0.15, color='blue')

########### plotting for test_data #############
plt.plot(train_sizes, test_mean,
		color='green', linestyle='--',
		marker='s', markersize=5,
		label='validation accuracy')
plt.fill_between(train_sizes,
				test_mean + test_std,
				test_mean - test_std,
				alpha=0.15, color='green')

plt.grid()
plt.xlabel('Number of training samples')
plt.ylabel('Accuracy')
plt.legend(loc='lower right')
plt.ylim(0.8, 1.0)
# plt.show()
if not os.path.exists(os.path.join(os.getcwd(),'charts')):
	os.mkdir('charts')
plt.savefig('./charts/learning-curve.png', dpi=200)

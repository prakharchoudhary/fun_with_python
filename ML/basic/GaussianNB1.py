import numpy as np 
from sklearn.naive_bayes import GaussianNB

#this the dataset which will be used to train
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
Y = np.array([1, 1, 1, 2, 2, 2])

clf = GaussianNB()			#declaring a classifier
clf.fit(X, Y)				#training the classifier using the above dataset

p = [-1.2, 1.9]
pred = clf.predict([p])		#predict the class to which the point belongs

print pred 					#print the predicted class
"""
Implementation of the SBS algorithm on a KNN classifier.
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
from sbs import SBS

########################################### Download the datset ##############################################
df_wine = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data", header=None)
df_wine.columns = ['Class label', 'Alcohol',
	'Malic acid', 'Ash',
	'Alcalinity of ash', 'Magnesium',
	'Total phenols', 'Flavanoids',
	'Nonflavanoid phenols',
	'Proanthocyanins',
	'Color intensity', 'Hue',
	'OD280/OD315 of diluted wines',
	'Proline']

########################################### Split the datset ###########################################
X, y = df_wine.iloc[:, 1:].values, df_wine.iloc[:, 0].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

############################## Feature scaling(using standardization) ##################################
stdsc = StandardScaler()
X_train_std = stdsc.fit_transform(X_train)
X_test_std = stdsc.fit_transform(X_test)

############################## Implement Sequental Backward Selection using KNN #########################
knn = KNeighborsClassifier(n_neighbors=2)
sbs = SBS(knn, k_features=1)
sbs.fit(X_train_std, y_train)


############################ plot the classification accuracy of the KNN classifier #####################
k_feat = [len(k) for k in sbs.subsets_]
plt.plot(k_feat, sbs.scores_, marker='o')
plt.ylim([0.7, 1.1])
plt.ylabel('Accuracy')
plt.xlabel('Number of features')
plt.grid()
plt.show()
# plt.savefig('sbm_classification_using_knn.png', dpi=300)

############################ get the features that yield best performance ################################
k5 = list(sbs.subsets_[8])
print(df_wine.columns[1:][k5])

############ Performance of the KNN classifier on the original test set(with all features) ###############
knn.fit(X_train_std, y_train)
print('Training accuracy:', knn.score(X_train_std, y_train))
print('Test accuracy:', knn.score(X_test_std, y_test))

######## Performance of the KNN classifier on the original test set(with best feature subset) ###########
knn.fit(X_train_std[:, k5], y_train)
print('Training accuracy:', knn.score(X_train_std[:, k5], y_train))
print('Test accuracy:', knn.score(X_test_std[:, k5], y_test))
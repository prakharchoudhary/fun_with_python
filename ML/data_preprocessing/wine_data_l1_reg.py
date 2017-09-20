import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

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

########################################### Plot the graph ##############################################
fig = plt.figure()
ax = plt.subplot(111)
plt.subplots_adjust(right=0.68, bottom=0.22, top=0.95)
colors = ['blue', 'green', 'red', 'cyan',
		  'magenta', 'yellow', 'black',
		  'pink', 'lightgreen', 'lightblue',
		  'gray', 'indigo', 'orange']

weights, params = [], []
for c in np.arange(-4,6):
	lr = LogisticRegression(penalty='l1', C=10.**c, random_state=0)		# here we will find results for varying regularization strengths
	lr.fit(X_train_std, y_train)
	weights.append(lr.coef_[1])
	params.append(10.**c)

weights = np.array(weights)
for column, color in zip(range(weights.shape[1]), colors):
	plt.plot(params, weights[:, column],
			label=df_wine.columns[column+1],
			color=color)
plt.axhline(0, color='black', linestyle='--', linewidth=3)
plt.xlim([10.**(-5), 10**5])
plt.ylabel('weight coefficient')
plt.xlabel('C')
plt.xscale('log')
plt.legend(loc='upper left')
ax.legend(loc='upper center',
		  bbox_to_anchor=(1.38, 1.03),
		  ncol=1, fancybox=True)
# plt.show()
plt.savefig('l1_path.png', dpi=150)

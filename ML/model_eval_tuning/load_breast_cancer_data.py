"""

So let us load the breast cancer dataset:

1. Read dataset directly from the UCI website using pandas.
2. We assign the 30 features to a NumPy array X. Using LabelEncoder
   transform the class labels from their original string representation
   into integers.
3. Split the dataset into seperate training and test dataset.

"""
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

def load_data(): 
	df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/wdbc.data",
					header=None)

	X = df.loc[:, 2:].values
	y = df.loc[:, 1].values
	le = LabelEncoder()
	y = le.fit_transform(y)

	X_train, X_test, y_train, y_test = \
			train_test_split(X, y, test_size=0.2, random_state=1)

	return X_train, X_test, y_train, y_test

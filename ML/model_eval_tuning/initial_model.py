"""
Herein we will use the standard PCA to reduce our 30 dimensions to 2 dimensions;
and use LogisticRegression to train on the samples.

However rather than doing each step individually we will bind it using a Pipeline.
"""

from load_breast_cancer_data import load_data
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

# Build the pipeline
pipe_lr = Pipeline([('scl', StandardScaler()),
					('pca', PCA(n_components=2)),
					('clf', LogisticRegression(random_state=1))])

# load and split the dataset
X_train, X_test, y_train, y_test = load_data()

# fit the model
pipe_lr.fit(X_train, y_train)
print('Test Accuracy: %.3f' % pipe_lr.score(X_test, y_test))

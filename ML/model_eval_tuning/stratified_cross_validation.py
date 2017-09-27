from load_breast_cancer_data import load_data
import numpy as np
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import cross_val_score

# Build the pipeline
pipe_lr = Pipeline([('scl', StandardScaler()),
					('pca', PCA(n_components=2)),
					('clf', LogisticRegression(random_state=1))])

# load and split the dataset
X_train, X_test, y_train, y_test = load_data()

kfold = StratifiedKFold(n_splits=10,
						random_state=1).split(X_train, y_train)

########## manually scoring the cross validation score for each fold and finally finding cv accuracy ##########
scores = []
for k, (train, test) in enumerate(kfold):
	pipe_lr.fit(X_train[train], y_train[train])
	score = pipe_lr.score(X_train[test], y_train[test])
	scores.append(score)
	print('Fold: %s, Class dist.: %s, Acc: %.3f' % (k+1, 
		np.bincount(y_train[train]), score))

print('CV accuracy: %.3f +/- %.3f' % (np.mean(scores), np.std(scores)))

############################### using scikit-learn to calculate #########################################
print("\n" + "#"*100 + "\n")
scores = cross_val_score(estimator=pipe_lr,
                         X=X_train,
                         y=y_train,
                         cv=10,
                         n_jobs=1)
print('CV accuracy scores(using sklearn cross_val_score):\n%s' % scores)
print('CV accuracy: %.3f +/- %.3f' % (np.mean(scores), np.std(scores)))
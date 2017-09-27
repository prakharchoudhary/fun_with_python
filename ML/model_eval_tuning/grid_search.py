from load_breast_cancer_data import load_data
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC

X_train, X_test, y_train, y_test = load_data()
pipe_svc = Pipeline([('scl', StandardScaler()),
					 ('clf', SVC(random_state=1))])
param_range = [0.0001, 0.001, 0.01, 0.1, 1.0, 10.0, 100.0, 1000.0]
param_grid = [{'clf__C': param_range,
			   'clf__kernel': ['linear']},
			  {'clf__C': param_range,
			   'clf__gamma': param_range,
			   'clf__kernel': ['rbf']}]

gs = GridSearchCV(estimator=pipe_svc,
				  param_grid=param_grid,
				  scoring='accuracy',
				  cv=10,
				  n_jobs=-1)
gs = gs.fit(X_train, y_train)
print(gs.best_score_)
print(gs.best_params_)
clf = gs.best_estimator_
clf.fit(X_train, y_train)
print('Test accuracy: %.3f' % clf.score(X_test, y_test))

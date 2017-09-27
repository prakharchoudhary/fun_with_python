from load_breast_cancer_data import load_data
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline

# load and split the dataset
X_train, X_test, y_train, y_test = load_data()

# Building the confusion matrix
pipe_svc = Pipeline([('scl', StandardScaler()),
					 ('clf', SVC(random_state=1))])
pipe_svc.fit(X_train, y_train)
y_pred = pipe_svc.predict(X_test)
confmat = confusion_matrix(y_true=y_test, y_pred=y_pred)
print(confmat)

# plot the confusion matrix
fig, ax = plt.subplots(figsize=(2.5, 2.5))
ax.matshow(confmat, cmap=plt.cm.Blues, alpha=0.3)
for i in range(confmat.shape[0]):
	for j in range(confmat.shape[1]):
		ax.text(x=j, y=i,
				s=confmat[i, j],
				va='center', ha='center')

plt.xlabel('predicted label')
plt.ylabel('true label')
# plt.show()
plt.savefig('./charts/confusion_matrix.png', dpi=200)
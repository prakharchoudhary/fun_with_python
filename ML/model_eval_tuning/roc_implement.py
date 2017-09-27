from load_breast_cancer_data import load_data
from matplotlib import pyplot as plt
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold
from sklearn.pipeline import Pipeline
from sklearn.metrics import roc_curve, auc			# auc: area under curve
from scipy import interp							# roc_curve: Receiver Operator characteristic curve 
from sklearn.metrics import roc_auc_score, accuracy_score

# load and split the dataset
X_train, X_test, y_train, y_test = load_data()

# Building the confusion matrix
pipe_lr = Pipeline([
			('scl', StandardScaler()),
			('clf', LogisticRegression(
							penalty='l2', random_state=0))])

# Drawing the roc curve
X_train2 = X_train[:, [4, 14]]
cv = list(StratifiedKFold(n_splits=3,
					random_state=1).split(X_train2, y_train))
fig = plt.figure(figsize=(7, 5))
mean_tpr = 0.0
mean_fpr = np.linspace(0, 1, 100)
all_tpr = []
for i, (train, test) in enumerate(cv):
	probas = pipe_lr.fit(X_train2[train],
						y_train[train]).predict_proba(X_train2[test])
	fpr, tpr, thresholds = roc_curve(y_train[test],
									probas[:, 1],
									pos_label=1)
	mean_tpr += interp(mean_fpr, fpr, tpr)
	mean_tpr[0] = 0.0
	roc_auc = auc(fpr, tpr)
	plt.plot(fpr,
			tpr,
			lw=1,
			label='ROC fold %d (area = %0.2f)' % (i+1, roc_auc))

plt.plot([0, 1],
		 [0, 1],
		 color = (0.6, 0.6, 0.6),
		 label='random guessing')
mean_tpr /= len(cv)
mean_tpr[-1] = 1.0
mean_auc = auc(mean_fpr, mean_tpr)
plt.plot(mean_fpr, mean_tpr, 'k--',
		label='mean ROC (area = %0.2f)' % mean_auc, lw=2)
plt.plot([0, 0, 1],
		[0, 1, 1],
		lw=2,
		linestyle=':',
		color='black',
		label='perfect performance')
plt.xlim([-0.05, 1.05])
plt.ylim([-0.05, 1.05])
plt.xlabel('false positive rate')
plt.ylabel('true positive rate')
plt.title('Receiver Operator Characteristic')
plt.legend(loc="lower right")
# plt.show()
plt.savefig('./charts/roc_auc.png', dpi=250)

###### Comparing ROC AUC and Accuracy ##########
pipe_lr = pipe_lr.fit(X_train2, y_train)
y_labels = pipe_lr.predict(X_test[:, [4, 14]])
y_probas = pipe_lr.predict_proba(X_test[:, [4, 14]])[:, 1]


print('ROC AUC: %.3f' % roc_auc_score(
	y_true=y_test, y_score=y_probas))

print('Accuracy: %.3f' % accuracy_score(
	y_true=y_test, y_pred=y_labels))
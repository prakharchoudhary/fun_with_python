from sklearn import svm
# using the support vector classifier(SVC)

X = [[0,1], [1,1]]
y = [0,1]

clf = svm.SVC()
clf.fit(X,y)

pred = clf.predict([[2., 2.]])
print pred
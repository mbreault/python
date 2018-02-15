from sklearn import svm
from sklearn import datasets
import pickle

clf = svm.SVC()
iris = datasets.load_iris()
X, y = iris.data, iris.target
print(clf.fit(X, y))

s = pickle.dumps(clf)
clf2 = pickle.loads(s)
clf2.predict(X[0:1])

print(y[0])
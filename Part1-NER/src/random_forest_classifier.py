from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

clf = RandomForestClassifier(n_estimators=100, max_depth=2,random_state=0)
clf.fit(x_train, y_train)
y_pred = clf.predict(x_val)

print('Validation Accuracy : {}'.format(accuracy_score(y_val, y_pred)))
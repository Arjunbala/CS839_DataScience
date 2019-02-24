from sklearn import tree

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X_train, Y_train)
Y_pred = clf.predict(X_val)

print('Validation Accuracy : {}'.format(accuracy_score(y_val, y_pred)))
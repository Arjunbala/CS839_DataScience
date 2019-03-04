import nltk
import numpy as np
import pandas as pd
from preprocess import get_file_numbers, label_dataset
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import KFold
from sklearn import tree
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_recall_fscore_support


def train_decision_tree(X_train, y_train, X_test, y_test):
	"""
	Trains a decision tree model on the training data and returns the accuracy on the testing data
	:param X_train: ndarray, feature vectors for candidates for training
	:param y_train: list, class labels for training
	:param X_test: ndarray, feature vectors for candidates for testing
	:param y_test: list, class labels for testing
	:return: (float, float, float, int), precision, recall, fbeta_score, support
	"""
	dt_clf = tree.DecisionTreeClassifier()
	dt_clf.fit(X_train, y_train)
	predictions = dt_clf.predict(X_test)
	return precision_recall_fscore_support(y_test, predictions, average='binary')		# dt_clf.score(X_test, y_test),


def train_random_forest(X_train, y_train, X_test, y_test):
	"""
	Trains a random forest model on the training data and returns the accuracy on the testing data
	:param X_train: ndarray, feature vectors for candidates for training
	:param y_train: list, class labels for training
	:param X_test: ndarray, feature vectors for candidates for testing
	:param y_test: list, class labels for testing
	:return: (float, float, float, int), precision, recall, fbeta_score, support
	"""
	randomforest_clf = RandomForestClassifier(n_estimators=100, max_depth=2, random_state=0)
	randomforest_clf.fit(X_train, y_train)
	predictions = randomforest_clf.predict(X_test)
	return precision_recall_fscore_support(y_test, predictions, average='binary')  # randomforest_clf.score(X_test, y_test)


def train_logistic_regression(X_train, y_train, X_test, y_test):
	"""
	Trains a logistic regression model on the training data and returns the accuracy on the testing data
	:param X_train: ndarray, feature vectors for candidates for training
	:param y_train: list, class labels for training
	:param X_test: ndarray, feature vectors for candidates for testing
	:param y_test: list, class labels for testing
	:return: (float, float, float, int), precision, recall, fbeta_score, support
	"""
	logistic_clf = LogisticRegression(solver='liblinear')
	logistic_clf.fit(X_train, y_train)
	predictions = logistic_clf.predict(X_test)
	return precision_recall_fscore_support(y_test, predictions, average='binary')  # logistic_clf.score(X_test, y_test)


def train_svm(X_train, y_train, actual_candidates, X_test, y_test):
	"""
	Trains n SVM model on the training data and returns the accuracy on the testing data
	:param X_train: ndarray, feature vectors for candidates for training
	:param y_train: list, class labels for training
	:param X_test: ndarray, feature vectors for candidates for testing
	:param y_test: list, class labels for training
	:return: (float, float, float, int), precision, recall, fbeta_score, support
	"""
	class_wts = 'balanced'	# {0: 1, 1: 10000}
	svm_clf = SVC(gamma='scale')
	svm_clf.fit(X_train, y_train)
	predictions = svm_clf.predict(X_test)
	find_false_positives(actual_candidates, y_test, predictions)
	return precision_recall_fscore_support(y_test, predictions, average='binary')  # svm_clf.score(X_test, y_test)


def find_false_positives(actual_candidates, y_test, predictions):
	for i in range(0, len(predictions)):
		if predictions[i] != y_test[i]:
			print(actual_candidates[i] + " pred->" + str(predictions[i]) +" actual->" + str(y_test[i]))


def main():
	dev_set, test_set = get_file_numbers()
	kf = KFold(n_splits=4)
	kf.get_n_splits(dev_set)
	for train_indices, validation_indices in kf.split(dev_set):
                print("## Model ####")
                train_points = []
                validation_points = []
                for idx in train_indices:
                    train_points.append(dev_set[idx])
                for idx in validation_indices:
                    validation_points.append(dev_set[idx])

                train_set = label_dataset(train_points, True)
                np.savetxt("train.csv", np.column_stack((train_set[0], train_set[1])), delimiter=",")
                validation_set = label_dataset(validation_points, False)

                print('Decision Tree:', train_decision_tree(train_set[0], train_set[1], validation_set[0], validation_set[1]))
                print('Random Forest:', train_random_forest(train_set[0], train_set[1], validation_set[0], validation_set[1]))
                print('Logistic Regression:', train_logistic_regression(train_set[0], train_set[1], validation_set[0], validation_set[1]))
                print('SVM:', train_svm(train_set[0], train_set[1], validation_set[2], validation_set[0], validation_set[1]))
                print()

if __name__ == "__main__":
	main()

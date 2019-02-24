import nltk
import numpy as np
import pandas as pd
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression


def train_logistic_regression(X_train, y_train, X_test, y_test):
	"""
	Trains a logistic regression model on the training data and returns the accuracy on the testing data
	:param X_train: ndarray, feature vectors for candidates for training
	:param y_train: list, class labels for training
	:param X_test: ndarray, feature vectors for candidates for testing
	:param y_test: list, class labels for testing
	:return: float, accuracy of the logistic regression model
	"""
	logistic_clf = LogisticRegression()
	logistic_clf.fit(X_train, y_train)
	return logistic_clf.score(X_test, y_test)


def train_svm(X_train, y_train, X_test, y_test):
	"""
	Trains n SVM model on the training data and returns the accuracy on the testing data
	:param X_train: ndarray, feature vectors for candidates for training
	:param y_train: list, class labels for training
	:param X_test: ndarray, feature vectors for candidates for testing
	:param y_test: list, class labels for training
	:return: float, accuracy of the SVM model
	"""
	svm_clf = SVC()
	svm_clf.fit(X_train, y_train)
	return svm_clf.score(X_test, y_test)


def main():
	pass


if __name__ == "__main__":
	main()

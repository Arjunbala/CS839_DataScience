import nltk
import numpy as np
import pandas as pd
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression


def train_logistic_regression(X_train, y_train, X_test, y_test):
	logistic_clf = LogisticRegression()
	logistic_clf.fit(X_train, y_train)
	return logistic_clf.score(X_test, y_test)


def train_svm(X_train, y_train, X_test, y_test):
	svm_clf = SVC()
	svm_clf.fit(X_train, y_train)
	return svm_clf.score(X_test, y_test)


def main():
	pass


if __name__ == "__main__":
	main()

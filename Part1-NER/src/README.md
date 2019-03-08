# DataScience, Spring 2019
## Project Stage 1 - Named Entity Recognition

### Prerequisites
#### Tools and Libraries
- Python 3.6
- Pandas, Numpy
- NLTK
#### Training data
Annotated and raw documents are to be present in the required directories and format

### Usage
1. Run `setup.sh` as shown below to download pretrained GloVe [[1]](#references) word vectors:
	```
	$ bash setup.sh
	```
2. Run `model.py` with *Python 3.6* as follows. This file performs 4 fold cross validation on the training data (~200 documents) to choose the best model among `SVM`, `Logistic Regression`, `Decision Tree` and `Random Forest`. Then it evaluates the best model on the testing data (~100 documents) and reports its Precision, Recall and F1 score.
	```
	$ python model.py
	```

### References
[1] Jeffrey Pennington and Richard Socher and Christopher D. Manning. 2014. GloVe: Global Vectors for Word Representation. _Empirical Methods in Natural Language Processing (EMNLP)_
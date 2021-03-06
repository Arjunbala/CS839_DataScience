---
layout: default
title: Project Stage 1
nav_order: 2
---

## Project Stage I - Named Entity Recognition
{: .fs-5 .fw-300 }

### Dataset
A dataset of news articles from [BBC](http://mlg.ucd.ie/datasets/bbc.html) was used for the project. About 386 documents from Entertainment section were extracted from the above link. 330 of these were annotated and used for this project.

The raw dataset and the annotated dataset can be found below along with the dev and test splits:
- [Raw](Part1-NER/raw-dataset/)
	- [Set I - Dev Set](Part1-NER/train_set)
	- [Set J - Test Set](Part1-NER/test_set)
- [Annotated](Part1-NER/dataset)
	- [Set I - Dev Set](Part1-NER/train_set_annotated)
	- [Set J - Test Set](Part1-NER/test_set_annotated)

### Source Code
- [Link](Part1-NER/src)

### Results
On the test set, our model achieved the following results:

| Precision | Recall | F1 Score |
| :---: | :---: | :---: |
| 0.9140 | 0.8878 | 0.9007 |


### Other documents
- [Zip file](Part1-NER/ProjectStage1_LumenScience.zip){: .btn }
- [Report](Part1-NER/report.html)

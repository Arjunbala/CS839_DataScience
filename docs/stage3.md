---
layout: default
title: Project Stage 3
nav_order: 3
---

## Project Stage III - Entity Matching using CloudMatcher
{: .fs-5 .fw-300 }

### Matching Fodors and Zagats
- CloudMatcher User ID: **arungta**
- Project ID: **group-3_stage-3**
- Statistics of Matches:

![LastPage](Part3-EntityMatching/last-page.png?raw=true "LastPage")

<p></p>

## Movies from IMDB and Metacritic

### Blocking Step

- CloudMatcher User ID: **arungta**
- Project ID : **group_3_movies_matching**

- Screenshot:

![movies_blocking](Part3-EntityMatching/movies_blocking.png?raw=true "movies_blocking")

<p></p>


### Matching Step
- CloudMatcher User ID: **arungta**
- Project ID : **group_3_movies_matching**

- Statistics of Matches:

![movies_matching](Part3-EntityMatching/movies_matching.png?raw=true "movies_matching")

<p></p>

## Estimating Accuracy
- [Prediction List](Part3-EntityMatching/Prediction_List)
- [Candidate Set](Part3-EntityMatching/Original_Candidate_Set)
- [Table A](Part3-EntityMatching/IMDB)
- [Table B](Part3-EntityMatching/Metacritic)

- Size of Candidate Set: `2997152`
	- Candidate set is more than `500`
	- [Computing Density of matches](Part3-EntityMatching/report.html)
	- [Blocking Code](Part3-EntityMatching/blocker.ipynb)
	- [Final Reduced set of Candidate Tuple Pairs](Part3-EntityMatching/Blocked_Candidate_Set)
	- [Manually Labeled Tuple Pairs](Part3-EntityMatching/Labeled_final)
	- Precision: [`0.9597402500318443 - 0.9986098101849362`]
	- Recall: [`1.0 - 1.0`]

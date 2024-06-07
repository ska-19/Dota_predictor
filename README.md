# Dota predictor

### [PRESENTATION](https://docs.google.com/presentation/d/1l1IhJ6n9MRVGZeF4tQREiUocQqSLOdAfPMwEqgelCew/edit?usp=sharing)
### [DEMONSTRATION](https://drive.google.com/file/d/1VZQUm9WiOwRqVUqsCUgMtbvp__1bkMhU/view?usp=sharing)
****
## Description

Educational project, Python bot predicting the probability of a team's victory based on the picks.

## Setup

Install python dependencies:

```pip install -r requirements.txt```

Run locally:

```
cd telegram_bot/
python3 main.py
```

### Dataset

We trained all our models on [this dataset](https://www.kaggle.com/datasets/devinanzelmo/dota-2-matches).
And 

### Models

- ~~Logistic Regression~~
- ~~XGBoost~~
- **CatBoostClassifier**

### Metrics

- accuracy_score 

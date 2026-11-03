# Phase 4.1 — ML Workflow

## Introduction

**Topic:** Understand Problem Framing, Baselines and Train/Validation/Test Splits.

**Learning Outcome:** Write a correct ML experiment plan.

### 1. What is an ML Workflow?

An ML workflow is a sequence of steps followed to solve a real-world problem using Machine Learning.

A typical ML workflow includes:

1. Problem Framing
2. Data Collection
3. Data Preparation
4. Train/Validation/Test Splitting
5. Baseline Model Development
6. Model Training
7. Model Evaluation
8. Final Testing

**Important:** A good ML project starts with a clearly defined problem, not with selecting an algorithm.

### 2. Problem Framing

Problem framing means converting a real-world business problem into a Machine Learning problem.

Examples:

| Business Problem | ML Problem | ML Type |
|---|---|---|
| Predict customer churn | Predict whether a customer will leave | Classification |
| Estimate house prices | Predict house selling prices | Regression |
| Group similar customers | Discover customer segments | Clustering |
| Detect fraudulent transactions | Identify suspicious transactions | Classification |
| Predict monthly sales | Estimate future sales | Regression |

Three major ML problem types:

- **Classification:** Predict categories or classes.
- **Regression:** Predict numerical values.
- **Clustering:** Group similar data points without predefined labels.

### 3. Baseline Model

A baseline model is a simple starting model used as a performance benchmark.

It helps us determine whether advanced Machine Learning models actually improve performance.

Common baselines:

| ML Problem | Baseline Approach |
|---|---|
| Classification | Predict the most frequent class |
| Regression | Predict the training-set mean or median |
| Clustering | Simple clustering or domain-based grouping |

Example:

A dataset contains 1,000 customer records:

- 900 customers did not purchase.
- 100 customers purchased.

A most-frequent-class baseline predicts that every customer will not purchase.

Accuracy:

Accuracy = (900 / 1000) × 100 = 90%

Although accuracy is 90%, the model fails to identify any purchasing customers.

**Lesson:** Accuracy alone can be misleading, especially with imbalanced datasets.

### 4. Train, Validation and Test Split

We divide a dataset into three separate parts.

Example: 10,000 records using a 70/15/15 split.

| Dataset | Percentage | Records | Purpose |
|---|---:|---:|---|
| Training | 70% | 7,000 | Teach the model |
| Validation | 15% | 1,500 | Tune hyperparameters and select models |
| Testing | 15% | 1,500 | Final evaluation on unseen data |

#### A. Training Set

- Used to train the model.
- The model learns patterns and relationships from the training data.

#### B. Validation Set

- Used to compare different models.
- Helps tune hyperparameters.
- Helps select the best-performing model.

#### C. Test Set

- Used for final model evaluation.
- Represents unseen data.
- Should not be repeatedly used for model tuning.

**Golden Rule:** Never use the test dataset to repeatedly tune or select models.

Other common splits include 80/20 and 80/10/10. The appropriate split depends on the dataset and experiment.

### 5. Python Implementation

Libraries:

- pandas
- scikit-learn

Installation:

```bash
pip install pandas scikit-learn
```

Example:

```python
import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("customers.csv")

X = df.drop("purchased", axis=1)
y = df["purchased"]

# Training and temporary datasets
X_train, X_temp, y_train, y_temp = train_test_split(
    X, y,
    test_size=0.30,
    random_state=42,
    stratify=y
)

# Validation and test datasets
X_val, X_test, y_val, y_test = train_test_split(
    X_temp, y_temp,
    test_size=0.50,
    random_state=42,
    stratify=y_temp
)

print("Training:", len(X_train))
print("Validation:", len(X_val))
print("Testing:", len(X_test))
```

Important parameters:

- `test_size`: Determines the proportion of data allocated to the split.
- `random_state=42`: Makes the split reproducible.
- `stratify=y`: Preserves approximately the same target-class distribution in each split.

**Note:** For time-series problems, chronological splitting is generally preferred over random splitting.

### 6. Data Leakage

Data leakage happens when information that would not legitimately be available at prediction time influences model training or evaluation.

Examples:

1. Using future information to predict past events.
2. Scaling the entire dataset before splitting.
3. Including target-related information in input features.
4. Repeatedly tuning a model using test-set results.

How to prevent leakage:

- Split data before preprocessing.
- Fit scalers and encoders using training data only.
- Apply learned transformations to validation and test data.
- Avoid future information in model features.
- Keep the test dataset separate until final evaluation.

Scikit-learn Pipelines help prevent preprocessing leakage.

### 7. ML Experiment Plan

Before developing a Machine Learning model, document the following:

| Component | Description |
|---|---|
| Business Problem | What real-world problem are we solving? |
| ML Problem | Classification, regression or clustering? |
| Target Variable | What are we predicting? |
| Features | Which input columns will we use? |
| Baseline | What simple model will we compare against? |
| Data Split | Training, validation and testing percentages |
| Evaluation Metrics | Accuracy, Precision, Recall, F1, MAE, RMSE, etc. |
| Model Selection | How will we select the best model? |
| Final Evaluation | How will we test generalization? |
| Leakage Prevention | How will we avoid data leakage? |

---

## Practice Tasks

### Task 1 — Problem Framing

An online shopping company wants to predict whether customers will purchase again within 30 days.

Define:
- Business problem
- ML problem type
- Target variable
- Five possible features

### Task 2 — Baseline Understanding

A dataset contains:
- 800 negative cases
- 200 positive cases

Calculate the accuracy of a most-frequent-class baseline.

Explain why accuracy may be misleading.

### Task 3 — Dataset Splitting

You have 10,000 records.

Calculate the number of records in:
- Training (70%)
- Validation (15%)
- Testing (15%)

Explain the purpose of each dataset.

### Task 4 — Data Leakage

A model predicts next month's sales, but its features include next month's actual discount and sales figures.

Identify the leakage and explain how to fix it.

### Task 5 — Complete ML Experiment Plan

Create a complete ML experiment plan for predicting customer churn.

Include:
- Business problem
- Target variable
- Features
- Baseline
- Data splitting strategy
- Evaluation metrics
- Model selection
- Leakage prevention

---

## Learning Outcome

After completing this module, I should be able to:

- Convert business problems into ML problems.
- Identify classification, regression and clustering tasks.
- Understand and create baseline models.
- Correctly divide data into training, validation and test sets.
- Understand and prevent data leakage.
- Write a complete ML experiment plan before training a model.

## Recommended Resources

1. Scikit-learn Getting Started: https://scikit-learn.org/stable/getting_started.html
2. Model Evaluation: https://scikit-learn.org/stable/modules/model_evaluation.html
3. Cross Validation: https://scikit-learn.org/stable/modules/cross_validation.html
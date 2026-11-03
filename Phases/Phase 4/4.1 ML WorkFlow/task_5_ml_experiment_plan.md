# Task 5 — Complete ML Experiment Plan

**Project:** Customer Churn Prediction

## 1. Business Problem

A company wants to identify customers who are likely to stop using its services.

The goal is to predict customer churn early so the company can take action to improve customer retention.

## 2. Target Variable

`churn`

- 1 = Customer leaves the company.
- 0 = Customer stays with the company.

## 3. Possible Features

| Feature | Description |
|---|---|
| customer_age | Customer's age |
| monthly_charges | Monthly payment |
| tenure | How long customer has used the service |
| total_spending | Total customer spending |
| support_calls | Number of customer support calls |

## 4. Baseline Model

Start with a Most Frequent Class Classifier.

It predicts the majority class for every customer.

This gives us a basic performance score to compare with more advanced models.

## 5. Dataset Splitting

Use a 70/15/15 split:

- 70% Training
- 15% Validation
- 15% Testing

Use stratified splitting to maintain the churn distribution.

If customer records are time-dependent, use a chronological split to avoid future information leaking into training.

## 6. Evaluation Metrics

| Metric | Purpose |
|---|---|
| Accuracy | Overall correct predictions |
| Precision | How many predicted churners actually churned |
| Recall | How many actual churners were identified |
| F1-score | Balance between precision and recall |

Recall is particularly important because we want to identify as many customers at risk of leaving as possible.

## 7. Model Selection

Start with these models:

1. Logistic Regression
2. Decision Tree
3. Random Forest

Compare their validation performance and select the model that best meets the business objective.

## 8. Data Leakage Prevention

- Remove future information from features.
- Use only data available at prediction time.
- Fit preprocessing steps using training data only.
- Apply the same transformations to validation and test data.
- Keep the test set separate until final evaluation.

## 9. Final Evaluation

Evaluate the selected model using the test dataset.

Check Precision, Recall, F1-score and Confusion Matrix.

If the model performs well, the company can use its predictions to identify customers who may leave and develop customer retention strategies.

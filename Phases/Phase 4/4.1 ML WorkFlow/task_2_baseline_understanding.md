# Task 2 — Baseline Understanding

## Given Data

- Negative cases = 800
- Positive cases = 200
- Total records = 1000

## Baseline Model

A most-frequent-class model always predicts the majority class.

Here, the majority class is Negative (800 cases).

## Accuracy Calculation

Formula:

Accuracy = (Correct Predictions / Total Predictions) × 100

Accuracy = (800 / 1000) × 100

**Accuracy = 80%**

## Why Can Accuracy Be Misleading?

Accuracy is misleading when the dataset is imbalanced.

Our model predicts every customer as Negative.

- Negative predictions: 800 correct.
- Positive predictions: 200 incorrect.

Although accuracy is 80%, the model cannot identify even one positive case.

## Conclusion

We should also use Precision, Recall and F1-score to evaluate the model.

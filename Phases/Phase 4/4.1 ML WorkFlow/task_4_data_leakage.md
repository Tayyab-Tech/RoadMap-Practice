# Task 4 — Data Leakage

## Problem

The model predicts next month's sales, but its features include:

- Next month's actual discount.
- Next month's actual sales.

## What is Data Leakage?

Data leakage happens when a model receives information during training that would not be available when making real-world predictions.

## Why Is This a Problem?

The model already has access to future information, so it may show excellent performance during testing but fail in real-world situations.

## How to Fix It

1. Remove next month's actual sales from the features.
2. Remove next month's actual discount if it is not known at prediction time.
3. Use only historical information available before the prediction date.
4. Split data according to time instead of randomly splitting it.

## Example

| Feature | Use? |
|---|---|
| Previous month's sales | Yes |
| Previous month's discount | Yes |
| Current customer demand | Yes |
| Next month's actual sales | No |
| Next month's unknown discount | No |

## Conclusion

Always use information that would realistically be available at prediction time.

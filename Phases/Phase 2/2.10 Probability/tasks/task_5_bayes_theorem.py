# A spam filter receives 1,000 emails.

# 20% of emails are actually spam.
# The filter detects spam correctly 95% of the time.
# For legitimate emails, the filter incorrectly marks 5% as spam.

# Calculate:

# (P(Spam))
# (P(Spam^c))
# (P(FilterSpam | Spam))
# (P(FilterSpam | NotSpam))
# (P(FilterSpam)
# Most importantly:
# P(Spam | FilterSpam)
# Explain in one or two sentences why the answer to #6 is not simply 95%


import pandas as pd


# Total emails
total_emails = 1000

# Probabilities
p_spam = 0.20
p_not_spam = 1 - p_spam

p_filter_spam_given_spam = 0.95
p_filter_spam_given_not_spam = 0.05


# 1. P(Spam)
P_Spam = p_spam

# 2. P(Spam^c)
P_NotSpam = p_not_spam

# 3. P(FilterSpam | Spam)
P_FilterSpam_given_Spam = p_filter_spam_given_spam

# 4. P(FilterSpam | NotSpam)
P_FilterSpam_given_NotSpam = p_filter_spam_given_not_spam


# 5. P(FilterSpam)
# P(FilterSpam) =
# P(FilterSpam | Spam) * P(Spam)
# + P(FilterSpam | NotSpam) * P(NotSpam)

P_FilterSpam = (
    P_FilterSpam_given_Spam * P_Spam
    + P_FilterSpam_given_NotSpam * P_NotSpam
)


# 6. P(Spam | FilterSpam)
# Bayes' Theorem

P_Spam_given_FilterSpam = (
    P_FilterSpam_given_Spam * P_Spam
) / P_FilterSpam


# Number of emails in each category
spam_emails = int(total_emails * P_Spam)
not_spam_emails = int(total_emails * P_NotSpam)

correctly_detected_spam = spam_emails * P_FilterSpam_given_Spam
false_positives = not_spam_emails * P_FilterSpam_given_NotSpam


# Create a Pandas DataFrame
results = pd.DataFrame({
    "Calculation": [
        "P(Spam)",
        "P(NotSpam)",
        "P(FilterSpam | Spam)",
        "P(FilterSpam | NotSpam)",
        "P(FilterSpam)",
        "P(Spam | FilterSpam)"
    ],
    "Probability": [
        P_Spam,
        P_NotSpam,
        P_FilterSpam_given_Spam,
        P_FilterSpam_given_NotSpam,
        P_FilterSpam,
        P_Spam_given_FilterSpam
    ]
})


# Print results
print("=== Bayes' Theorem ===")
print(results.to_string(index=False))

print("\n=== Email Counts ===")
print(f"Total emails: {total_emails}")
print(f"Spam emails: {spam_emails}")
print(f"Not spam emails: {not_spam_emails}")
print(f"Correctly detected spam: {correctly_detected_spam}")
print(f"False positives: {false_positives}")

print("\n=== Final Answer ===")
print(f"P(Spam | FilterSpam) = {P_Spam_given_FilterSpam:.4f}")
print(f"Percentage = {P_Spam_given_FilterSpam * 100:.2f}%")

print("\n=== Explanation ===")
print(
    "It is not simply 95% because 95% is P(FilterSpam | Spam), "
    "while we need P(Spam | FilterSpam). "
    "The calculation must also consider the 5% false-positive rate "
    "among the much larger group of legitimate emails."
)
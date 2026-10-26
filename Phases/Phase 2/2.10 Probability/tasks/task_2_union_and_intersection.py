# A class has 40 students:

# 25 students study Python
# 18 students study SQL
# 10 students study both Python and SQL

# Calculate:

# (P(Python))
# (P(SQL))
# (P(Python ∩ SQL))
# Probability that a randomly selected student studies Python or SQL.
# Probability that the student studies neither Python nor SQL.


total = 40
python_students = 25
sql_students = 18
both = 10

# 1. P(Python)
p_python = python_students / total

# 2. P(SQL)
p_sql = sql_students / total

# 3. P(Python ∩ SQL)
p_both = both / total

# 4. P(Python ∪ SQL)
p_union = p_python + p_sql - p_both

# 5. Neither
p_neither = 1 - p_union

print("P(Python):", p_python)
print("P(SQL):", p_sql)
print("P(Python ∩ SQL):", p_both)
print("P(Python ∪ SQL):", p_union)
print("P(Neither):", p_neither)


# in pandas 

import pandas as pd

df = pd.DataFrame({
    "Group": ["Python", "SQL", "Both"],
    "Students": [25, 18, 10]
})

df["Probability"] = df["Students"] / total

print(df)
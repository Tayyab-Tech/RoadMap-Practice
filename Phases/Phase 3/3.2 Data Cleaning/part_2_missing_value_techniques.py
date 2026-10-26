import pandas as pd
import numpy as np


data = {
    "Employee": ["Ali", "Sara", "Ahmed", "Zain", "Ayesha"],
    "Department": ["IT", "IT", "HR", "HR", "IT"],
    "Salary": [50000, np.nan, 40000, np.nan, 60000]
}

employees = pd.DataFrame(data)

employees["Salary"] = employees["Salary"].fillna(
    employees.groupby("Department")["Salary"]
    .transform("median")
)

print(employees)
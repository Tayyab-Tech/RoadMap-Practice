# Mini NumPy Data Processor

# Create a random 10 × 5 dataset.

# Assume:

# Column 1 → Age
# Column 2 → Experience
# Column 3 → Salary
# Column 4 → Performance
# Column 5 → Hours Worked

# Perform all of the following:

# Extract each column using indexing.
# Find average of every column.
# Find employees with salary > 100000.
# Find employees with performance > 80.
# Increase salaries by 10% using broadcasting.
# Normalize the performance column between 0 and 1.
# Find employee with highest salary.
# Find employee with highest performance.
# Sort employees by salary.
# Calculate correlation between experience and salary.

# Restriction: Avoid unnecessary Python loops. Try to solve the entire problem using NumPy operations.

import importlib
np = importlib.import_module("numpy")


np.random.seed(42)

data = np.column_stack([
    np.random.randint(20, 61, 10),          # Age
    np.random.randint(1, 21, 10),           # Experience
    np.random.randint(60000, 150001, 10),   # Salary
    np.random.randint(50, 101, 10),         # Performance
    np.random.randint(30, 61, 10)           # Hours Worked
])

print(data)

age = data[:,0]
experience = data[:,1]
salary = data[:,2]
performance = data[:,3]
hours_worked = data[:,4]

print(f"\nAge data : {age}")
print(f"Experience data : {experience}")
print(f"Salary data : {salary}")
print(f"Perfomance data : {performance}")
print(f"Hours Worked data : {hours_worked}\n")


avg = np.round(data.mean(axis=0),2)
print("Average of every column:", [f"{x:.2f}" for x in avg])

above_lac_salary = salary[salary>100000]
print("Employees with salary greater than 1 lac : ",above_lac_salary)

above_80_performance = performance[performance>80]
print("Employees with performance greater than 80 : ", above_80_performance)

increase_salary = salary*1.10
print("Salary increasing by 10% : ",increase_salary)


# Normalize performance between 0 and 1 
# Normalize formula : 
# x-x.min()/x.max()-x.min()
performance_normalized = (
    (performance - performance.min()) / (performance.max() - performance.min())
)

print("\nNormalized performance:")
print(performance_normalized)



highest_salary_employee = np.argmax(data[:,2])
print("\nEmployee with highest salary:", highest_salary_employee + 1)
print("Highest salary : ",data[highest_salary_employee, 2])


highest_performance = np.argmax(data[:,3])
print("\nEmployee with highest perfomance : ",highest_performance)
print("Employee highest perfomance : ",data[highest_performance,3])


# Sort employees by salary
sorted_by_salary = data[np.argsort(data[:, 3])[::-1]]
print("\nEmployees sorted by salary:\n", sorted_by_salary)


# Correlation between experience and salary
correlation = np.corrcoef(experience, salary)[0, 1] # if we don't add [0,1] it returns correlation matix

print("\nCorrelation between experience and salary:", correlation)
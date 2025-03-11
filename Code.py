import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = "employee_data.csv"
df = pd.read_csv(file_path)

# Display basic information and first few rows
print("Dataset Overview:")
print(df.info())
print(df.head())

# Basic salary statistics
print("\nSalary Statistics:")
print("Mean Salary:", df['Salary'].mean())
print("Median Salary:", df['Salary'].median())
print("Minimum Salary:", df['Salary'].min())
print("Maximum Salary:", df['Salary'].max())

# Highest and lowest-paid employees
highest_paid = df.loc[df['Salary'].idxmax()]
lowest_paid = df.loc[df['Salary'].idxmin()]
print("\nHighest Paid Employee:")
print(highest_paid)
print("\nLowest Paid Employee:")
print(lowest_paid)

# Salary distribution plot
plt.figure(figsize=(8, 5))
plt.hist(df['Salary'], bins=20, color='skyblue', edgecolor='black')
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.title('Salary Distribution')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

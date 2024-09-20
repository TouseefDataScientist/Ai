# Importing pandas
import pandas as pd

# 1. Creating a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [24, 27, 22, 32, 29],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
    'Salary': [70000, 80000, 50000, 60000, 75000],
    'Department': ['HR', 'Finance', 'IT', 'Marketing', 'Finance']
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# 2. Basic DataFrame Information
print("\nDataFrame Info:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe())

# 3. Sorting the DataFrame by Age
sorted_df = df.sort_values(by='Age')
print("\nDataFrame sorted by Age:")
print(sorted_df)

# 4. Filtering Data (e.g., Salary > 60000)
filtered_df = df[df['Salary'] > 60000]
print("\nFiltered DataFrame (Salary > 60000):")
print(filtered_df)

# 5. Adding a new column (Bonus as 10% of Salary)
df['Bonus'] = df['Salary'] * 0.1
print("\nDataFrame with Bonus column added:")
print(df)

# 6. Grouping Data by Department and calculating the average salary
grouped_df = df.groupby('Department')['Salary'].mean().reset_index()
print("\nAverage Salary by Department:")
print(grouped_df)

# 7. Applying a function (e.g., converting Age to a category)
def age_category(age):
    if age < 25:
        return 'Young'
    elif 25 <= age < 30:
        return 'Mid-aged'
    else:
        return 'Senior'

df['Age Category'] = df['Age'].apply(age_category)
print("\nDataFrame with Age Category column added:")
print(df)

# 8. Merging two DataFrames
# Creating a second DataFrame
extra_data = {
    'Name': ['Alice', 'Charlie', 'Eva'],
    'Experience': [2, 5, 3]
}

df_extra = pd.DataFrame(extra_data)

# Merging the two DataFrames on 'Name'
merged_df = pd.merge(df, df_extra, on='Name', how='left')
print("\nMerged DataFrame:")
print(merged_df)

# 9. Pivot Table Example
pivot_table = df.pivot_table(values='Salary', index='Department', columns='City', aggfunc='mean', fill_value=0)
print("\nPivot Table:")
print(pivot_table)

# 10. Exporting DataFrame to CSV
df.to_csv('output.csv', index=False)
print("\nDataFrame exported to CSV (output.csv)")

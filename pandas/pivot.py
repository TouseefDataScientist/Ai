# Import pandas
import pandas as pd

# Sample data
data = {
    'Name': ['John', 'Emily', 'Nick', 'Laura', 'Paul', 'John', 'Emily'],
    'Department': ['Sales', 'HR', 'IT', 'Sales', 'HR', 'IT', 'Sales'],
    'Salary': [70000, 50000, 80000, 60000, 65000, 70000, 52000],
    'Bonus': [5000, 3000, 4000, 6000, 3500, 4500, 3000],
    'City': ['New York', 'Los Angeles', 'Chicago', 'New York', 'Los Angeles', 'Chicago', 'New York']
}

# Creating a DataFrame
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Creating a pivot table
# We will create a pivot table showing the average Salary and Bonus per Department and City
pivot_table = df.pivot_table(values=['Salary', 'Bonus'], index='Department', columns='City', aggfunc='mean', fill_value=0)

print("\nPivot Table with average Salary and Bonus per Department and City:")
print(pivot_table)



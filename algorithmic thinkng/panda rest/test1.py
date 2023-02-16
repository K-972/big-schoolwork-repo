import pandas as pd

# create a sample DataFrame
data = {'Name': ['John', 'Alice', 'Bob'],
        'Age': [25, 30, 35],
        'Salary': [50000, 60000, 70000]}
df = pd.DataFrame(data)

# write the DataFrame to an Excel file
with pd.ExcelWriter('output.xlsx') as writer:
    df.to_excel(writer, sheet_name='Sheet1', index=False)
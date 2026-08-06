'''Exercise 1
Read the CSV file and print the DataFrame.'''

import pandas as pd 

df = pd.read_csv("datasets/students.csv")
print(df)

'''Exercise 1
Read the CSV file and print the DataFrame.'''

print(df.head())
print(df.tail())
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.info())
print(df.describe())

'''Exercise 4
Read only the first 3 rows.'''


df = pd.read_csv("datasets/students.csv",nrows=3)
print(df)

'''Exercise 5
Read only the columns:
Name
Marks'''

df = pd.read_csv("datasets/students.csv",usecols=["Name","Marks"])
print(df)

'''Exercise 6
Save the DataFrame to:
students_copy.csv
without the index.'''

df.to_csv("datasets/students_copy.csv",index=False)
df.to_excel("datasets/students_copy.xlsx",index=False)
df.to_json("datasets/students_copy.json",orient="records",indent=4)

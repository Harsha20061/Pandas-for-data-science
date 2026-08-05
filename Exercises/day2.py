'''Exercise 1
Create this DataFrame:
Name	Age	Marks
Harsha	20	92
Rahul	21	85
Anjali	19	96
Priya	22	88'''

import pandas as pd 
data = {
    "Name":["Harsha","Rahul","Anjali","Priya"],
    "Age":[20,21,19,22],
    "Marks":[92,85,96,88]
}

df = pd.DataFrame(data)
print(df)

'''Exercise 2
Print:
Shape
Size
Columns
Index
Data types'''

print("shape :",df.shape)
print("size :",df.size)
print("columns :",df.columns)
print("Index :",df.index)
print("Data types :",df.dtypes)


print(df.info())
print(df.describe())

'''Exercise 4

Print:

First 2 rows
Last 2 rows'''

print(df.head(2))
print(df.tail(2))

'''Exercise 5

Print only the "Name" column.'''

print(df["Name"])

'''Exercise 6
Print only:
Name
Marks'''

print(df[["Name","Marks"]])


'''Exercise 7
Add a new column:
Grade
A
B
A
B'''

df["Grade"] = ["A","B","A","B"]


'''Exercise 8
Create a new column:
Bonus Marks = Marks + 5'''

df["Bonus Marks"] = df["Marks"]+5
print(df)


'''Exercise 9
Rename the "Marks" column to "Score".'''

df.rename(columns={"Marks":"Score"},inplace=True)
df.drop(columns=["Grade"],inplace=True)
print(df)

'''Exercise 11

Print:

Mean Score
Maximum Score
Minimum Score
Sum of Scores'''

print(df["Score"].mean())
print(df["Score"].max())
print(df["Score"].min())
print(df["Score"].sum())

# print(df.iloc[0])
# print(df.iloc[1:3])

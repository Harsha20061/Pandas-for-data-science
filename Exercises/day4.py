import pandas as pd

data = {
    "Name": ["Harsha", "Rahul", "Anjali", "Priya", "Arjun"],
    "Age": [20, 21, 19, 22, 20],
    "Marks": [92, 85, 96, 88, 91],
    "City": ["Hyderabad", "Bangalore", "Chennai", "Hyderabad", "Pune"]
}

df = pd.DataFrame(data)

'''Exercise 1
Print only the "Marks" column.'''

print(df["Marks"])

'''Exercise 2
Print only:
Name
City'''
print(df[["Name","City"]])

'''Exercise 3
Print the first 3 rows.'''
print(df.head(3))

'''Exercise 3
Print the last 2 rows.'''
print(df.tail(2))

'''Exercise 5
Using .loc, print the second row (index 1)'''

print(df.loc[1])

'''Exercise 6
Using .iloc, print the third row.'''

print(df.iloc[2])

'''xercise 7
Using .loc, print:
Rows: 1 to 3
Columns: Name, Marks'''

print(df.loc[1:3,["Name","Marks"]])

'''Exercise 8
Using .iloc, print:
Rows: 0 to 2
Columns: Name, Age
(Hint: use column positions.)'''

print(df.iloc[0:3,0:2])

'''Exercise 9

Print the value:

Anjali's Marks
Using:
.loc
.iloc'''

print("Anjalis Marks",df.loc[[2],["Marks"]])
print("Anjalis Marks",df.iloc[[2],[2]])

'''Exercise 10

Set "Name" as the index.

Then print:

df.loc["Rahul"]

Finally, reset the index.'''

df.set_index("Name",inplace=True)
print(df.loc["Rahul"])
df.reset_index(inplace=True)
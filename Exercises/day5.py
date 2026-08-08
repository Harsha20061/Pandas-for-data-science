import pandas as pd

data = {
    "Name": ["Harsha", "Rahul", "Anjali", "Priya", "Arjun"],
    "Age": [20, 21, 19, 22, 20],
    "Marks": [92, 85, 96, 88, 91],
    "City": ["Hyderabad", "Bangalore", "Chennai", "Hyderabad", "Pune"]
}

df = pd.DataFrame(data)


'''Exercise 1
Print students whose marks are greater than 90.'''

print(df[df["Marks"]>90])

'''Exercise 2
Print students whose marks are less than 90.'''

print(df[df["Marks"]<90])


'''Exercise 3
Print students whose marks are greater than or equal to 90.'''

print(df[df["Marks"]>=90])


'''Exercise 4
Print students from Hyderabad'''

print(df[df["City"]=="Hyderabad"])


'''Exercise 5
Print students who are not from Hyderabad.'''

print(df[df["City"]!="Hyderabad"])


'''Exercise 6
Print students whose:
Marks > 90
AND Age < 21'''

print(df[(df["Marks"]>90)&(df["Age"]<21)])

'''Exercise 7
Print students who are:
From Hyderabad
OR Pune'''

print(df[(df["City"]=="Hyderabad") | (df["City"]=="Pune")])

'''Exercise 8
Use isin() to find students from:
Hyderabad
Chennai'''

print(df[df["City"].isin(["Hyderabad","Pune"])])

'''Exercise 9
Use between() to find students whose marks are between:
85 and 92'''

print(df[df["Marks"].between(85,92)])

'''Exercise 10
Using .loc[], print only:
Name
Marks
for students who scored greater than 90.'''

print(df.loc[df["Marks"]>90,["Name","Marks"]])


'''Exercise 11
Use query() to find students whose:
Marks > 90'''

print(df.query("Marks > 90"))


'''Exercise 12

Use query() to find students whose:

Marks > 90 AND Age < 21'''

print(df.query("Marks>90 and Age < 21 "))
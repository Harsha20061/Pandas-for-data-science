#concept of filtering data

import pandas as pd

data = {
    "Name": ["Harsha", "Rahul", "Anjali", "Priya", "Arjun"],
    "Age": [20, 21, 19, 22, 20],
    "Marks": [92, 85, 96, 88, 91],
    "City": ["Hyderabad", "Bangalore", "Chennai", "Hyderabad", "Pune"]
}

df = pd.DataFrame(data)

print(df)


print(df["Marks"]>90)

#basic filtering 

print(df[df["Marks"]>90])

print(df[df["Marks"]<90])

print(df[df["Marks"]>=90])

print(df[df["Marks"]<=90])

print(df[df["City"]=="Hyderabad"])

print(df[df["City"] !="Hyderabad"])

print(df[(df["Marks"]>90)&(df["Age"]==20)])

print(df[(df["City"]=="Hyderabad") | (df["City"]=="Pune")])

print(df[~(df["City"] == "Hyderabad")])

print(df[df["City"].isin(["Hyderabad","Pune"])])

print(df[df["Marks"].between(85,92)])

print(df.loc[df["Marks"]>90,["Name","Marks"]])

print(df.query("Marks > 90"))

print(df[df["Name"].str.contains("a",case=False)])

print(df[(df["City"].isin(["Hyderabad","Pune"]))&(df["Marks"]>=90)])
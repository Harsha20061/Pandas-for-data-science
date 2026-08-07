#concepts of selecting rows and columns 

import pandas as pd

data = {
    "Name": ["Harsha", "Rahul", "Anjali", "Priya", "Arjun"],
    "Age": [20, 21, 19, 22, 20],
    "Marks": [92, 85, 96, 88, 91],
    "City": ["Hyderabad", "Bangalore", "Chennai", "Hyderabad", "Pune"]
}

df = pd.DataFrame(data)

print(df)

#Selecting columns 
print("=======Selecting columns =======")
print(df["Name"])
print(df[["Name","Marks"]])

print(df[:3])
print(df.head(3))

print(df[-2:])
print(df.tail(2))

print(df[1:4])


print(df.loc[2])
print(df.loc[[1,3]]) 
print(df.loc[1:3]) #includes 1,2,3 rows 

print(df.loc[[0,2,4],["Name","Marks"]])

#selecting with .iloc

print(df.iloc[4])

print(df.iloc[0:3])

print(df.iloc[:0:2])

print(df.iloc[[0,3],[0,2]])

df.set_index("Name",inplace=True)
print(df.loc["Harsha"])
df.reset_index(inplace=True)

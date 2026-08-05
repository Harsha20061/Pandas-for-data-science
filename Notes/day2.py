# concept of data frames 

import pandas as pd

data = {
    "Name":["Harsha","Abdul","Kalyan"],
    "Age":[20,21,19],
    "City":["Hyderabad","Mahabubnagar","Nizamabad"]
    }
df = pd.DataFrame(data)
print(df)

#concept of dataframe from list of lists 

data = [
    ["harsha",20],
    ["Abdul",30],
    ["Kalyan",40]
]
df = pd.DataFrame(data,columns=["Name","Age"])
print(df)

#concept of dataframe from list of dictionaries 

students =[
    {"Name":"harsha","age":20},
    {"name":"kalyan","age":30}
]
df = pd.DataFrame(students)
print(df) 


# concept of Atrributes of Data frame 

Data = {
    "Name":["harsha","abdul","kalyan"],
    "age":[19,20,21],
    "marks":[90,91,92]
}
df = pd.DataFrame(Data)
print("shape",df.shape)
print("size",df.size)
print("columns",df.columns)
print("index",df.index)
print("datatypes",df.dtypes)
print("info",df.info)
print("describe",df.describe())

#concept of viewing data 

print(df.head()) #for first five rows 

print(df.tail()) #for last five rows

print(df["Name"])
print(type(df["Name"])) #returns series 
print(df[["Name","marks"]])
print(type(df[["Name","marks"]]))

df["grade"] = ["A","B","A"]
print(df )

df["marks + bonus "]= df["marks"]+5
print(df)


df.rename(columns={"marks":"score"},inplace=True)
df.drop(columns=["grade"],inplace=True)
print(df)

#statistics from data frame 

print(df["score"].mean())
print(df["score"].max())
print(df["score"].min())
print(df["score"].sum())
print(df["score"].value_counts())
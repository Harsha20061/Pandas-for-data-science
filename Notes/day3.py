#concept of reading files 
import pandas as pd

df = pd.read_csv(r"datasets/students.csv")  # reading a csv file 
print(df)


#to read first n rows 

df = pd.read_csv("datasets/students.csv",nrows=2)
print(df)


#to read selected cols 

df = pd.read_csv("datasets/students.csv",usecols=["Name","Age"])
print(df)

#to skip initial rows

df = pd.read_csv("datasets/students.csv",skiprows=2)
print(df)

'''custom parameter 

df = pd.read_csv("datasets/stuents.csv",sep=";")'''

#reading excel file 

df = pd.read_excel("datasets/students.xlsx")
print("from excel file ",df)

df = pd.read_json("datasets/students.json")
print("from json ",df)

#writing to csv 

data = {
    "Name":["Harsha","Abdul"],
    "Marks":[90,95]
}
df = pd.DataFrame(data)
df.to_csv("datasets/output.csv",index=False)
df.to_excel("datasets/output.xlsx",index=False)
df.to_json("datasets/output.json", orient="records",
    indent=4)
import pandas as pd
import numpy as np
print(pd.__version__)

#creating first series 

marks = pd.Series([90,35,100,95])
print(marks)

#creating series using list

numbers = [10,20,30,40]
s = pd.Series(numbers)
print("series using list ",s)

#creating series using numpy array

arr = np.array([5,10,15,20])
s = pd.Series(arr)
print("series using numpy array",s)

#creating series with custom index

marks = pd.Series(
    [90,85,100,70],
    index=["english","maths","science","Social"]
    )
print(marks)

#Acessing the values from series 

print("using position",s[0])
print("using label",marks["maths"]) 

#creating series from dictionary

student ={
    "math":80,
    "physics":95,
    "chemistry":70
}

s = pd.Series(student)
print("series using student dictionary",s)

#Attributes of Series 

marks = pd.Series([90,85,100,95])

print("series of marks",marks)
print("shape of marks" ,marks.shape)
print("size of marks",marks.size)
print("datatype of marks",marks.dtype)
print("index of marks",marks.index)
print("values of marks",marks.values)

#basic statistics 

marks = pd.Series([90,85,100,95])

print("mean",marks.mean())
print("median",marks.median())
print("maximum",marks.max())
print("minimum",marks.min())
print("sum is",marks.sum())
print("count is",marks.count())

#vectoized operations 

print("adding 5 to each",marks+5)
print("multiplying 2 with each",marks*2)
print("squaring each value",marks**2)

#Boolean operations 

print("marks > 90",marks>90)
print("filtering marks",marks[marks>90])


s = pd.Series([10,20,np.nan,40])
print(s)

#checking missing values 

print(s.isna()) #check missing values
print(s.isna().sum()) #count missing values 

'''Exercise 1
Create a Series containing:
10
20
30
40
50'''

import pandas as pd
import numpy as np

s = pd.Series([10,20,30,40,50])
print("sample series ",s)

'''Exercise 2
Create a Series with custom labels:
A → 100
B → 200
C → 300'''

cus = pd.Series(
    [100,200,300],
    index=["A","B","C"]
)
print("series with custom indexes",cus)

'''Exercise 3
Create a Series from
{
"Apple":120,
"Banana":40,
"Orange":90
}'''

dic = {
    "Apple":120,
    "Banana":40,
    "orange":90
}

dicts = pd.Series(dic)
print("Series from dictionary",dicts)

'''Exercise 4

Print:

Mean
Max
Min
Sum'''


print("mean",s.mean())
print("max",s.max())
print("min",s.min())
print("sum",s.sum())

'''Exercise 5
Add 50 to every element.'''
print("adding 50 to every element",s+50)

'''Exercise 6
Print values greater than 100.'''

print("values grater than 100",cus[cus>100])

'''Exercise 7
Create a Series with one missing value and count the missing values.'''

srr = pd.Series([10,20,np.nan,40,50])
print(srr.isna().sum())

'''
Chapter 5: NumPy Basics
Date: 10/24/23
Reference: Python for Data Analysis (McKinney, 2022)
Topics:
    1. 
'''

# Introduction to pandas data structures


# Series 
'''
import pandas as pd

obj = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) # most basic 

print(obj)


'''

# DataFrames

#'''
import pandas as pd
import numpy as np

# default practice dataframe
data = pd.DataFrame(np.arange(36).reshape((6,6)), index = ["alpha", "bravo", "charlie", "delta", "echo", "foxtrot"], columns = ["1", "2", "3", "4", "5", "6"])

data["7"] = 32 # creating a column that does not exist before 

print(data)


#'''
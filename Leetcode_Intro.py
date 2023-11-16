'''
LEETCODE PANDAS INTRO
Date: 11/14/23
Notes:
    - This is a dedicated file for playing with introductory pandas problems
    - Goal is to finish the intro problems to practice lahat nung natutunan ko from chapter 5
'''

'''
Problem # 2877: Create a DataFrame from List 
Date: 11/14/23
Link: https://leetcode.com/problems/create-a-dataframe-from-list/description/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata
Difficulty: Easy
Notes:  
    - Create a dataframe with two columns from a given 2D list
'''

'''
import pandas as pd

student_data = [[1, 15, "2018-22379", "BS CHEM"], [2, 11, "2018-40307", "BS CHEM" ], [3, 11, "2018-82999", "BS CHEM"], [4, 20, "2018-93458", "BS CHEM"]]

col_names = ["student_id", "age", "student_number", "course"]

df = pd.DataFrame(student_data, columns=col_names)

print(df)

'''

'''
Problem # 2880: Select Data 
Date: 11/14/23
Link: https://leetcode.com/problems/select-data/description/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata
Difficulty: Easy
Notes:  
    - Select certain columns for a single row
'''
'''

import pandas as pd

data = {"student_id":["101", "53", "128", "3"], "name":["Ulysses", "William", "Henry", "Henry"], "age":[13, 10, 6, 11] }
df = pd.DataFrame(data)

print(df.loc[df["student_id"]== 101,["name", "age"]])

'''

'''
Problem # 2883: Drop Missing Data
Date: 11/16/23
Link: https://leetcode.com/problems/drop-missing-data/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata
Difficulty: Easy
Notes:  
    - Remove rows with missing data
'''

'''
import pandas as pd

data = {"student_id":[32, 217, 779, 849], "name":["Piper", None, "Georgia", "Willow"], "age":[5, 19, 20, 14]}

df = pd.DataFrame(data)

clean = df.dropna()

print(clean)
'''


'''
Problem # 2887: Fill Missing Data
Date: 11/16/23
Link: https://leetcode.com/problems/fill-missing-data/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata
Difficulty: Easy
Notes:  
    - Fill missing rows in the quantity column with 0
'''

#'''

import pandas as pd

data = {"name":["Wristwatch", "WirelessEarbuds", "GolfClubs", "Printe"], "quantity":[None, None, 779, 849], "price":[135, 821, 9319, 3051]}

products = pd.DataFrame(data)

print(products.fillna({"quantity":0}))


#'''
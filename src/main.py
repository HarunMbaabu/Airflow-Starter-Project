import pandas as pd 

data  = pd.read_csv("data/bestsellers with categories.csv") 

print(data.columns) 

"""
The following is the output of :  print(data.columns)  

Index(['Name', 'Author', 'User Rating', 'Reviews', 'Price', 'Year', 'Genre'], dtype='object')


"""



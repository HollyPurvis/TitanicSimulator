import numpy as np
import pandas as pd

a = [1,6,8]
# this is a panda series
series = pd.Series(a)
print(series)

# reads data from titanic.csv
titanic_csv = pd.read_csv("files/titanic.csv")

# turns data into a data frame
titanic_df = pd.DataFrame(titanic_csv)
print(titanic_df)
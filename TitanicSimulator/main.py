import numpy as np
import pandas as pd

# reads data from titanic.csv
# index_col removes index column
titanic_csv = pd.read_csv("files/titanic.csv", index_col=0)

# turns data into a data frame
titanic_df = pd.DataFrame(titanic_csv)
print(titanic_df)

# gets total number of passengers
total_passengers = titanic_df['Freq'].sum()
print(total_passengers)
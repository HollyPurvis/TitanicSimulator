import numpy as np
import pandas as pd

# reads data from titanic.csv
# index_col removes index column
titanic_csv = pd.read_csv("files/titanic.csv", index_col=0)

# turns data into a data frame
titanic_df = pd.DataFrame(titanic_csv)
#print(titanic_df)

# gets total number of passengers
total_passengers = titanic_df['Freq'].sum()
#print(total_passengers)

# filters for children and gets total number of children on board
children_passengers = titanic_df[titanic_df["Age"] == "Child"]
print(children_passengers)

children_class = children_passengers[children_passengers["Class"] == "1st"]['Freq'].mean()
print(children_class)

# filters for adults and gets total number of children on board
adult_passengers = titanic_df[titanic_df["Age"] == "Adult"]['Freq'].sum()
# print(adult_passengers)



#declares variable
def introduction():
    ticket = {}
    print('Hello!\n' 'We are pleased to inform you that you have been awarded a ticket to board the Titanic. \n'
          'Please enter your information so we can determine what class ticket you won.')
    while True:
        user_sex = input('Are you male or female? ').strip().lower()
        if user_sex != 'male' and user_sex != 'female':
            print('Please Enter Male or female')
        else:
            break
    while True:
        user_age = input('Are you an adult or child? ').strip().lower()
        if user_age != 'child' and user_age != 'adult':
            print('Please enter adult or child')
        else:
            break
    ticket['sex'] = user_sex
    ticket['age'] = user_age
    return ticket

    #determine survival rate




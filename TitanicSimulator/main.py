import numpy as np
import pandas as pd

# reads data from titanic.csv
# index_col removes index column
titanic_csv = pd.read_csv('files/titanic.csv', index_col=0)

user_info = {}


# turns data into a data frame
titanic_df = pd.DataFrame(titanic_csv)
#print(titanic_df)


# gets total number of passengers
total_passengers = titanic_df['Freq'].sum()

#gets classes

#print(total_passengers)


#print(children_passengers)



def child_probability():
    # filters for children
    total_children = titanic_df[titanic_df['Age'] == 'Child']['Freq'].sum()

    #filters for children in 1st class and survived
    first_class_children = titanic_df[(titanic_df['Age'] == 'Child') & (titanic_df['Survived'] == 'Yes')]
    first_class_children = first_class_children[first_class_children['Class'] == '1st']['Freq'].sum()
    print(first_class_children)


child_probability()

#get gender
def get_gender():
    while True:
        user_sex = input('Are you male or female? ').strip().lower()
        if user_sex != 'male' and user_sex != 'female':
            print('Please Enter Male or female')
        else:
            break
    #add input to user info
    user_info['gender'] = user_sex

#get age
def get_age():
    while True:
        user_age = input('Are you an adult or child? ').strip().lower()
        if user_age != 'child' and user_age != 'adult':
            print('Please enter adult or child')
        else:
            break
    #add input to user info
    user_info['age'] = user_age

get_gender()
get_age()
#get class
def get_class(info):
    passenger_class = list(titanic_df['Class'].unique())
    passenger_class = [item.lower() for item in passenger_class]
    #removes crew option if the age is equal to child
    if info['age'] == 'child':
        passenger_class.pop()
    #gives user options for class
    print('Passenger Class Options:')
    for c in passenger_class:
        print(c)
    while True:
        user_class = input('Please enter a class: ').strip().lower()
        if user_class in passenger_class:
            #add class to dictionary
            info['class'] = user_class
            break
        else:
            print('Sorry. Please enter a valid class')

get_class(user_info)
print(user_info)
def introduction():
    print('Hello!\n' 'You are a passenger on the titanic. Please fill out some information to find out if you survive or not.')


    #determine survival rate




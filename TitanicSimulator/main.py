import numpy as np
from numpy import random

import pandas as pd

# reads data from titanic.csv
# index_col removes index column
titanic_csv = pd.read_csv('files/titanic.csv', index_col=0)

user_info = {}

# turns data into a data frame
titanic_df = pd.DataFrame(titanic_csv)

#get gender
def get_gender():
    while True:
        user_sex = input('Are you male or female? ').strip().lower()
        if user_sex != 'male' and user_sex != 'female':
            print('Please Enter Male or female')
        else:
            break
    #add input to user info
    user_info['gender'] = user_sex.title()

#get age
def get_age():
    while True:
        user_age = input('Are you an adult or child? ').strip().lower()
        if user_age != 'child' and user_age != 'adult':
            print('Please enter adult or child')
        else:
            break
    #add input to user info
    user_info['age'] = user_age.title()


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
            if user_class == 'crew':
                user_class = user_class.title()
                info['class'] = user_class
            else:
                info['class'] = user_class
            break
        else:
            print('Sorry. Please enter a valid class')
            for c in passenger_class:
                print(c)


def get_user_input():
    get_gender()
    get_age()
    get_class(user_info)

def probability(user_info):
    # gets group data that matches the user
    group = titanic_df[
        (titanic_df['Age'] == user_info['age'])
        & (titanic_df['Class'] == user_info['class'])
        & (titanic_df['Sex'] == user_info['gender'])
    ]
    #gets total number of people in that specific group
    sum_group = group['Freq'].sum()
    # filters for survivors and turns it into an int
    survivors = int(group[(group['Sex'] == user_info['gender']) & (group['Survived'] == 'Yes')]['Freq'].iloc[0])
    #calculates probability for survival
    survival_probability = round((survivors / sum_group), 2)

    return survival_probability

def titanic_simulator():
    print('Hello!\n' 'You are a passenger on the titanic. Please fill out some information to find out if you survive or not.\n')
    get_user_input()
    print(user_info['class'])

    survival_probability = probability(user_info)
    death_probability = float(1.0 - survival_probability)

    outcome = random.choice(['Survived','Dead'], p=[survival_probability, death_probability])
    if outcome == 'Survived':
        print(f"\nCongratulations, you survived! Your probability of survival  was approximately {survival_probability} or {(survival_probability * 100)}%")
    else:
        print(f"\nSorry, but you didn't survive! Your probability of survival  was approximately {survival_probability} or {(survival_probability * 100)}%")

titanic_simulator()





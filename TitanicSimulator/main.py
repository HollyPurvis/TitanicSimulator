import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import pandas as pd

# reads data from titanic.csv
# index_col removes index column
titanic_csv = pd.read_csv('files/titanic.csv', index_col=0)

user_info = {}
menu_options = ['Home','Survival Probability Simulator', 'Survival Statistics', 'Exit']
menu_location = 0

# turns data into a data frame
titanic_df = pd.DataFrame(titanic_csv)

#get sex
def get_sex():
    while True:
        user_sex = input('Are you male or female? ').strip().lower()
        if user_sex != 'male' and user_sex != 'female':
            print('Please Enter Male or female')
        else:
            break
    #add input to user info
    user_info['sex'] = user_sex.title()

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
    get_sex()
    get_age()
    get_class(user_info)

#allows user to select option
def menu():
    global menu_location

    #removes current menu location from list
    my_menu_options = menu_options
    my_menu_options.pop(menu_location)

    while True:
        for count, k in enumerate(my_menu_options, 1):
            print(f'{count}. {k}')
        selection = input('Please select an option: ')

        # Check if selection is a digit and convert it to an integer
        if selection.isdigit():
            selection = int(selection)
            menu_location = int(selection)
            break

            # Check for the break condition
            if selection == 3:
                menu_location = 0
                break

            # Validate options
            if selection != 1 and selection != 2:
                print("Invalid selection. Please choose again.")
        else:
            print("Invalid input. Please enter a number.")

def check_user_info():
    #checks if user has already selected something
    if not bool(user_info):
        print('Hello!\n' 'Please select from the following to learn more about about those on the Titanic.\n')
        get_user_input()
    else:
        print('You already have the following selected:')
        print(f'Sex: {user_info['sex']}\n'
              f'Age: {user_info['age']}\n'
              f'Class: {user_info['class']}')
        #validates user response
        while True:
            user_selection = input('Would you like to keep what you have selected? (Y/N): ').lower()
            if user_selection != 'y' and user_selection != 'n':
                print('Please enter Y or N')
            else:
                break

        #gets user_selection
        if user_selection == 'n':
            print('Hello!\n' 'Please select from the following to learn more about those on the Titanic.\n')
            get_user_input()

def probability(user_info):
    # gets group data that matches the user
    group = titanic_df[
        (titanic_df['Age'] == user_info['age'])
        & (titanic_df['Class'] == user_info['class'])
        & (titanic_df['Sex'] == user_info['sex'])
    ]
    #gets total number of people in that specific group
    sum_group = group['Freq'].sum()
    # filters for survivors
    survivors = group[(group['Sex'] == user_info['sex']) & (group['Survived'] == 'Yes')]['Freq'].sum()
    #calculates probability for survival
    survival_probability = round((survivors / sum_group), 2)

    return survival_probability

def titanic_simulator():

    check_user_info()

    #print('Hello!\n' 'You are a passenger on the titanic. Please fill out some information to find out if you survive or not.\n')

    survival_probability = probability(user_info)
    death_probability = float(1.0 - survival_probability)

    outcome = random.choice(['Survived','Dead'], p=[survival_probability, death_probability])
    if outcome == 'Survived':
        print(f'\nCongratulations, you survived! Your probability of survival  was approximately {survival_probability} or {(survival_probability * 100)}%')
    else:
        print(f"\nSorry, but you didn't survive! Your probability of survival  was approximately {survival_probability} or {(survival_probability * 100)}%")

#titanic_simulator()

def sex_statistics():
    labels = 'Male', 'Female'

    #get total passenger number
    total_passengers = titanic_df["Freq"].sum()
    female_survivors = titanic_df[(titanic_df['Sex'] == 'Female') & (titanic_df['Survived'] == 'Yes')]["Freq"].sum()
    female_percentage = float((female_survivors / total_passengers) * 100)
    male_survivors = titanic_df[(titanic_df['Sex'] == 'Male') & (titanic_df['Survived'] == 'Yes')]["Freq"].sum()
    male_percentage = float(( male_survivors / total_passengers) * 100)

    percentages = [male_percentage, female_percentage]
    fig, ax = plt.subplots()
    ax.pie(percentages, labels=labels, autopct='%.2f')
    plt.title('Female vs Male Titanic Survivors')
    plt.show()

def age_statistics():
    labels = 'Adult', 'Child'

    #get total passenger number
    total_passengers = titanic_df["Freq"].sum()

    #get adult survivors
    adult_survivors = titanic_df[(titanic_df['Age'] == 'Adult') & (titanic_df['Survived'] == 'Yes')]["Freq"].sum()
    adult_percentage = float((adult_survivors / total_passengers) * 100)

    #get child survivors
    child_survivors = titanic_df[(titanic_df['Age'] == 'Child') & (titanic_df['Survived'] == 'Yes')]["Freq"].sum()
    child_percentage = float(( child_survivors / total_passengers) * 100)

    percentages = [child_percentage, adult_percentage]
    fig, ax = plt.subplots()
    ax.pie(percentages, labels=labels, autopct='%.2f%%')
    plt.title('Adult vs Child Titanic Survivors')
    plt.show()

def class_statistics():
    labels = '1st Class', '2nd Class', '3rd Class', 'Crew'

    #get total passenger number
    total_passengers = titanic_df["Freq"].sum()

    #get 1st Class survivors
    first_class_survivors = titanic_df[(titanic_df['Class'] == '1st') & (titanic_df['Survived'] == 'Yes')]["Freq"].sum()
    first_class_survivors_percentage = float((first_class_survivors / total_passengers) * 100)

    #get 2nd class survivors
    second_class_survivors = titanic_df[(titanic_df['Class'] == '2nd') & (titanic_df['Survived'] == 'Yes')]["Freq"].sum()
    second_class_survivors_percentage = float((second_class_survivors / total_passengers) * 100)

    #get 3rd class survivors
    third_class_survivors = titanic_df[(titanic_df['Class'] == '3rd') & (titanic_df['Survived'] == 'Yes')]["Freq"].sum()
    third_class_survivors_percentage = float((third_class_survivors / total_passengers) * 100)

    #get crew survivors
    crew_class_survivors = titanic_df[(titanic_df['Class'] == 'Crew') & (titanic_df['Survived'] == 'Yes')]["Freq"].sum()
    crew_class_survivors_percentage = float((crew_class_survivors / total_passengers) * 100)

    percentages = [first_class_survivors_percentage, second_class_survivors_percentage, third_class_survivors_percentage, crew_class_survivors_percentage]
    fig, ax = plt.subplots()
    ax.pie(percentages, labels=labels, autopct='%.2f%%')
    plt.title('1st vs 2nd vs 3rd vs Crew Class Titanic Survivors')
    plt.show()


def survival_statistics():
    print('1. Age\n'
          '2. Sex\n'
          '3. Class\n')
    while True:
        user_input = int(input('Please select a category on which you would like to see the statistics of: ').strip())
        if user_input == 1:
            age_statistics()
        elif user_input == 2:
            sex_statistics()
        elif user_input == 3:
            class_statistics()
        else:
            print('1. Age\n'
                  '2. Sex\n'
                  '3. Class\n')
            print("Please enter either 1, 2, or 3")


survival_statistics()

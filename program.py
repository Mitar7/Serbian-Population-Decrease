import pandas as pd
import matplotlib.pyplot as plt
import os

msg = """
    -----------------------------------
    Serbia's population decline problem
    -----------------------------------
    1. Population by selected year
"""

# print(df.loc['2030':, ['Year', 'TotalPopulation']])
# print((df[df['TotalPopulation'] > 8000000]))


def filter_by_year():
    os.system('cls')
    year = int(input('Please enter a year: '))
    if 0 < year < 3000: 
        if year < 2022:
            df = pd.read_csv('hist.csv')
            print(df.loc[df['Year'] == year, ['Year', 'TotalPopulation']])
        else:
            df = pd.read_csv('proj.csv')
            print(df.loc[df['Year'] == year, ['Year', 'TotalPopulation']])
    x = input('Press any key to return to main menu...')
    main()


def main():
    os.system('cls')
    print(msg)
    option = int(input("Please select option: "))
    if option == 1:
        filter_by_year()
    if option == 2:
        print('Do something')
    if option == 3:
        print('Do something')
    if option == 4:
        print('Do something')


if __name__ == '__main__':
    main()

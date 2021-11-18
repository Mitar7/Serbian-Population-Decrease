import pandas as pd
import matplotlib.pyplot as plt
import os

msg = """
    -----------------------------------
    Serbia's population decline problem
    -----------------------------------
    1. Population by selected year
"""

# df = pd.read_csv('proj.csv')
# print(df.loc['2030':, ['Year', 'TotalPopulation']])
# print((df[df['TotalPopulation'] > 8000000]))


def filter_by_year():
    os.system('cls')
    year = input('Please enter a year: ')
    main()


def main():
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

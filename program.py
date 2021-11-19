import pandas as pd
import matplotlib.pyplot as plt
import os

msg = """
    -----------------------------------
    Serbia's population decline problem
    -----------------------------------
    1. Population by selected year
    2. Show population graphic (year <= 2021)
    3. Show population graphic (year > 2020)
    4. Show population graphic (1995 -> 2095)
    5. Highest / Lowest population rank
    6. Exit program
"""


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
    x = input('Press ENTER to return to main menu...')
    main()


def graphic_rep_history():
    df = pd.read_csv('hist.csv')
    df['TotalPopulation'] = df['TotalPopulation'] / 1000000
    df.plot(x='Year', y='TotalPopulation', kind='line', ylabel='Population in Millions', xlabel='Year')
    plt.show()
    x = input('Press ENTER to return to main menu...')
    main()


def graphic_rep_future():
    df = pd.read_csv('proj.csv')
    df['TotalPopulation'] = df['TotalPopulation'] / 1000000
    df.plot(x='Year', y='TotalPopulation', kind='line', ylabel='Population in Millions', xlabel='Year')
    plt.show()
    x = input('Press ENTER to return to main menu...')
    main()


def graphic_rep_combine():
    a = pd.read_csv('hist.csv')
    b = pd.read_csv('proj.csv')
    df = pd.merge(a, b, on=["Year", "TotalPopulation", "GrowthRate", "Density", "TotalPopulationRank", "DensityRank"],
                  how='outer')
    df.sort_index()
    df['TotalPopulation'] = df['TotalPopulation'] / 1000000
    df.plot(x='Year', y='TotalPopulation', kind='line', ylabel='Population in Millions', xlabel='Year')
    plt.show()
    x = input('Press ENTER to return to main menu...')
    main()


def population_rank():
    os.system('cls')
    a = pd.read_csv('hist.csv')
    b = pd.read_csv('proj.csv')
    df = pd.merge(a, b, on=["Year", "TotalPopulation", "GrowthRate", "Density", "TotalPopulationRank", "DensityRank"],
                  how='outer')
    min_population_rank = df['TotalPopulationRank'].min()
    max_population_rank = df['TotalPopulationRank'].max()
    print(f"""
        Highest population rank: {min_population_rank}
        Lowest population rank: {max_population_rank}
    """)
    x = input('Press ENTER to return to main menu...')
    main()


def main():
    os.system('cls')
    print(msg)
    option = int(input("Please select option: "))
    if option == 1:
        filter_by_year()
    if option == 2:
        graphic_rep_history()
    if option == 3:
        graphic_rep_future()
    if option == 4:
        graphic_rep_combine()
    if option == 5:
        population_rank()
    if option == 6:
        exit()


if __name__ == '__main__':
    main()

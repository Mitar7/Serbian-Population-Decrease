import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('proj.csv', index_col='Year')
print(df['TotalPopulation'])
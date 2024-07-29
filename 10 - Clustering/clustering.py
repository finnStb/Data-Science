



import pandas as pd

# read the data "data/country.txt" that is in csv format style
data = pd.read_csv("data/country.txt", sep=",")

print(data.head())


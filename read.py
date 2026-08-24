import pandas as pd

titanic = pd.read_csv("data/titanic.csv")

print(titanic.head(15))
print(titanic.tail(15))
print(titanic.dtypes)
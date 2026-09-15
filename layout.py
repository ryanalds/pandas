import pandas as pd

titanic = pd.read_csv('data/titanic.csv')
air_quality = pd.read_csv(
    "data/air_quality_long.csv", index_col="date.utc", parse_dates=True
)

titanic = titanic[['PassengerId', 'Age', 'Pclass', 'Name']]
# titanic = titanic.sort_values(by='Age') # ordenando a tabela pelo valor da coluna Age

titanic = titanic.sort_values(by=['Pclass', 'Age'], ascending=False) # ordenando a tabela pelo valor da coluna Pclass e, em caso de empate, pelo valor da coluna Age. O parâmetro
# asceding=False significa que a ordenação será feita de forma decrescente, ou seja, do maior para o menor valor da coluna Age.
# print(titanic.head())

no2 = air_quality[air_quality["parameter"] == "no2"]

print(no2.head())
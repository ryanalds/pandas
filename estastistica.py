import pandas as pd

titanic = pd.read_csv("data/titanic.csv")

# print("Mean ", round(titanic["Age"].mean(), 2)) # printando a media usando o metodo mean e formatando para dois digitos depois da virgula com round
# print(round(titanic[["Age", "Fare"]].median(), 2))
# print(round(titanic[["Age", "Fare"]].describe(), 2)) #usando o describe filtrando as colunas e arrendondando com o round

# print(round(titanic.agg(
#     {
#     "Age" : [ "max", "min", "median", "skew", "mean", "std"],
#     "Fare" : [ "max", "min", "median", "skew", "mean", "std"],
#     }
# ), 2)) #selecionando as estastisticas que seram printada de cada coluna

# titanic = titanic[["Age", "Sex"]].groupby("Sex").mean()
# filtrando as duas colunas e agrupando por sexo e calculando a media de cada grupo

# # titanic = titanic.groupby("Sex").mean(numeric_only=True) #agrupando por SEX e passando para mostrar todas as colunas
# print(round(titanic, 2))

print(titanic["Pclass"].value_counts()) # contando quantos passageiros tem para cada tipo de classe
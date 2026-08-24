import pandas as pd

titanic = pd.read_csv("data/titanic.csv") #lendo um arquivo csv e armazenando numa variavel

# print(titanic.head(15)) #printa as 15 primeiras linhas
# print(titanic.tail(15)) #printa as 15 ultimas linhas
# print(titanic.dtypes) #printa os tipos de dados das colunas

# convertendo para excel, declarando o nome da tabela "passengers" e tirando os indices 
titanic.to_excel("data/titanic.xlsx", sheet_name="passengers", index=False)

titanic = pd.read_excel("data/titanic.xlsx", sheet_name="passengers")

# print(titanic.info()) #printa informações sobre a tabela
print(titanic)
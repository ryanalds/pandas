import pandas as pd

titanic = pd.read_csv("data/titanic.csv")

print(titanic.head())

# filtrar por idade
# age = titanic["Age"]
# print(age.head()) #retorna dados unidimensionais = series

# print(titanic.shape) #printa a quantidade de linhas e colunas

# age_sex = titanic[["Age", "Sex"]]
# print(age_sex.head()) #retorna dados bidimensionais = dataFrame

# above_35 = titanic[titanic["Age"] > 35] #filtra a tabela e retorna apenas as linhas com idade maior que 35
# print(above_35.head())

# class_23 = titanic[titanic["Pclass"].isin([2,3])] #isin() função condicional retorna um valor Truepara cada linha em que os valores estão na lista fornecida
# print(class_23.head())

# age_no_na = titanic[titanic["Age"].notna()] #A notna()função condicional retorna um valor Truepara cada linha em que os valores não são Nullválidos
# print(age_no_na.head())

# adult_names = titanic.loc[titanic["Age"] > 35, "Name"] #Ao usar loc, a parte antes da vírgula representa as linhas desejadas e a parte depois da vírgula representa as colunas que você deseja selecionar
# print(adult_names.head)

# f = titanic.iloc[9:25, 2:6] #Quando estiver especificamente interessado em determinadas linhas e/ou colunas com base em sua posição na tabela, use o iloc
# print(f)
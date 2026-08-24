import pandas as pd

# criando dataFrame (Tabela)
df = pd.DataFrame(
    {
        "Name" : [
             "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss Elizabeth",
        ],
        "Age" : [22,35,58],
        "Sex" : ["Male", "Male", "Female"],
    }
)

# adicionando nova coluna com sua label "Active"
df["Active"] =  True

print(df)
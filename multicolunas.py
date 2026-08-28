import pandas as pd

air_quality = pd.read_csv("data/air_quality_no2.csv", index_col=0, parse_dates=True)

air_quality["london_mg_per_cubic"] = air_quality["station_london"] * 1.882 # fazendo calculo com uma coluna existente e criando noca coluna

air_quality["ratio_paris_antwerp"] = air_quality["station_paris"] / air_quality["station_antwerp"] # criando nova coluna a partir de operação com duas colunas ja existentes

air_quality_renamed = air_quality.rename(
    columns={
        "station_antwerp": "BETR801",
        "station_paris": "FR04014",
        "station_london": "London Westminster",
    }
)

air_quality_renamednew = air_quality_renamed.rename(columns= str.upper) #passando como parametro do rename uma função para deixar todas as colunas com nome maiusculo

print(air_quality_renamednew.head())
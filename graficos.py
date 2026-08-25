import pandas as pd
import matplotlib.pyplot as plt

air_quality = pd.read_csv('data/air_quality_no2.csv', index_col=0, parse_dates=True)

# air_quality.plot()
# plt.show() #cria grafico de linhas por padrão

# air_quality["station_antwerp"].plot() #filtrando a coluna, o plot em line é o padrão 

# air_quality.plot.scatter(x="station_london", y="station_paris", alpha=0.5) # passando qual coluna será o eixo x e y, alpha controla a opacidade do ponto

# air_quality.plot.box()

axs = air_quality.plot.area(figsize=(12,4),xlabel="Date Time",subplots=True) # grafico de area

plt.savefig("data/grafico.png")
plt.show()
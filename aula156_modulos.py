# from aula156_mod import exp
# import aula108_funcoes
# # print(exp(2))
# res = aula108_funcoes.soma(2,3,5)
# print(res)

from matplotlib import pyplot as plt

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]
# cria um gráfico de linha, anos no eixo x, gdp no eixo y
plt.plot(years, gdp, color='blue', marker='o', linestyle='solid')
# adiciona um título
plt.title("GDP Nominal")
# adiciona um selo no eixo y
plt.xlabel("Anos")
plt.ylabel("Bilhões de $")
plt.show()
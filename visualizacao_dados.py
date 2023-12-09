from matplotlib import pyplot as plt

# years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
# gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]
# # cria um gráfico de linha, anos no eixo x, gdp no eixo y
# plt.plot(years, gdp, color='blue', marker='o', linestyle='solid')
# # adiciona um título
# plt.title("GDP Nominal")
# # adiciona um selo no eixo y
# plt.xlabel("Anos")
# plt.ylabel("Bilhões de $")
# plt.show()

movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]
# barras possuem o tamanho padrão de 0.8, então adicionaremos 0.1 às
# coordenadas à esquerda para que cada barra seja centralizada
xs = [i + 0.1 for i, _ in enumerate(movies)]
# as barras do gráfico com as coordenadas x à esquerda [xs], alturas [num_oscars]
plt.bar(xs, num_oscars)
plt.ylabel("# de Premiações")
plt.title("Meus Filmes Favoritos")
# nomeia o eixo x com nomes de filmes na barra central
plt.xticks([i + 0.1 for i, _ in enumerate(movies)], movies)
plt.show()
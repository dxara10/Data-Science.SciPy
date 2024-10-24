from scipy.stats import norm

# Gerar 1000 amostras de uma distribuição normal padrão
amostras = norm.rvs(size=1000)

# Média e Desvio Padrão
media = norm.mean()
desvio_padrao = norm.std()

print("Média:", media)
print("Desvio Padrão:", desvio_padrao)

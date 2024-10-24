from scipy import stats
import numpy as np

# Dados
grupo1 = np.array([85, 90, 88, 82, 87])
grupo2 = np.array([78, 80, 85, 75, 82])

# Teste t de Student para médias iguais
t_stat, p_valor = stats.ttest_ind(grupo1, grupo2)

print("Estatística t:", t_stat)
print("Valor p:", p_valor)

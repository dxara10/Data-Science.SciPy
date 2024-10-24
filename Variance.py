from scipy import stats
import numpy as np

# Dados
grupo1 = np.array([85, 90, 88, 82, 87])
grupo2 = np.array([78, 80, 85, 75, 82])
grupo3 = np.array([72, 68, 74, 80, 73])

# ANOVA
f_stat, p_valor = stats.f_oneway(grupo1, grupo2, grupo3)

print("Estatística F:", f_stat)
print("Valor p:", p_valor)

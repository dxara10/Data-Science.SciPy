from scipy import stats
import numpy as np

# Dados
X = np.array([1, 2, 3, 4, 5])
y = np.array([2, 3, 4, 5, 6])

# Regressão linear
slope, intercept, r_value, p_value, std_err = stats.linregress(X, y)

print("Coeficiente Angular:", slope)
print("Intercepto:", intercept)
print("Coeficiente de Correlação:", r_value)
print("Valor p:", p_value)

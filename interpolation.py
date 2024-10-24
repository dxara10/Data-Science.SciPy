from scipy import interpolate
import numpy as np

# Dados
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 3, 4, 5, 6])

# Interpolação
interp_func = interpolate.interp1d(x, y, kind='linear')

# Valor interpolado para x = 2.5
valor_interpolado = interp_func(2.5)

print("Valor interpolado:", valor_interpolado)

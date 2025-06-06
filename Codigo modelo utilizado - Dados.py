import numpy as np
import matplotlib.pyplot as plt

def energia_escape(f):
    delta_U_grande = (np.sqrt(1 + f**2) - f)
    delta_U_pequena = (np.sqrt(1 + f**2) - 1)
    Z = 2*delta_U_grande + 4*delta_U_pequena
    P_grande = delta_U_grande / Z
    P_pequena = delta_U_pequena / Z
    return P_grande, P_pequena

# Rango de f
f_values = np.linspace(0.1, 0.99, 100)
P_grande, P_pequena = zip(*[energia_escape(f) for f in f_values])

# Gráfica
plt.figure(figsize=(10, 6))
plt.plot(f_values, P_grande, color='blue', lw=2, label='Cara Grande ($L \\times L$)')
plt.plot(f_values, P_pequena, color='red', lw=2, label='Cara Pequeña ($L \\times fL$)')
plt.xlabel('Factor de deformación $f$', fontsize=12)
plt.ylabel('Probabilidad', fontsize=12)
plt.title('Modelo de Disipación Energética\nProbabilidades por Cara', fontsize=14)
plt.legend()
plt.grid(alpha=0.3)
plt.show()

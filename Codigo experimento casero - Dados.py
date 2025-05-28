import numpy as np
import matplotlib.pyplot as plt

# Datos experimentales
caras = ['1', '2', '3', '4', '5', '6']
f05 = [36, 5, 6, 7, 8, 38]  # f=0.5
f025 = [50, 3, 1, 0, 0, 46]  # f=0.25

# Convertir a porcentajes
total = 100
f05 = np.array(f05)/total
f025 = np.array(f025)/total

# Configuración de la gráfica
x = np.arange(len(caras))
ancho = 0.35

plt.figure(figsize=(14, 8))

# Crear barras
rects1 = plt.bar(x - ancho/2, f05, ancho, color='royalblue', edgecolor='black', label='f=0.5 ')
rects2 = plt.bar(x + ancho/2, f025, ancho, color='darkorange', edgecolor='black', label='f=0.25')


# Personalización
plt.title('Comparación de Probabilidades por Cara: f=0.5 vs f=0.25\n(Datos Experimentales)', fontsize=14)
plt.xlabel('Cara del Dado', fontsize=12)
plt.ylabel('Probabilidad (%)', fontsize=12)
plt.xticks(x, caras, fontsize=12)
plt.yticks(np.arange(0, 0.55, 0.05), [f'{int(i*100)}%' for i in np.arange(0, 0.55, 0.05)])
plt.grid(axis='y', alpha=0.3)
plt.ylim(0, 0.55)

# Añadir valores
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.annotate(f'{height*100:.1f}%',
                    xy=(rect.get_x() + rect.get_width()/2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=9)

autolabel(rects1)
autolabel(rects2)

# Añadir anotaciones clave (versión centrada)
plt.text(1.72, 0.52, 'Caras Grandes (L×L)\nMayor probabilidad con menor f',
        ha='center', color='green', fontsize=11, weight='bold',
        bbox=dict(facecolor='white', edgecolor='green', boxstyle='round,pad=0.3'))

plt.text(3.25, 0.52, 'Caras Pequeñas (L×fL)\nPrácticamente desaparecen con f=0.25',
        ha='center', color='red', fontsize=11, weight='bold',
        bbox=dict(facecolor='white', edgecolor='red', boxstyle='round,pad=0.3'))

plt.legend(loc='upper left', fontsize=10)
plt.tight_layout()
plt.show()

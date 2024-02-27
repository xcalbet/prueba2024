import random

# Parametros
numero_pasos = 1000
desviacion_estandar = 0.1
media = 0.0

# Simulaci?n del camino aleatorio
camino = [0]
for i in range(1, numero_pasos):
#camino con tendencia
  media = 0,01*i
  paso = random.normalvariate(media, desviacion_estandar)
  camino.append(camino[-1] + paso)

# Grafica del camino 
import matplotlib.pyplot as plt

plt.plot(camino)
plt.xlabel("Paso")
plt.ylabel("Valor")
plt.show()



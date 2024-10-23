import os

os.system('cls')


import numpy as np


valores = [150000, 180000, 200000, 220000, 250000, 280000, 300000, 320000, 400000, 1500000]

media = np.mean(valores)
mediana = np.median(valores)
print('Média: ', media)
print('Mediana: ', mediana)
print('O valor que melhor representa o "valor típico" das casas vendidas seria a mediana, pois o valor de 1.500.000 é um valor muito elevado comparado aos outros valores.')
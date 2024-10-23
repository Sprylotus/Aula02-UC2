import os

os.system('cls')


import numpy as np


import pandas as pd 


df = pd.read_excel('vendas_eletos_eletronicos2.xlsx')
print(df)

prod = df['Nome do Produto']
total = df['Total']

media = np.mean(total)
mediana = np.median(total)

q1 = np.quantile(total, 0.25)
q2 = np.quantile(total, 0.50)
q3 = np.quantile(total, 0.75)

print(95 * '=')
print('TENDÊNCIA CENTRAL')
print(f'Média: {media}')
print(f'Mediana: {mediana}')

print(95 * '=')
print('TENDÊNCIA POSICIONAL')
print(f'25% DOS PRODUTOS TEM VALOR TOTAL DE VENDA INFERIOR A R${q1}')
print(f'50% DOS PRODUTOS TEM VALOR TOTAL DE VENDA INFERIOR A R${q2}')
print(f'75% DOS PRODUTOS TEM VALOR TOTAL DE VENDA INFERIOR A R${q3}')

print(95 * '=')
print('MAIS VENDIDOS')
mais_vdd = df[df['Total']>q3].sort_values(by='Total', ascending=False)
print(mais_vdd)
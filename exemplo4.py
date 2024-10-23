import pandas as pd


import numpy as np


df = pd.read_excel('vendas_roupas1.xlsx')
# print(df)


categoria = df['Categoria']
quantidade_vendida = df['Quantidade Vendida']
# print(quantidade_vendida.describe())
# print(categoria.unique())

q1 = np.quantile(quantidade_vendida, 0.25)
q2 = np.quantile(quantidade_vendida, 0.50)
q3 = np.quantile(quantidade_vendida, 0.75)

# print(f'Q1 25%: {q1}')
# print(f'Q2 50%: {q2}')
# print(f'Q3 75%: {q3}')

media = np.mean(quantidade_vendida)
mediana = np.median(quantidade_vendida)

# print(f'Média: {media}')
# print(f'Mediana: {mediana}')

qtdvdd_org = df.sort_values(by="Quantidade Vendida", ascending=True)
qtd_vdd = qtdvdd_org['Quantidade Vendida']
print(qtd_vdd.values)
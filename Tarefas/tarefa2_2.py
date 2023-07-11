import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df1 = pd.read_excel(r'D:\POLI - UPE\2023.1\LPAA\Material Complementar\Aracaju.xlsx')
df2 = pd.read_excel(r'D:\POLI - UPE\2023.1\LPAA\Material Complementar\Fortaleza.xlsx')
df3 = pd.read_excel(r'D:\POLI - UPE\2023.1\LPAA\Material Complementar\Natal.xlsx')
df4 = pd.read_excel(r'D:\POLI - UPE\2023.1\LPAA\Material Complementar\Recife.xlsx')
df5 = pd.read_excel(r'D:\POLI - UPE\2023.1\LPAA\Material Complementar\Salvador.xlsx')


dados1= pd.merge(df1, df2,how = 'outer')
dados2 = pd.merge(df3, df4,how = 'outer')
dados3 = pd.merge(dados1, dados2,how = 'outer')
dados = pd.merge(dados3, df5,how = 'outer')

fig, ax = plt.subplots()
plt.bar('Cidade', 'Vendas', data=dados)
# Add labels and title
ax.set_xlabel('Cidade')
ax.set_ylabel('Vendas')
ax.set_title('Vendas por Cidade')

# Display the plot
plt.show()
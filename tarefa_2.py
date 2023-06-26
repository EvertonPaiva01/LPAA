import pandas as pd
import numpy as np

### Construção Series e DataFrame
#Series
obj = pd.Series([4, 7, -5, 3])

#Data Frame
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
'year': [2000, 2001, 2002, 2001, 2002, 2003],
'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}

df = pd.DataFrame(data)

print(obj)
print(df)

### Slicing e indexação
#Slicing
print(df['state'][3:])

#indexação
print(df['year'].iloc[(2)])

### Operações aritméticas e lógicas com Séries e DataFrame
#Series
obj2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
print(obj2 * 2)
print(np.exp(obj2))

#DataFrame
df2 = df.copy()
print(df2*2)
print(df2.min())
print(df2.max())

### Métodos de Preenchimento
df1 = pd.DataFrame(np.arange(12.).reshape((3, 4)),columns=list('abcd'))
df2 = pd.DataFrame(np.arange(20.).reshape((4, 5)),columns=list('abcde'))
print('='*30)
print(df1)
print(df2)
print('='*30)
df2.loc[1,'b'] = np.nan
print(df2)
print('='*30)
print('df1 + df2:')
print(df1 + df2)

### Ordenação e Classificação
obj = pd.Series(range(4), index=['d', 'a', 'b', 'c'])
print(obj)
print('='*30)
print(obj.sort_index())


frame = pd.DataFrame(np.arange(8).reshape((2, 4)),index=['three', 'one'],columns=['d', 'a', 'b', 'c'])
print(frame)
print('='*30)
print(frame.sort_index())
frame.sort_index(axis=1)
print('='*30)
print(frame.sort_index(axis=1))

### Funções estatísticas no pandas
df = pd.DataFrame([[1.4, np.nan], [7.1, -4.5],[np.nan, np.nan], [0.75, -1.3]],index=['a', 'b', 'c', 'd'],columns=['one', 'two'])
print(df)
print('='*30)
#Somando colunas:
print(df.sum())
print('='*30)
print(df.sum(axis='columns'))
#máximo
print('='*30)
print(df.max())
#mínimo
print('='*30)
print(df.min())
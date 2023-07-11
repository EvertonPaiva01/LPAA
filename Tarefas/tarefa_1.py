import numpy as np

#----------- Construção de Array Unidimensional e Multidimensional----------- #

#Construção de Array Unidimensional:
unid_array = np.arange(1,11)

#Construção de Array Multidimensional:
multd_array = np.array([np.arange(10),np.arange(11,21)])

#print array Unidimensional:
unid_array

#print array Multidimensional:
multd_array



#-----------  Slicing e indexação ----------- #

# Array Unidimensional

#pegando o primeiro elemento do array:
print(f'o primeiro elemento do array Unidimensional: {unid_array[0]}')

#pegando os 3 ultimos elementos do array:
print(f'\nos 3 ultimos elementos do array: {unid_array[-3:]}')

# Array Multidimensional:

#pegando o primeiro elemento da linha e primeira coluna:
multd_array[0][0]
print(f'\no primeiro elemento da linha e primeira coluna: {multd_array[0][0]}')
#pegando os 3 ultimos elementos de cada linha:
multd_array[0:,7:]
print(f'\nos 3 ultimos elementos de cada linha:\n {multd_array[0:,7:]}')


#-----------  Operações com arrays (lógicas, aritméticas e algébricas) ----------- #

#Criando uma cópias dos arrays:
_unid_array= unid_array.copy()
_multd_array=multd_array.copy()

#multiplicação:
print(f' unid_array * unid_array: {_unid_array * _unid_array}\n')
print(f'multd_array * multd_array: {_multd_array * _multd_array}\n')

#soma:
print(f' unid_array + unid_array: {_unid_array + _unid_array}\n')
print(f' multd_array + multd_array: {_multd_array + _multd_array}\n')

#Subtração:
print(f' unid_array - unid_array: {_unid_array - _unid_array}\n')
print(f' multd_array - multd_array: {_multd_array - _multd_array}\n')

#Raiz quadrada:
print(f' sqrt(unid_array) : {_unid_array**(1/2)}\n')
print(f' sqrt(multd_array) : {_multd_array**(1/2)}\n')


#-----------  Principais métodos utilizados pelos objetos Numpy ----------- #
# cria um array com todos os elementos sendo 0
print( np.zeros(10))

# cria um array com todos os elementos sendo 1
print( np.ones(10))

# cria um array cujo conteúdo inicial é aleatório.
print( np.empty(10))

#-----------  Funções universais e estatísticas com Numpy ----------- #
e = np.random.randn(5, 4)
print(e)

# Média:
print(f'\nMédia do array : {e.mean()}')

#soma:
print(f'\nSoma do array : {e.sum()}')

#Desvio padrão:std
print(f'\nDesvio padrão do array : {e.std()}')


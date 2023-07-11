# -*- coding: utf-8 -*-
"""
LPAA - Linguagem de Programação Aplicada a Automação - 2020.1

- Pandas (Comandos e Generalidades)


Professor: Emmanuel Andrade
"""

""""
Aula Carga de dados e manipulação de arquivos

- São trabalhados (por hora) apenas com arquivos do tipo CSV, Excel e txt.

"""

import pandas as pd
import numpy as np


df = pd.read_csv('J:\Professional\Documents\Disciplinas - POLI2020.1\LPAA\Codigos\ex (2).csv')

df

pd.read_table('J:\Professional\Documents\Disciplinas - POLI2020.1\LPAA\Codigos\ex (2).csv', sep=',')


#arquivo sem cabeçalho
pd.read_csv('J:\Professional\Documents\Disciplinas - POLI2020.1\LPAA\Codigos\ex (3).csv')

pd.read_csv('J:\Professional\Documents\Disciplinas - POLI2020.1\LPAA\Codigos\ex (3).csv',names=['a','b','c','d','message'])

#indexação de coluna poro um array
names=['a','b','c','d','message']

pd.read_csv('J:\Professional\Documents\Disciplinas - POLI2020.1\LPAA\Codigos\ex (3).csv',names=names,index_col='message')

#indice hierarquico
pd.read_csv('J:\Professional\Documents\Disciplinas - POLI2020.1\LPAA\Codigos\ex (1).csv')

parsed=pd.read_csv('J:\Professional\Documents\Disciplinas - POLI2020.1\LPAA\Codigos\ex (1).csv',index_col=['key1','key2'])

parsed

#tabela sem delimitador fixo, que usam espaço em branco ou outro padrão para separar os campos

list(open('J:\Professional\Documents\Disciplinas - POLI2020.1\LPAA\Codigos\ex3.txt'))

result = pd.read_table('J:\Professional\Documents\Disciplinas - POLI2020.1\LPAA\Codigos\ex3.txt', sep='\s+')
#read_table infere que a primeira coluna é de indice do dataframe

result

#funções de parser (analisadores sintáticos que possuem regras de entrad) para remoção de linhas específicas

#Pesquise sobre parsing (ou funções de parser)
teste = pd.read_csv('J:\Professional\Documents\Disciplinas - POLI2020.1\LPAA\Codigos\ex (5).csv')

pd.read_csv('J:\Professional\Documents\Disciplinas - POLI2020.1\LPAA\Codigos\ex (5).csv',skiprows=[0,2,3])

#Lidando com valores ausente

result = pd.read_csv('J:\Professional\Documents\Disciplinas - POLI2020.1\LPAA\Codigos\ex (6).csv')

pd.isnull(result)

result = pd.read_csv('J:\Professional\Documents\Disciplinas - POLI2020.1\LPAA\Codigos\ex (6).csv',na_values=['NULL'])

result

sentinels = {'message':['foo','NA'],'something':['two']}

pd.read_csv('J:\Professional\Documents\Disciplinas - POLI2020.1\LPAA\Codigos\ex (6).csv',na_values=sentinels)

#Lendo Arquivos-texto em Parte

pd.options.display.max_rows = 10

result = pd.read_csv('J:\Professional\Documents\Disciplinas - POLI2020.1\LPAA\Codigos\ex (7).csv')


pd.read_csv('J:\Professional\Documents\Disciplinas - POLI2020.1\LPAA\Codigos\ex (7).csv', nrows=5)

#trabalhando com pedaços

chunker = pd.read_csv('J:\Professional\Documents\Disciplinas - POLI2020.1\LPAA\Codigos\ex (7).csv', chunksize =1000)

chunker

tot = pd.Series([])
for piece in chunker:
    tot=tot.add(piece['key'].value_counts(),fill_value=0)
    
tot = tot.sort_values(ascending=False)


chunker
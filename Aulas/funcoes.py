# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 18:12:56 2022

@author: Emmanuel Andrade

Funções:
    - Bloco de codigo identificado por um nome
    - Pode receber uma lista de parâmetros
    - Pode ser reutilizada/reaproveitada
    - Torna o código mais estruturado

"""

## Criando a primeira função

def exibir_mensagem():
    print("Olá mundo!")


def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")


def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}!")


exibir_mensagem()
exibir_mensagem_2(nome="Fulano")
exibir_mensagem_3()
exibir_mensagem_3(nome="Beltrano")

### usando uma função com retorno

def calcular_total(numeros):
    return sum(numeros)

def soma_3_numeros(a,b,c):
    return(a+b+c)


def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    return antecessor, sucessor

def par_ou_impar(num):
    if (num%2)==0:
        return 'par'
    else:
        return 'ímpar'


print(calcular_total([10, 20, 34]))  # 64
print(retorna_antecessor_e_sucessor(10))  # (9, 11)


#estrutura de argumentos nomeados

def salvar_carro(marca, modelo, ano, placa):
    # salva carro no banco de dados...
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")


salvar_carro("Fiat", "Palio", 1999, "ABC-1234")
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")
salvar_carro(**{ "marca":"Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"})

# uso de args e kwargs

"""
*args e **kwargs são argumentos utilizados em funções, e possuem construções
distintas

o operador "*" e "**" não são ponteiros, são operadores de desempacotamento

*args trabalha com tuplas e é um objeto iterável

**kwargs trabalha com chave:valor


"""
#função genérica
def my_function(a, b, *args, **kwargs):
    pass

#função de soma de inteiros
def my_sum(my_integers):
    result = 0
    for x in my_integers:
        result += x
    return result

list_of_integers = [1, 2, 3]
print(my_sum(list_of_integers))

#reecrevendo a função acima utilizando *args
def my_sum(*args):
    result = 0
    # Iterating over the Python args tuple
    for x in args:
        result += x
    return result

print(my_sum(1, 2, 3))


def my_sum(*integers):
    result = 0
    for x in integers:
        result += x
    return result

print(my_sum(1, 2, 3))



def concatenate(**kwargs):
    result = ""
    # Iterating over the Python kwargs dictionary
    for arg in kwargs.values():
        result += arg
    return result

print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))




# função somente com parâmetros de posição

"""
função genérica (estrutura):
    
    def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2)
    
         positional      posicional      apenas chave:valor
                         ou chave:valor

"""


def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)


criar_carro("Palio", 1999, "ABC-1234",
            marca="Fiat", motor="1.0", combustivel="Gasolina")#correto

criar_carro(modelo="Palio", ano=1999, placa="ABC-1234",
            marca ="Fiat", motor="1.0", combustivel="Gasolina")  # inválido


#função somente com parâmetros por nome

# def criar_carro(modelo, ano, placa, /, *, marca, motor, combustivel):
#     print(modelo, ano, placa, marca, motor, combustivel)


"""
Objetos de Primeira classe

Funções também são objetos (isso as tornam objetos de primeira classe)
    - Possibilidade de atribuir funções à variáveis e/ou passar como 
    parâmetro de funções e/ou utilizá-las como elementos em listas, tuplas, etc.
"""


def somar(a, b):
    return a + b
def subtracao(a,b):
    return a-b


def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação {a} + {b} = {resultado}")


exibir_resultado(10, 10, somar)  # O resultado da operação 10 + 10 = 20


#variáveis globais x variáveis locais


salario = 2000
bonus=300


def salario_bonus(bonus_var):
    global salario
    salario += bonus_var
    return salario


salario_bonus(bonus)  # 2300
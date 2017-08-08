# -*- coding: utf-8 -*-

"""2.Lista.


Declaração
Acessando elementos
Adicionando elementos
Removendo elementos
"""

# Declarando uma lista.
lista = ['João', 'Pedro', 'Antonio', 'Carlos',]

# Acessando elementos individualmente.
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])

# Acessando elementos através do loop.
for item in lista:
    print(item)

# Imprimindo uma mensagem para cada nome.
saudacao = "Bom dia "
for item in lista:
    mensagem = saudacao + item + "!"
    print(mensagem)

# Modificando elementos na lista.
lista[2] = "José"
print(lista)

# Adicionando elementos na lista.
lista.append("Paulo")
print(lista)

# Removendo elementos de uma lista.
del lista[3]

# Inserindo elementos na lista.
lista.insert(3, "Francisco")
print(lista)

# Removendo itens da lista com pop.
removido = []
removido.append(lista.pop())

mensagem = "Convidado removido: " + removido[-1]
print(mensagem)
print("Convidados: " + ", ".join(lista))

convidados_encontrados = ['Benedito', 'Joaquim', 'Manoel']

print("Convidados em potencial: " + ", ".join(convidados_encontrados))
lista.insert(0, convidados_encontrados.pop(0))
print("Convidados confirmados: " + ", ".join(lista))

print("Convidados em potencial: " + ", ".join(convidados_encontrados))
lista.insert(3, convidados_encontrados.pop(0))
print("Convidados confirmados: " + ", ".join(lista))

print("Convidados em potencial: " + ", ".join(convidados_encontrados))
lista.append(convidados_encontrados.pop(0))
print("Convidados confirmados: " + ", ".join(lista))

for convidado in lista:
    mensagem = "Olá " + convidado + ", " + "venha participar do meu \
jantar?"        
    print(mensagem)

# Organizando uma lista
places = ['Vancoucer', 'Londres', 'Toquio', 'Los Angeles', 'Oslo', ]

print("Meus lugares escolhidos: " + ', '.join(places) + ".")
places_sorted = sorted(places)
print("Meus lugares escolhidos: " + ', '.join(places_sorted) + ".")
places_sorted_reverse = sorted(places, reverse=True)
print("Meus lugares escolhidos: " + ', '.join(places_sorted_reverse) + ".")
print("Meus lugares escolhidos: " + ', '.join(places) + ".")
places.reverse()
print("Meus lugares escolhidos: " + ', '.join(places) + ".")
places.reverse()
print("Meus lugares escolhidos: " + ', '.join(places) + ".")
places.sort()
print("Meus lugares escolhidos: " + ', '.join(places) + ".")
places.sort(reverse=True)
print("Meus lugares escolhidos: " + ', '.join(places) + ".")

print("Quantidade de convidados: " + str(len(lista)))

# Listas númericas.

lista_de_numeros = [0,1,2,3,4,5,6,7,8,9]
print(lista_de_numeros)

# O mesmo resultado será obtido com:
lista_de_numeros = list(range(0,10))
print(lista_de_numeros)

# Contando até vinte:
for numero in range(1,21):
    print(numero, end=" ")

print()

# Gerando uma lista até 100.
lista_de_milhao = list(range(1,101))

# Recuperando o menor e o maior número da lista.
print(min(lista_de_milhao))
print(max(lista_de_milhao))

# Somando todos os itens da lista.
soma_da_lista = sum(lista_de_milhao)
print(soma_da_lista)

# Gerando e imprimindo os impares de 1 a 20.
for numero in range(1, 21, 2):
    print(numero, end=" ")

print()

# Múltiplos de 3 até 30.
for numero in range(3, 31, 3):
    print(numero, end=" ")

print()

# 10 primeiros cubos.
for numero in range(1, 11,):
    print(numero**3, end=" ")

print()

# list comprehension.
cubos = [numero**3 for numero in range(1,11)]
print(cubos)

'''
list comprehension divide-se em 3 partes:
1 - a variável que guardará os valores, a lista em si.
2 - a operação a ser realizada em cada loop
3 - o for com o intervalo definido.

Ex.:

   1           2                   3
cubos = | [numero**3 | for numero in range(1,11)]

'''

# Outros exemplo.
[print(numero, end=" ") for numero in range(1, 11, 2)]
print()

# Slices em Python
print(lista)

# Slicing a lista
print("lista[0:2] => ", lista[0:2])
print("lista[2:5] => ", lista[2:5])
print("lista[0:] => ", lista[0:])
print("lista[:4] => ", lista[:4])

# O primeiros 3 itens.
print("O primeiros 3 itens: ", lista[0:3])
print("3 itens a partir do meio são: ", lista[3:])
print("3 itens a partir do meio são: ", lista[-3:])

# Copiando listas.
lista_cidades_1 = ['Araras', 'Leme', 'Pirassununga', 'Descalvado',]
lista_cidades_2 = []

print("lista_cidades_1: ", lista_cidades_1, end=" ")
print()
print("lista_cidades_2: ", lista_cidades_2, end=" ")
print()
print("Copiando a lista 1 para a 2:")
lista_cidades_2 = lista_cidades_1[:]
print("lista_cidades_1: ", lista_cidades_1, end=" ")
print()
print("lista_cidades_2: ", lista_cidades_2, end=" ")
print("\nAlterando a lista 1")
lista_cidades_1.append("São Carlos")
print("lista_cidades_1: ", lista_cidades_1, end=" ")
print()
print("lista_cidades_2: ", lista_cidades_2, end=" ")
print("\nAlterando a lista 2")
lista_cidades_2.append("Mococa")
print("lista_cidades_1: ", lista_cidades_1, end=" ")
print()
print("lista_cidades_2: ", lista_cidades_2, end=" ")

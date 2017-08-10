#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tuplas e Dicionários: Notas de Estudo.

Tuplas são estruturas parecidas com listas, porém não podem ser 
alteradas.

Dicionários em python são uma estrutura de dados capaz de armazenar um
valor associado a uma chave.

"""

"""Tuplas

Primeiros passos

"""

tupla = (1, [1, 2, 3], {"chave": "valor"}, (0, 1), lambda x: x + 1, 3.1)

[print(item) for item in tupla]


"""Iniciando em dicionários.

Nesse exemplo foi criado um dicionário que armazena contatos telefônicos
Sendo que a chave representa o nome do contato e o valor o número.

"""
contatos = {"Joao": "991456325", "Pedro": "992854136",
            "Maria": "998756325", "Jose": "985631254",
            "Paula": "941253641"}

print(contatos)


"""Manipulando dicionários

- Acessando valores

Para acessar um valor em um dict é necessário informar a chave.
"""
print("Valor da chave João:", contatos["Joao"])


"""Existem também o método get que permite recuperar o valor associado a
uma chave.

Esse método pode receber dois argumentos, sendo que o segundo será
retornado caso a chace não seja encontrada.

"""

print("Recuperando com get, contatos.get('Pedro'):", contatos.get("Pedro"))
print(
    "\t...contatos.get('Epaminondas'):", contatos.get("Epaminondas",
    "Não localizado"))


"""
- Adicionando novos pares

Duas formas para inserir valores no dicionário:

- dict[index] = valor
- dict.update(dict)
"""

contatos["Luciano"] = "996324152"

print("Imprimindo contatos:")

for nome, numero in contatos.items():
    print("Nome: %s, Número: %s" % (nome, numero))


"""
- Iniciando um dict vazio

Um dict pode ser declarado de maneiras distintas:
"""

dicionario = dict()

print(type(dicionario))

dicionario = {}

print(type(dicionario))


"""
- Modificando valores no dicionário


O valor da chave em um dicionario é imutável, porém é possível 
substituir um par dentro de um dict.

"""

print("Contato do Luciano:", contatos["Luciano"])

contatos.update({"Luciano": "936463611"})

print("Contato do Luciano:", contatos["Luciano"])

contatos["Luciano"] = "889643641"

print("Contato do Luciano:", contatos["Luciano"])


"""
- Removendo pares

"""
contatos.pop("Luciano")

print("Contato do Luciano:", contatos.get("Luciano", "Não localizado.")) 

del contatos['Paula']

print("Contato da Paula:", contatos.get("Paula", "Não localizado.")) 


"""
- Percorrendo todos os elementos

Assim como em lista, o for pode ser utilizado para percorer dicts.

"""
print(contatos)

for nome, numeros in contatos.items():
    print(nome, "\t", numero)


[print("\tNome: %s, \tNumero: %s" % 
    (nome, numero)) for nome, numero in contatos.items()]


"""
- Percorrendo somente as chaves

"""
[print("Nome: %s" % nome) for nome in contatos.keys()]


"""
- Percorrendo somente os valores
"""
[print("Números: %s" % numero) for numero in contatos.values()]


"""
- Exemplos finais

Outros tipos de dicts.

"""

print({(1,1):[1, 2, 3, 4], 1: "Um", lambda x: x + 1: {"Nome": 1}})

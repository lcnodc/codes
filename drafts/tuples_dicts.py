# -*- coding: utf-8 -*-

"""3.Tuples e dictionary.


Tuples
Dictionary
Recuperando e alterando valores
"""

# Manipulando tuplas.
tupla = (1,2)

for i in tupla:
    print(i, end=" ")

'''
Acesso aos indices das tuplas é semelhante às listas, porém a tupla não permite
alterar o valor contido em seus índices.

tupla(0) = 2 NÃO PERMITIDO.

'''

print('\n\n')

# Dicionários em Python
# Person: using a dict to store information about a person.
# Creating a empty dict 
person = {}
person['first_name'] = 'josé'
person['last_name'] = 'santos'
person['age'] = 30
person['city'] = 'rio de janeiro'

for chave, valor in person.items():
    print(chave, valor)

print('\n')

# Store people's favorite numbers.
favorite_numers = {}
favorite_numers['jose'] = '1234-5678'
favorite_numers['joao'] = '9876-5432'
favorite_numers['antonio'] = '5432-5678'
favorite_numers['carlos'] = '1928-7364'

for chave, valor in favorite_numers.items():
    print(chave, valor)

print('\npython glossary\n'.title())

# Glossary of programming words.
glossary = {}
glossary['tuple'] = 'is a sequence of immutable Python objects. Tuples are \
sequences, just like lists'
glossary['list'] = 'are very similar to arrays. They can contain any type of \
variable, and they can contain as many variables as you wish'
glossary['variable'] = 'a something wich can change, a way of refering to a \
memory location used by a computer program'
glossary['dictionary'] = 'a data type similar to arrays, but works with keys \
and values instead of indexes'
glossary['function'] = 'a structuring element in programming languages to group\
 a set of statements so they can be utilized more than once in a program'

for chave, valor in glossary.items():
    print(chave.title() + '\n\t' + valor + '.')

print('\nglossary keys'.title())

for chaves in glossary.keys():
    print(chaves.title())

print('\nglossary values'.title())

for valores in glossary.values():
    print(valores)

print('\n\n')

novos_favoritos = ['manoel', 'jose', 'joaquim', 'pedro', 'joao',]

atuais_favoritos = favorite_numers.keys()

print("novos_favoritos: " ,novos_favoritos)
print("atuais_favoritos: " ,atuais_favoritos)

print('')

lista_convidar = []
lista_agradecer = []

for novo in novos_favoritos:
    if novo in atuais_favoritos:
        lista_agradecer.append(novo)
    else:
        lista_convidar.append(novo)

print("Agradecer: ", lista_agradecer)
print("Convidar: ", lista_convidar)

print("")


# Nesting
# Storing a set of dicts in a dicts
musics = {}
musics['three_little_birds'] = {
    'title' : 'three little birds',
    'singer' : 'bob marley',
    'duration' : '2:59',
}
musics['the_hardest_party'] = {
    'title' : 'the hardest party',
    'singer' : 'cold play',
    'duration' : '4:29',
}
musics['train_of_throught'] = {
    'title' : 'train of throught',
    'singer' : 'a-ha',
    'duration' : '4:15',
}

# Other form to declare a dict.
musics = {
    'three_little_birds' : {
        'title' : 'three little birds',
        'singer' : 'bob marley',
        'duration' : '2:59',
    },
    'the_hardest_party' : {
        'title' : 'the hardest party',
        'singer' : 'cold play',
        'duration' : '4:29',
    },
    'train_of_throught' : {
        'title' : 'train of throught',
        'singer' : 'a-ha',
        'duration' : '4:15',
    },
}

for musica, infos in musics.items():
    print("Id: " + musica)
    print("\tTítulo: " + infos['title'])
    print("\tCantor: " + infos['singer'])
    print("\tDuração: " + infos['duration'])


print('\n\n')

pets = []

pet = { 
    'nome' : 'bob',
    'tipo': 'cachorro', 
    'proprietario': 'john',
    }

pets.append(pet)

pet = {
    'nome' : 'garfield',
    'tipo':'gato',
    'proprietario': 'mike',
    }

pets.append(pet)

pet = {
    'nome' : 'vanda',
    'tipo': 'peixe',
    'proprietario': 'tina',
    }

pets.append(pet)

for pet in pets:
    print("Tudo sobre o/a pet chamado(a): " + pet['nome'])
    for caracteristica, valor in pet.items():
        print('\t' + caracteristica.title() + ": " + valor.title())
    
    print()

print('\n\n')

# Favorite places
favorite_places = {
    'john' : ['new york', 'san francisco', 'london',],
    'bob' : ['são paulo', 'rio de janeiro', 'curitiba',],
    'mike' : ['santiago' , 'barcelona', 'ontario',],
    }

for person, places in favorite_places.items():
    print('Os lugares favoritos de ' + person.title() + ' são: ')
    for place in places:
        print(place.title(), end= ", ")
    print('\n')   

print('\n\n')

# Favorite numbers
# Favorite places
favorite_numbers = {
    'john' : [23, 34, 53,],
    'bob' : [12, 66,88,],
    'mike' : [54, 11, 7,],
    }

for person, numbers in favorite_numbers.items():
    print('Os números favoritos de ' + person.title() + ' são: ')
    for number in numbers:
        print(number, end= ", ")
    print('\n')   

cities = {
    'new york': {
        'country': 'united states',
        'population': '19.796.000',
        'governor':'andrew cuomo',
        }, 
    'vancouver': {
        'country': 'canada',
        'population': '631.486',
        'governor': 'gregor robertson',
        },
    'london' : {
        'country': 'united kingdom',
        'population': '8.674.000',
        'governor': 'sadiq khan',
        },
    }

for citie, attributes in cities.items():
    print(citie.title())
    for key, value in attributes.items():
        print('\t' + key.title() + ': ' + value.title())
    print()

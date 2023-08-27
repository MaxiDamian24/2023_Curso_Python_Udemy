lista =[12, 4, 7]
lista_animal = ['perro', 'gato', 'elefante', 'lobo', 'yarara']

lista.sort()
lista_animal.sort()
print(lista)
print(lista_animal)
lista.reverse()
lista_animal.reverse()



print(lista)
print(lista_animal)
print(lista_animal[2])
print(sum(lista))
print(max(lista))
print(min(lista))
print(max(lista_animal))
print(min(lista_animal))
nueva_lista_animales = lista_animal * 3
print(nueva_lista_animales)
print(len(nueva_lista_animales))
tot = 0
for x in lista:
    tot  += 1

print('Total de numeros en la lista es: {}'.format(tot))

if 'lobo' in lista_animal:
    print('Existe un lobo en la lista')
else:
    print('no existe un lobo en la lista')
    lista_animal.append('lobo')
    print(lista_animal)

lista_animal.pop(1)
print(lista_animal)

lista_animal.remove('elefante')
print(lista_animal)

tupla = (3, 5, 1, 67)
print(tupla)
print(tupla[2])
print(len(tupla))
tupla_animal = tuple(lista_animal)
print(tupla_animal)
lista_numerica = list(tupla)
print (lista_numerica)
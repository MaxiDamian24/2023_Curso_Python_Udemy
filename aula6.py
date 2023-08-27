# conjunto = {1, 2, 3, 4, 4, 2}
# print(type(conjunto))
# print(conjunto)
# conjunto.add(5)
# print(conjunto)
# conjunto.discard(2)
# print(conjunto)

conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}
conjunto_union = conjunto.union(conjunto2)
print('Union: {}' .format(conjunto_union))
conjunto_interseccion = conjunto.intersection(conjunto2)
print('Interseccion:  {} '.format(conjunto_interseccion))
conjunto_diferencia1 = conjunto.difference(conjunto2)
print('Diferencia Conjunto: {}'.format(conjunto_diferencia1))
conjunto_diferencia2 = conjunto2.difference(conjunto)
print('Diferencias Conjunto2: {}' .format(conjunto_diferencia2))
conjunto_dif_simetrica = conjunto.symmetric_difference(conjunto2)
print(conjunto_dif_simetrica)

conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
conjunto_a_incluido = conjunto_a.issubset(conjunto_b)
print('El conjunto_a esta incluido en el conjunto_b? {}'.format(conjunto_a_incluido))
conjunto_b_incluido = conjunto_b.issubset(conjunto_a)
print('El conjunto_b esta incluido en el conjunto_a? {}'.format(conjunto_b_incluido))
conjunto_superconjunto = conjunto_b.issuperset(conjunto_a)
print('El conjunto_superconjunto incluye al conjunto_a? {}'.format(conjunto_superconjunto))

lista = ['perro', 'perro', 'gato', 'gato', 'elefante']
print(lista)
conjunto_animales = set(lista)
print(conjunto_animales)
lista_animales = list(conjunto_animales)
print(lista_animales)
# El mayor de tres numeros
# a = int(input('Ingrese el primer valor: '))
# b = int(input('Ingrese el segundo valor: '))
# c = int(input('Ingrese el tercer valor: '))
#
# if a > b and a > c:
#     print('El mayor valor es: {}' .format(a))
# elif b > c and b > a:
#     print('El mayor valor es: {} '.format(b))
# else:
#     print('El mayor numero es: {}'.format(c))
# print('Fin del programa')

# Saber si un numero es par o impar
# a = int(input('Ingrese el primer numero: '))
# b = int(input('Ingrese el segundo numero: '))
# resto_a = a % 2
# resto_b = b % 2
# if resto_a == 0 or resto_b == 0:
#     print('Por lo menos un numero es par.')
# else:
#     print('Ningun numero es par. ')
#
# if resto_a == 0:
#     print('El numero {} es par' .format(a))
# else:
#     print('El numero {} es impar'.format(a))
# if resto_b == 0:
#     print('El numero {} es par' .format(b))
# else:
#     print('El numero {} es  impar'.format(a))

# Promedio de notas verifico que los valores sean menores o igual a 10
a = int(input('Ingrese nota primer trimestre: '))
if a > 10:
    a = int(input('El valor debe ser 10 o menor, vuelva a ingresarlo: '))
b = int(input('Ingrese nota segundo trimestre: '))
if b > 10:
    b = int(input('El valor debe ser 10 o menor, vuelva a ingresarlo: '))
c = int(input('Ingrese nota tercer trimestre: '))
if c > 10:
    c = int(input('El valor debe ser 10 o menor, vuelva a ingresarlo: '))
d = int(input('Ingrese nota cuarto trimestre: '))
if d > 10:
    d = int(input('El valor debe ser 10 o menor, vuelva a ingresarlo: '))
promedio = (a + b + c + d) / 4
print('El promedio es: {}'.format(promedio))

# if a <= 10 and b <= 10 and c <= 10 and c <= 10:
#     promedio = (a + b + c + d) / 4
#     print('El promedio es: {}'.format(promedio))
# else:
#     print('Escribio un valor incorrecto')
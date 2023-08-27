# # Ingreso un número y me fijo si es primo
# a = int(input('Ingrese un número: '))
# div = 0
# for x in range(1, a+1):
#     resto = a % x
#     if resto == 0:
#        div += 1
#
# if div == 2 :
#     print('El número {} es primo'.format(a))
# else:
#     print('El número {} no es primo'.format(a))
# Ingreso un número y me fijo si es primo

# Los primeros 100 numeros, cuales son primos
# for num in range(101):
#     div = 0
#     for x in range(1, num + 1):
#         resto = num % x
#         if resto == 0:
#             div += 1
#
#     if div == 2 or num == 1:
#         print('El número {} es primo'.format(num))
#     else:
#         print('El número {} no es primo'.format(num))

# a = 0
# while a <= 10:
#     print(a)
#     a += 1

# nota = int(input('Ingrese una nota entre 0 y 10:'))
# while nota > 10 or nota < 0:
#     nota = int(input('Ingrese una nota entre 0 y 10:'))
# print(nota)

a = int(input('Ingrese nota primer trimestre: '))
while a > 10:
    a = int(input('El valor debe ser 10 o menor, vuelva a ingresarlo: '))
b = int(input('Ingrese nota segundo trimestre: '))
while b > 10:
    b = int(input('El valor debe ser 10 o menor, vuelva a ingresarlo: '))
c = int(input('Ingrese nota tercer trimestre: '))
while c > 10:
    c = int(input('El valor debe ser 10 o menor, vuelva a ingresarlo: '))
d = int(input('Ingrese nota cuarto trimestre: '))
while d > 10:
    d = int(input('El valor debe ser 10 o menor, vuelva a ingresarlo: '))
promedio = (a + b + c + d) / 4
print('El promedio es: {}'.format(promedio))

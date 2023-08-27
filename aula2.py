a = int(input('Ingrese un numero: '))
b = int(input('Ingrese otro numero: '))
suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b
resto = a % b
#print('suma es una variable: ')
#print(type(suma))
# Convierto la variable suma de Entero a String
#suma = str(suma)
#print(type(suma))
resultado = ('suma: {sum} '
      '\nresta: {res} '
      '\nmultiplicacion: {multi} '
      '\ndivision: {di} '
      '\nresto: {rest}'
      .format(sum=suma, res=resta, multi=multiplicacion, di=division, rest=resto))
print(resultado)
print('suma: ' + str(suma))
#print(suma)
print(resta)
print(multiplicacion)
# Imprimo la variable division de float a entero
print(int(division))
# Imprimo la variable division como float
print(division)
print(resto)
x = '1'
suma2 = int(x) + 1
print(suma2)
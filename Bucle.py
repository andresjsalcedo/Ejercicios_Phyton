#Sentencia WHILE

'''want_greet = 'S'  #importante dar un valor inicial

while want_greet == 'S':
    print('Hola qué tal!')
    want_greet = input('¿Quiere otro saludo? [S/N] ')
print('Que tenga un buen día')'''

#Hola qué tal!
#¿Quiere otro saludo? [S/N] S
#Hola qué tal!
#¿Quiere otro saludo? [S/N] S
#Hola qué tal!
#¿Quiere otro saludo? [S/N] N
#Que tenga un buen día



#Romper un bucle while

MAX_GREETS = 4

num_greets = 0
want_greet = 'S'

while want_greet == 'S':
    print('Hola qué tal!')
    num_greets += 1
    if num_greets == MAX_GREETS:
        print('Máximo número de saludos alcanzado')
        break
    want_greet = input('¿Quiere otro saludo? [S/N] ')
print('Que tenga un buen día')
#Condicionales simples
'''temperature = 30

if temperature > 35:
    print('Aviso por alta temperatura')
else:
        print('La temperatura está normal')'''



#Condicionales anidadas

'''temperature = 40

if temperature < 20:
    if temperature < 10:
        print('Nivel azul')
    else:
        print('Nivel verde')
else:
    if temperature < 30:
        print('Nivel naranja')
    else:
        print('Nivel rojo')'''


#Otra forma de utilizar el else-If

'''temperature = 28

if temperature < 20:
    if temperature < 10:
        print('Nivel azul')
    else:
        print('Nivel verde')
elif temperature < 30:
    print('Nivel naranja')
else:
    print('Nivel rojo')'''


#Asignacion de condicionales 

'''temperature = 30

if temperature < 30:
    fire_risk = 'LOW'
else:
    fire_risk = 'HIGH'''


#Asignacion de condicionales forma abreviada 

'''fire_risk = 'LOW' if temperature < 30 else 'HIGH'

fire_risk'''

#MatchCase Para version

'''color = '#FF0000'

match color:
    case '#FF0000':
        print('🔴')
    case '#00FF00':
        print('🟢')
    case '#0000FF':
        print('🔵')'''

#Operador morsa

'''radius = 4.25
perimeter = 2 * 3.14 * radius
if perimeter < 100:
    print('Increase radius to reach minimum perimeter')
    print('Actual perimeter: ', perimeter)'''



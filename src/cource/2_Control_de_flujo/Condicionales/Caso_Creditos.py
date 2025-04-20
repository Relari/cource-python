
edad = 18
antiguedad = 3
ingreso = 1000

if edad >= 18:

    if antiguedad >= 3 and ingreso >= 2500:
        print('Aprobado')
    elif ingreso >= 4000:
        print('Aprobado')
    else:
        print('No aprobado')

else:
    print('No aprobado')
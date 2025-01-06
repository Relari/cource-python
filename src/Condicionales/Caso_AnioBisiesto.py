
anio = 2135

if anio % 4 == 0:

    if anio % 100:

        if anio % 400:
            print('Bisiesto')
        else:
            print('No bisiesto')

    else:
        print('Bisiesto')

else:
    print('No bisiesto')
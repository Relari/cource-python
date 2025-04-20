anio = int(input('Ingrese anio: '))

if (anio >= 1920) and (anio <= 1940):
    generacion = 'Generacion Silenciosa'
elif (anio >= 1946) and (anio <= 1964):
    generacion = 'Baby Boomer'
elif (anio >= 1965) and (anio <= 1979):
    generacion = 'Generacion X'
elif (anio >= 1980) and (anio <= 2000):
    generacion = 'Milennials'
elif (anio >= 2001) and (anio <= 2010):
    generacion = 'Generacion Z'
else:
    generacion = 'No clasificado'

print(f"La generacion es {generacion}")

exit(0)
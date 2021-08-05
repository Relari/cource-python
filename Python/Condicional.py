edad = int(input("Ingrese edad: "))

if (edad > 18) and (edad < 60):
  print("Es mayor de edad")
elif edad > 59:
  print("Es adulto mayor")
else:
  print("Es menor de edad")
#ESCRIBE UN PROGRAMA QUE SOLICITE AL USUARIO UN NUMEREO QUE VERIFIQUE SI "NO" ES MAYOR QUE 50

# Solicita los números al usuario
num = float(input("Ingrese el primer número: "))

no_mayor_que_50 = not num > 50

#Mostrar el resultado
print(f"¿El número ({num}) no es mayor que 50? {no_mayor_que_50}")


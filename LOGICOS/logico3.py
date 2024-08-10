#NEGACION DE UN ACONDIION COMPUESTA


# Solicita un número al usuario
num = int(input("Ingrese un número: "))

# Verifica si el número es par
no_en_rango = not(10<= num <=20)

# Imprime si el número es par o no
print(f"¿El número ({num}) no está entre 10 y 20? {no_en_rango}")

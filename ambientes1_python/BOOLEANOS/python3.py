# VERIFICAR SI UN NÚMERO ESTÁ EN UN RANGO
# Solicita un número al usuario
num = float(input("Ingrese un número: "))

# Verifica si el número está en el rango de 10 a 20
en_rango = 10 <= num <= 20

# Imprime si el número está en el rango o no
print(f"El número ({num}) está entre 10 y 20? {en_rango}")
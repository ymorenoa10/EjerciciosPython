# PARIDAD DE UN NÚMERO
# Solicita un número al usuario
num = int(input("Ingrese un número: "))

# Verifica si el número es par
es_par = num % 2 == 0

# Imprime si el número es par o no
print(f"¿El número ({num}) es par? {es_par}")
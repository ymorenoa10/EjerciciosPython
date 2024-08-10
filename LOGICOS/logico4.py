#VERIFICAR SI UN NÚMERO ES MULTIPLO DE 3 Y NO DE 5


# Solicita un número al usuario
num = int(input("Ingrese un número: "))

# Verifica si el número es par
multiplo_de_3_no_de_5 = num % 3 == 0 and num % 5 !=0

# Imprime si el número es par o no
print(f"¿El número ({num}) es multiplo de 3 y no de 5? {multiplo_de_3_no_de_5}")

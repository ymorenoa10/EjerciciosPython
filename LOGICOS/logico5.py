#VERIFICAR SII UN NUMERO NO ES MULTIPLO DE 4 O ES POSITIVO


# Solicita un número al usuario
num = int(input("Ingrese un número: "))

# Verifica si el número es par
no_multiplo_de_4_o_positivo = num % 4 != 0 or num >0

# Imprime si el número es par o no
print(f"¿El número ({num}) no es multiplo de 4 o es positivo? {no_multiplo_de_4_o_positivo}")
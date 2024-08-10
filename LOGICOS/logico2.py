#VERIFICAR SI UN NUMERO ES POSITIVO Y PAR


# Solicita un número al usuario
num = int(input("Ingrese un número: "))

# Verifica si el número es par
es_negativo_o_impar = num <0 or num %2 != 0

# Imprime si el número es par o no
print(f"¿El número ({num}) es par? {es_negativo_o_impar}")
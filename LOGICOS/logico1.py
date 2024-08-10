#VERIFICAR SI UN NUMERO ES POSITIVO Y PAR


# Solicita un número al usuario
num = int(input("Ingrese un número: "))

# Verifica si el número es par
es_positivo_y_par = num >0 %2 == 0

# Imprime si el número es par o no
print(f"¿El número ({num}) es par? {es_positivo_y_par}")
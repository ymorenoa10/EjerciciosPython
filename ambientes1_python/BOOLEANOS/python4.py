# CREE UN PROGRAMA QUE SOLICITE LOS DOS NÚMEROS Y DETERMINE SI SON IGUALES
# Solicita los números al usuario
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

# Verifica si los números son iguales
son_iguales = num1 == num2

# Imprime si los números son iguales o no
print(f"¿Los números ({num1}) y ({num2}) son iguales? {son_iguales}")
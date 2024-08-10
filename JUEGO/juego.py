import random

def adivina_el_numero():
    numero_secreto = random.randint(1,100)
    intentos = 0

    print("Biwnvenido al juego de adivina al numero")
    print("estoy pensando en un numero entre 1 y 100")

    while True:
        try: 
            adivinansa = int(input("adivina el numero: "))
            intentos +=1

            if adivinansa < numero_secreto :
                print("demasiado bajo. intenta de nuevo")
            elif adivinansa> numero_secreto:
                print("demasiado alto. intenta de nuevo")
            else:
                print(f"felicidades adivinaste el numero en {intentos} intentos")

                break
        except ValueError:
            print("Por favor ingrese un numero valido")

if __name__ == "__main__":
    adivina_el_numero()
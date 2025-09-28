#Consiga 
#crear un juego de Adivinar palabra / estilo ahorcado/ 
#debe tener: 

#Mostrar con --- la cantidad de letras de la palabra a adivinar 
#Usar Python random
#Ver la cantida de vidas 
#Mostrar las letras incorrectas
#
#Cada letra debe validarse, si es correcta o no. 
#Game over / Winer
#Seguir jugando o salir del juego // No seguir es el fin del juego. 

import random

print("¡Hola, bienvenid@!\n¿Quieres adivinar la palabra secreta?" )

juego = input("si/no: ").lower()

if juego == "si":
    print("A jugar 👾✨ !!!") 
    print()
    print("Tienes 5 oportunidades de adivinar")
else:
    print("Está bien, en otro momento lo intentas 👋")

def seleccion_palabra():
    palabras = ["arepa", "ceviche", "asado", "empanada", "locro", "pisco", "feijoada", "humita"]
    return random.choice(palabras)

def guion_palabra(palabra, letras_correctas):
    return " ".join([letra if letra in letras_correctas else "_" for letra in palabra])

def adivinar():
    palabra_secreta = seleccion_palabra()
    letras_correctas = set()
    letras_incorrectas = set()
    intentos_vidas = 5 

    while intentos_vidas > 0:
        estado = guion_palabra(palabra_secreta, letras_correctas)
        print("\nPalabra:", estado)
        print("Intentos restantes:", intentos_vidas)
        print("Letras incorrectas:", " ".join(sorted(letras_incorrectas)) if letras_incorrectas else "Ninguna")

        letra = input("Introduce una letra: ").lower()

        if len(letra) != 1 or not letra.isalpha():
            print("Carácter no válido, por favor ingresa una sola letra.")
            continue
        if letra in letras_correctas or letra in letras_incorrectas:
            print("Ya utilizaste esta letra.")
            continue

        if letra in palabra_secreta:
            letras_correctas.add(letra)
            print("¡Correcto!")
        else:
            letras_incorrectas.add(letra)
            intentos_vidas -= 1
            print("Opps... intenta nuevamente.")

        # Si ya se adivinó toda la palabra
        if all(l in letras_correctas for l in palabra_secreta):
            print("\n🎉 ¡Adivinaste la palabra! Era:", palabra_secreta)
            break
    else:
        # Si se quedó sin intentos
        print("\n💀 Game Over. La palabra era:", palabra_secreta)

if _name_ == "_main_":
    if juego == "si":
        adivinar()
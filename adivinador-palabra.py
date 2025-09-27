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

juego = input("si/no): ").lower()

if juego == "si":
    print("A jugar 👾✨ !!!") 
    print()
    print("Tienen 5 oportunidades de adivinar")

else:
    print("Está bien, en otro momento lo intentas 👋")

def seleccion_palabra():
    palabra = ["arepa", "ceviche", "asado", "empanada", "locro", "pisco", "feijoada", "humita"]
    return random.choice (palabra) #aca va a elegir una palabra 

def guion_palabra(palabra, letra_correct):
    return " ".join([letras if letras in letra_correct else "_" for letras in palabra ])

def adivinar():
    palabras = seleccion_palabra 
    letra_corret = set()
    intentos_vidas = 5 
    
while True #Falta definir las coneccciones con IF y ELSE, tener en cuenta si usar un BREAK , 
  if isalpha()    # El método isalpha() devuelve True si todos los caracteres son alfabéticos, False de lo contrario
                  
                  # confirmar si la letra es correcta o no.
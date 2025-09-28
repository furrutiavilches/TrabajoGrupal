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
import flet as ft

# Lista de palabras
PALABRAS = ["asado", "empanada", "locro", "mate", "milanesa", "choripan", "humita", "provoleta"]

def seleccion_palabra():
    return random.choice(PALABRAS)

def guion_palabra(palabra, letras_correctas):
    return " ".join([letra if letra in letras_correctas else "_" for letra in palabra])

def main(page: ft.Page):
    page.title = "🍖 Parrilla Retro - Juego de Adivinar"
    page.bgcolor = "#1c1c1c"
    page.theme_mode = "dark"
    page.window_width = 500
    page.window_height = 600
    page.padding = 20

    fuente_retro = ft.TextStyle(
        size=20,
        weight=ft.FontWeight.BOLD,
        font_family="Courier New",
        color="#00FF00"
    )

    # Variables del juego
    palabra_secreta = seleccion_palabra()
    letras_correctas = set()
    letras_incorrectas = set()
    intentos_vidas = 5

    # Widgets dinámicos
    titulo = ft.Text("👾 Bienvenido al Restaurante Retro Argentino 👾", size=22, color="orange", weight="bold", text_align="center")
    palabra_texto = ft.Text(guion_palabra(palabra_secreta, letras_correctas), style=fuente_retro)
    intentos_texto = ft.Text(f"Intentos restantes: {intentos_vidas}", style=fuente_retro)
    incorrectas_texto = ft.Text("Letras incorrectas: Ninguna", style=fuente_retro)
    entrada_letra = ft.TextField(label="Introduce una letra", width=200, on_submit=lambda e: jugar(e.control.value))
    mensaje = ft.Text("", size=18, color="yellow")

    # Botones de reinicio o salida
    boton_continuar = ft.ElevatedButton("▶ Continuar", visible=False, on_click=lambda e: reiniciar())
    boton_salir = ft.ElevatedButton("❌ Salir", visible=False, on_click=lambda e: page.window_close())

    botones_final = ft.Row([boton_continuar, boton_salir], alignment="center")

    def mostrar_botones_final():
        boton_continuar.visible = True
        boton_salir.visible = True
        page.update()

    def ocultar_botones_final():
        boton_continuar.visible = False
        boton_salir.visible = False
        page.update()

    def reiniciar():
        nonlocal palabra_secreta, letras_correctas, letras_incorrectas, intentos_vidas
        # Reiniciar variables
        palabra_secreta = seleccion_palabra()
        letras_correctas = set()
        letras_incorrectas = set()
        intentos_vidas = 5

        # Reiniciar interfaz
        palabra_texto.value = guion_palabra(palabra_secreta, letras_correctas)
        intentos_texto.value = f"Intentos restantes: {intentos_vidas}"
        incorrectas_texto.value = "Letras incorrectas: Ninguna"
        entrada_letra.value = ""
        entrada_letra.disabled = False
        mensaje.value = ""
        ocultar_botones_final()
        page.update()

    def jugar(letra):
        nonlocal intentos_vidas

        letra = letra.lower().strip()
        entrada_letra.value = ""  # limpiar

        if len(letra) != 1 or not letra.isalpha():
            mensaje.value = "⚠ Ingresa una sola letra válida."
        elif letra in letras_correctas or letra in letras_incorrectas:
            mensaje.value = "⚠ Ya usaste esa letra."
        elif letra in palabra_secreta:
            letras_correctas.add(letra)
            mensaje.value = "✅ ¡Correcto!"
        else:
            letras_incorrectas.add(letra)
            intentos_vidas -= 1
            mensaje.value = "❌ Opps... intenta de nuevo."

        # Actualizar estado
        palabra_texto.value = guion_palabra(palabra_secreta, letras_correctas)
        intentos_texto.value = f"Intentos restantes: {intentos_vidas}"
        incorrectas_texto.value = f"Letras incorrectas: {' '.join(sorted(letras_incorrectas)) if letras_incorrectas else 'Ninguna'}"

        # Verificar fin de juego
        if all(l in letras_correctas for l in palabra_secreta):
            mensaje.value = f"🎉 ¡Ganaste! La palabra era {palabra_secreta.upper()}"
            entrada_letra.disabled = True
            mostrar_botones_final()
        elif intentos_vidas == 0:
            mensaje.value = f"💀 Game Over. La palabra era {palabra_secreta.upper()}"
            entrada_letra.disabled = True
            mostrar_botones_final()

        page.update()

    # Layout inicial
    page.add(
        titulo,
        palabra_texto,
        intentos_texto,
        incorrectas_texto,
        entrada_letra,
        mensaje,
        botones_final
    )

ft.app(target=main)
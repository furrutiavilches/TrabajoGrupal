🍖 Parrilla Retro - Juego de Adivinar Palabra
📌 Descripción

Este proyecto consiste en un juego interactivo estilo ahorcado, donde el jugador debe adivinar una palabra secreta relacionada con la gastronomía argentina.

El programa fue desarrollado en Python utilizando la librería Flet
 para la interfaz gráfica.

🎮 Funcionamiento

El juego selecciona aleatoriamente una palabra secreta.

Se muestra al jugador la cantidad de letras usando guiones (_).

El jugador cuenta con 5 vidas.

Cada vez que se ingresa una letra:

✅ Si es correcta, se muestra en la palabra.

❌ Si es incorrecta, se resta una vida y la letra se guarda en la lista de intentos fallidos.

El juego termina cuando:

Se adivina la palabra (Ganador 🎉)

Se quedan sin vidas (Game Over 💀)

El jugador decide salir.

⚙️ Requisitos

Python 3.10 o superior

Librerías necesarias (instalar desde requirements.txt):

pip install -r requirements.txt

📂 Estructura del repositorio
📁 -trabajo-grupal.py
 ┣ 📄 trabajo-grupal.py      # Código principal del juego
 ┣ 📄 requirements.txt       # Dependencias del proyecto
 ┣ 📄 README.md              # Documentación del proyecto
 ┗ 📄 integrantes.txt        # Lista de integrantes del grupo

🌱 Flujo de trabajo con Git

Para este proyecto seguimos la metodología Git Flow con las siguientes ramas:

main → contiene la versión final y estable del proyecto (sin código de prueba).

develop → rama de integración, donde unimos y probamos los aportes del grupo.

feature/[nombre] → ramas individuales de cada integrante para trabajar de forma separada.

🔀 Proceso de trabajo

Cada integrante creó su propia rama feature/nombre.

Se desarrolló y probó el código en las ramas individuales.

Se hizo merge de las feature a la rama develop.

Finalmente, develop se integró en main para la entrega final.

📥 Instalación y ejecución

Clonar el repositorio:

git clone https://github.com/vediasofia6-sudo/-trabajo-grupal.py.git
cd -trabajo-grupal.py


Instalar dependencias:

pip install -r requirements.txt


Ejecutar el programa:

python trabajo-grupal.py

🕹️ Cómo jugar

Ingresa una letra en el campo de texto.

Revisa si fue correcta o incorrecta.

Intenta adivinar la palabra antes de quedarte sin vidas.

Al finalizar, elige si quieres continuar o salir del juego.

👩‍💻 Integrantes

Sofía Vedia

Macarena Santamaría

Francisca Urrutia
# 🍖 Parrilla Retro - Juego de Adivinar Palabra

## 📌 Descripción

Este proyecto consiste en un juego interactivo estilo ahorcado, donde el jugador debe adivinar una palabra secreta relacionada con la gastronomía argentina.

El programa fue desarrollado en Python utilizando la librería Flet para la interfaz gráfica.

## 🎮 Funcionamiento

- El juego selecciona aleatoriamente una palabra secreta.
- Se muestra al jugador la cantidad de letras usando guiones (_).
- El jugador cuenta con 5 vidas.
- Cada vez que se ingresa una letra:
  - ✅ Si es correcta, se muestra en la palabra.
  - ❌ Si es incorrecta, se resta una vida y la letra se guarda en la lista de intentos fallidos.
- El juego termina cuando:
  - Se adivina la palabra (Ganador 🎉)
  - Se quedan sin vidas (Game Over 💀)
  - El jugador decide salir.

## ⚙️ Requisitos

- Python 3.10 o superior
- Librerías necesarias (instalar desde requirements.txt):

```bash
pip install -r requirements.txt
```

## 📂 Estructura del repositorio

📁 -trabajo-grupal.py  
 ┣ 📄 trabajo-grupal.py      # Código principal del juego  
 ┣ 📄 requirements.txt       # Dependencias del proyecto  
 ┣ 📄 README.md              # Documentación del proyecto  
 ┗ 📄 integrantes.txt        # Lista de integrantes del grupo  

## 🌱 Flujo de trabajo con Git

Para este proyecto seguimos la metodología **Git Flow** con las siguientes ramas:

- **main** → contiene la versión final y estable del proyecto (sin código de prueba).
- **develop** → rama de integración, donde unimos y probamos los aportes del grupo.
- **feature/[nombre]** → ramas individuales de cada integrante para trabajar de forma separada.

### 🔀 Proceso de trabajo

1. Cada integrante creó su propia rama `feature/nombre`.
2. Se desarrolló y probó el código en las ramas individuales.
3. Se hizo merge de las `feature` a la rama `develop`.
4. Finalmente, `develop` se integró en `main` para la entrega final.

## 📥 Instalación y ejecución

1. Clonar el repositorio:
```bash
git clone https://github.com/furrutiavilches/TrabajoGrupal.git
cd TrabajoGrupal
```

2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

3. Ejecutar el programa:
```bash
python trabajo-grupal.py

```

## 🕹️ Cómo jugar

1. Ingresa una letra en el campo de texto.
2. Revisa si fue correcta o incorrecta.
3. Intenta adivinar la palabra antes de quedarte sin vidas.
4. Al finalizar, elige si quieres continuar o salir del juego.

## 👩‍💻 Integrantes

- Sofía Vedia  
- Macarena Santamaría  
- Francisca Urrutia  

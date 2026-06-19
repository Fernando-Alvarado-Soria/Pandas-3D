# Pandas-3D

Proyecto de práctica con la librería **Panda3D** para desarrollo de aplicaciones 3D interactivas en Python.

## Requisitos Previos

⚠️ **Importante:** Esta librería requiere una versión específica de Python para funcionar correctamente sin errores.

### 1. Instalar Python 3.10.10

La librería Panda3D 1.10.16 es compatible con **Python 3.10.10**. Se recomienda usar esta versión para evitar problemas de compatibilidad.

- Descarga Python 3.10.10 desde: [python.org](https://www.python.org/downloads/release/python-31010/)
- Durante la instalación, **marca la opción "Add Python to PATH"**

Verifica la instalación:
```bash
python --version
```

## Instalación

### 2. Clonar el Repositorio

```bash
git clone https://github.com/Fernando-Alvarado-Soria/Pandas-3D.git
cd Pandas-3D
```

### 3. Crear un Entorno Virtual

Crea un entorno virtual con Python 3.10.10:

**En Windows (PowerShell):**
```powershell
python -m venv pandas3d_env
.\pandas3d_env\Scripts\Activate.ps1
```

**En Windows (CMD):**
```cmd
python -m venv pandas3d_env
pandas3d_env\Scripts\activate.bat
```

**En macOS/Linux:**
```bash
python -m venv pandas3d_env
source pandas3d_env/bin/activate
```

### 4. Instalar Dependencias

Una vez activado el entorno virtual:

```bash
pip install -r requirements.txt
```

Esto instalará:
- **Panda3D 1.10.16** - Motor 3D para Python

## Uso

Para ejecutar los ejemplos disponibles:

```bash
python ejemplo1.py
python ejemplo2.py
python main.py
```

## Estructura del Proyecto

```
Pandas-3D/
├── ejemplo1.py          # Ejemplo 1 de uso de Panda3D
├── ejemplo2.py          # Ejemplo 2 de uso de Panda3D
├── main.py              # Script principal
├── requirements.txt     # Dependencias del proyecto
├── .gitignore          # Archivos ignorados por Git
└── pandas3d_env/       # Entorno virtual (ignorado en Git)
```

## Notas de Compatibilidad

- ⚠️ Python 3.10.10 es la versión recomendada para esta versión de Panda3D
- Se han omitido los archivos del entorno virtual del repositorio para mantener un tamaño reducido
- Cada desarrollador debe crear su propio entorno virtual siguiendo estos pasos

## Licencia

Este es un proyecto de práctica y aprendizaje.

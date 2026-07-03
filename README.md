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
- **panda3d-gltf 1.3.0** - Soporte para cargar modelos `.gltf` y `.glb`

> **Nota para entornos restringidos:** Si no puedes crear un entorno virtual ni usar `pip` (por ejemplo, en sistemas Linux donde Python está "externally managed"), puedes instalar las dependencias localmente en la carpeta del proyecto:
> ```bash
> curl -sS https://bootstrap.pypa.io/get-pip.py -o get-pip.py
> python3 get-pip.py --user
> ~/.local/bin/pip install -r requirements.txt --target .local_packages
> export PYTHONPATH="$(pwd)/.local_packages:$PYTHONPATH"
> ```
> Luego ejecuta los scripts anteponiendo `PYTHONPATH=./.local_packages` al comando.

## Uso

### Ejecutar ejemplos básicos

```bash
python ejemplo1.py
python main.py
```

### Visor de modelos 3D (`visor_modelos.py`)

Este script carga y visualiza modelos `.glb` desde el catálogo de `assets/`.

```bash
python visor_modelos.py
```

Por defecto intenta cargar `assets/personajes/01_robot.glb`. Si recibes un error de `JSONDecodeError` o "Couldn't load file", significa que el archivo `.glb` está vacío o corrupto. Los archivos `.glb` incluidos en este repositorio son **placeholders** (todos contienen un modelo de prueba idéntico). Debes reemplazarlos con tus modelos 3D reales manteniendo los nombres de archivo.

## Estructura del Proyecto

```
Pandas-3D/
├── assets/                 # Catálogo de modelos 3D (.glb)
│   ├── personajes/         # 01_robot.glb ... 10_aventurero.glb
│   ├── vehiculos/          # 11_auto.glb ... 20_tren.glb
│   ├── naturaleza/         # 21_arbol.glb ... 30_lago.glb
│   ├── edificios/          # 31_casa.glb ... 40_iglesia.glb
│   ├── objetos/            # 41_mesa.glb ... 50_moneda.glb
│   ├── comida/             # 51_manzana.glb ... 60_taco.glb
│   ├── ciudad/             # 61_semaforo.glb ... 70_fuente.glb
│   ├── fantasia/           # 71_dragon.glb ... 80_tesoro.glb
│   ├── minecraft/          # 81_bloque_pasto.glb ... 90_bloque_oro.glb
│   └── escenarios/         # 91_isla.glb ... 100_base_espacial.glb
├── visor_modelos.py      # Visor de modelos GLB con Panda3D
├── ejemplo1.py           # Ejemplo 1 de uso de Panda3D
├── main.py               # Script principal
├── bloque.py             # Ejemplo de bloque 3D
├── galeria.py            # Ejemplo de galería de modelos
├── requirements.txt      # Dependencias del proyecto
├── .gitignore            # Archivos ignorados por Git
└── pandas3d_env/         # Entorno virtual (ignorado en Git)
```

## Notas sobre los Modelos

- Los archivos `.glb` dentro de `assets/` son **placeholders** (modelos de relleno).
- Para usar modelos reales, exporta tus diseños desde Blender (u otra herramienta) en formato **glTF 2.0 Binary (.glb)** y reemplaza los archivos correspondientes respetando los nombres.
- El visor utiliza `panda3d-gltf` para registrar automáticamente el cargador de archivos `.glb` dentro de Panda3D.

## Notas de Compatibilidad

- ⚠️ Python 3.10.10 es la versión recomendada para esta versión de Panda3D
- Se han omitido los archivos del entorno virtual del repositorio para mantener un tamaño reducido
- Cada desarrollador debe crear su propio entorno virtual siguiendo estos pasos
- **Linux sin entorno virtual:** Si usas `--target .local_packages`, asegúrate de definir `PYTHONPATH` antes de ejecutar los scripts.

## Licencia

Este es un proyecto de práctica y aprendizaje.

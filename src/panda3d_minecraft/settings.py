from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]

ASSETS_DIR = PROJECT_ROOT / "assets"
MAPS_DIR = ASSETS_DIR / "maps"
MODELS_DIR = ASSETS_DIR / "models"
TEXTURES_DIR = ASSETS_DIR / "textures"
SOUNDS_DIR = ASSETS_DIR / "sounds"

DEFAULT_MAP = MAPS_DIR / "level_01.txt"

WINDOW_TITLE = "Mini Minecraft con Panda3D"
BACKGROUND_COLOR = (0.45, 0.75, 1.0)
CAMERA_FOV = 80

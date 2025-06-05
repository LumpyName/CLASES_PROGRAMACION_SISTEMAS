# lib/cargar_fuentes.py

import os
import ctypes
from ctypes import wintypes

# Solo funciona en Windows
if os.name != "nt":
    raise OSError("Este script solo funciona en Windows.")

def cargar_fuentes_temporales(directorio_fuentes):
    """Carga todas las fuentes .ttf del directorio especificado de forma temporal (solo en memoria)."""
    
    # Cargar función de Windows
    AddFontResourceEx = ctypes.windll.gdi32.AddFontResourceExW
    AddFontResourceEx.argtypes = [wintypes.LPCWSTR, wintypes.DWORD, wintypes.PVOID]
    AddFontResourceEx.restype = wintypes.INT

    # Constante: FR_PRIVATE = 0x10
    FR_PRIVATE = 0x10

    fuentes_cargadas = []

    for archivo in os.listdir(directorio_fuentes):
        if archivo.lower().endswith(".ttf"):
            ruta_absoluta = os.path.abspath(os.path.join(directorio_fuentes, archivo))
            resultado = AddFontResourceEx(ruta_absoluta, FR_PRIVATE, None)
            if resultado > 0:
                fuentes_cargadas.append(ruta_absoluta)

    return fuentes_cargadas

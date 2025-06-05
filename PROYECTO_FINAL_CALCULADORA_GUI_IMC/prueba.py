import tkinter as tk
import tkinter.font as tkFont
from lib.cargar_fuente import cargar_fuentes_temporales

# Cargar fuentes desde la carpeta
cargar_fuentes_temporales("fuentes_ttf")

root = tk.Tk()
root.title("Demo fuentes TTF")

# Fuente regular (bold)
fuente_bold = tkFont.Font(family="Victor Mono", size=16, weight="bold")

# Fuente oblicua (italic)
fuente_oblique = tkFont.Font(family="Victor Mono Oblique", size=16)

# Ejemplo con fuente bold
label1 = tk.Label(root, text="Texto en Victor Mono Bold", font=fuente_bold)
label1.pack(pady=10)

# Ejemplo con oblique
label2 = tk.Label(root, text="Texto en Victor Mono Oblique", font=fuente_oblique)
label2.pack(pady=10)

root.mainloop()

import tkinter as tk

# Crear la ventana principal
root = tk.Tk()
root.title("Selección Exclusiva")
root.geometry("300x200")

# Crear un Frame para agrupar los elementos
frame = tk.Frame(root, padx=10, pady=10)
frame.pack(padx=20, pady=20)

# Variable para los Radiobuttons
selection_var = tk.StringVar()

# Configuración de los tres Radiobuttons
radio_button1 = tk.Radiobutton(frame, text="Opción 1", variable=selection_var, value="Opción 1")
radio_button1.grid(row=0, column=0, padx=5, pady=5, sticky="w")

radio_button2 = tk.Radiobutton(frame, text="Opción 2", variable=selection_var, value="Opción 2")
radio_button2.grid(row=1, column=0, padx=5, pady=5, sticky="w")

radio_button3 = tk.Radiobutton(frame, text="Opción 3", variable=selection_var, value="Opción 3")
radio_button3.grid(row=2, column=0, padx=5, pady=5, sticky="w")

# Para asegurar que se inicializa con un valor, lo configuramos
selection_var.set("Opción 1")

# Función para mostrar la selección
def mostrar_seleccion():
    seleccion = selection_var.get()
    print(f"Selección actual: {seleccion}")

# Botón para mostrar la selección
button = tk.Button(frame, text="Mostrar Selección", command=mostrar_seleccion)
button.grid(row=3, column=0, pady=10)

# Ejecutar la ventana
root.mainloop()

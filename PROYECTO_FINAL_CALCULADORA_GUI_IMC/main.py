import tkinter as tk

# Crear la ventana principal
root = tk.Tk()
root.title("Formulario Básico")
root.geometry("400x500")  # Tamaño de la ventana

# Crear un Frame para agrupar los elementos
frame = tk.Frame(root, padx=10, pady=10)
frame.pack(padx=20, pady=20)

# Variables para los Checkbuttons
adultos_var = tk.BooleanVar()
ninas_var = tk.BooleanVar()
ninos_var = tk.BooleanVar()

# Label y Checkbutton para "Adultos"
adultos_label = tk.Label(frame, text="Adultos")
adultos_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
adultos_check = tk.Checkbutton(frame, variable=adultos_var)
adultos_check.grid(row=0, column=1, padx=5, pady=5)

# Label y Checkbutton para "Niñas"
ninas_label = tk.Label(frame, text="Niñas")
ninas_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
ninas_check = tk.Checkbutton(frame, variable=ninas_var)
ninas_check.grid(row=1, column=1, padx=5, pady=5)

# Label y Checkbutton para "Niños"
ninos_label = tk.Label(frame, text="Niños")
ninos_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
ninos_check = tk.Checkbutton(frame, variable=ninos_var)
ninos_check.grid(row=2, column=1, padx=5, pady=5)

# Línea de separación (canvas)
separator = tk.Canvas(frame, height=2, width=300)
separator.grid(row=3, column=0, columnspan=2, pady=10)
separator.create_line(0, 1, 300, 1, fill="gray")

# Label y cuadro de entrada para "PESO"
peso_label = tk.Label(frame, text="PESO")
peso_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
peso_entry = tk.Entry(frame)
peso_entry.grid(row=4, column=1, padx=5, pady=5)

# Label para "Altura (en metros)"
altura_label = tk.Label(frame, text="Altura (en metros)")
altura_label.grid(row=5, column=0, padx=5, pady=5, sticky="w")

# Área de texto para la entrada de altura (usamos un widget Text)
altura_text = tk.Text(frame, height=1, width=20)
altura_text.grid(row=5, column=1, padx=5, pady=5)

# Label para "IMC:"
imc_label = tk.Label(frame, text="IMC:")
imc_label.grid(row=6, column=0, padx=5, pady=5, sticky="w")

# Cuadro de texto grande con un label centrado dentro
imc_box = tk.Label(frame, text="IMC Calculado", relief="solid", width=20, height=3)
imc_box.grid(row=7, column=0, columnspan=2, pady=15, padx=5)
imc_box.config(justify="center")

# Ejecutar la ventana
root.mainloop()

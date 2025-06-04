import tkinter as tk

import lib.recurso_gui as gui_user

# Crear la ventana principal
root = tk.Tk()
root.title("Formulario Básico")
root.geometry("400x500")

# Instanciar y colocar el grupo del Frame tipo de persona 'nino', 'adulto', 'nina'
tipe_person = gui_user.FrameTipePerson(root)
tipe_person.pack(padx=20, pady=10, fill='x')

# Instanciar y colocar el grupo del Frame de Peso y Altura
datos_of_user = gui_user.FrameDatos(root)
datos_of_user.pack(padx=20, pady=10, fill='x')

# Instanciar y colocar el grupo del Frame
mostrar_imc_calculado = gui_user.MostrarIMC(root)
mostrar_imc_calculado.pack(padx=20, pady=10, fill='x')

root.mainloop()
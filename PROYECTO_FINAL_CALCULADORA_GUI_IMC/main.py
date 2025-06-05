import tkinter as tk

import lib.recurso_gui as gui_user

from lib.tool import NucleoPrograma
from lib import adultos_bbdd, ninas_bbdd, ninos_bbdd
from lib.cargar_fuente import cargar_fuentes_temporales


TABLA_IMC = {
    "Adulto" : adultos_bbdd.tabla_adultos,
    "Niña" : ninas_bbdd.tabla_nina,
    "Niño" : ninos_bbdd.tabla_ninos
}

def clasificado(persona, valor_imc):
    for clasificacion_IMC, confirmacion in TABLA_IMC[persona].items():
        if confirmacion(valor_imc):
            return clasificacion_IMC

def notificacion_error(persona, peso, altura):
    print("Ocurrio algun error en los datos:\n")

    print(f"Persona: {persona}")
    print(f"Peso   : {peso}")
    print(f"altura : {altura}")

# Crear el cerebro de toda esta app
nucleo_process = NucleoPrograma()

# Cargar la fuente que usara este programa
cargar_fuentes_temporales("fuentes_ttf")

# Crear la ventana principal
root = tk.Tk()
root.title("Formulario Básico")
root.geometry("400x500")

# Instanciar y colocar el grupo del Frame tipo de persona 'nino', 'adulto', 'nina'
tipe_person = gui_user.FrameTipePerson(root, nucleo_process.tipo_persona)
tipe_person.pack(padx=20, pady=10, fill='x')

# Instanciar y colocar el grupo del Frame de Peso y Altura
datos_of_user = gui_user.FrameDatos(root)
datos_of_user.pack(padx=20, pady=10, fill='x')

# Instanciar y colocar el grupo del Frame
mostrar_imc_calculado = gui_user.MostrarIMC(root)
mostrar_imc_calculado.pack(padx=20, pady=10, fill='x')

# Ya bueno ahora pasamos todos los parametros que necesita nuestro nucleo central
# Procesamiento
root.bind_all(
    "<Return>",
    lambda event=None: nucleo_process.calcular_imc(
        datos_of_user.get_peso, datos_of_user.get_altura,
        notificacion_error,
        mostrar_imc_calculado.actualizar_imc,
        clasificado
    )
)

root.mainloop()

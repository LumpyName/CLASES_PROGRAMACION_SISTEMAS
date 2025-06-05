import tkinter as tk

class FrameTipePerson(tk.Frame):
    def __init__(self, master=None, receptor_of_tipo_person: callable = None, **kwargs):
        super().__init__(master, padx=10, pady=10, **kwargs)

        if not callable(receptor_of_tipo_person):
            raise ValueError("El parametro 'receptor_of_tipo_person' tiene que ser una funcion")

        # Variables independientes para cada botón
        self.adulto_var = tk.BooleanVar(value=False)
        self.nina_var = tk.BooleanVar(value=False)
        self.nino_var = tk.BooleanVar(value=False)

        # Función para manejar la selección única
        def seleccionar(tipo):
            # Desactiva todos
            self.adulto_var.set(False)
            self.nina_var.set(False)
            self.nino_var.set(False)

            # Activa solo el elegido
            if tipo == "Adulto":
                self.adulto_var.set(True)
            elif tipo == "Niña":
                self.nina_var.set(True)
            elif tipo == "Niño":
                self.nino_var.set(True)

            receptor_of_tipo_person(tipo)

        # Checkbutton para "Adulto"
        self.adultos_label = tk.Label(self, text="Adulto")
        self.adultos_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.adultos_check = tk.Checkbutton(
            self, variable=self.adulto_var,
            command=lambda: seleccionar("Adulto")
        )
        self.adultos_check.grid(row=0, column=1, padx=5, pady=5)

        # Checkbutton para "Niña"
        self.ninas_label = tk.Label(self, text="Niña")
        self.ninas_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.ninas_check = tk.Checkbutton(
            self, variable=self.nina_var,
            command=lambda: seleccionar("Niña")
        )
        self.ninas_check.grid(row=1, column=1, padx=5, pady=5)

        # Checkbutton para "Niño"
        self.ninos_label = tk.Label(self, text="Niño")
        self.ninos_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.ninos_check = tk.Checkbutton(
            self, variable=self.nino_var,
            command=lambda: seleccionar("Niño")
        )
        self.ninos_check.grid(row=2, column=1, padx=5, pady=5)

        # NOTA: No se selecciona ninguno al inicio (todas las variables están en False)



class FrameDatos(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, padx=10, pady=10, **kwargs)
        
        # Label y cuadro de entrada para "PESO"
        self.peso_label = tk.Label(self, text="PESO")
        self.peso_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.peso_entry = tk.Entry(self)
        self.peso_entry.grid(row=0, column=1, padx=5, pady=5)

        # Label y cuadro de entrada para "ALTURA"
        self.altura_label = tk.Label(self, text="Altura (en metros)")
        self.altura_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.altura_entry = tk.Entry(self, width=20)
        self.altura_entry.grid(row=1, column=1, padx=5, pady=5)

    def get_peso(self):
        return self.peso_entry.get()

    def get_altura(self):
        return self.altura_entry.get()


class MostrarIMC(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, padx=10, pady=10, **kwargs)

        # Label superior para IMC
        self.imc_top_label = tk.Label(self, text="Cálculo de IMC")
        self.imc_top_label.grid(row=0, column=0, columnspan=2, pady=5)

        # Label para "IMC:"
        self.imc_label = tk.Label(self, text="IMC:")
        self.imc_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        # Cuadro de texto grande con un label centrado dentro
        self.imc_box = tk.Label(self, text="IMC Calculado", relief="solid", width=20, height=3, justify="center")
        self.imc_box.grid(row=1, column=1, pady=15, padx=5)

    def actualizar_imc(self, persona, valor_imc, clasificado_imc):
        """Actualiza el texto mostrado en la caja del IMC"""
        self.imc_box.config(
            text=f"{clasificado_imc}"
        )
        self.imc_top_label.config(
            text=f"Cálculo de IMC: {valor_imc}; Para '{persona}'"
        )

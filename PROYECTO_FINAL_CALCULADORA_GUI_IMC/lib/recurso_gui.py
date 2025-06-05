import tkinter as tk

class FrameTipePerson(tk.Frame):
    def __init__(self, master=None, receptor_of_tipo_person: callable = None, **kwargs):
        super().__init__(master, padx=10, pady=10, **kwargs)
        
        # Verificando si el parametro "receptor_of_tipo_person" es una funcion
        if not callable(receptor_of_tipo_person):
            raise ValueError("El parametro 'receptor_of_tipo_person' tiene que ser una funcion")

        # Para el flujo de datos de 
        self.selection_tipo = tk.StringVar()
        
        # Label y Radiobutton para "Adultos"
        self.adultos_label = tk.Label(self, text="Adultos")
        self.adultos_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.adultos_check = tk.Radiobutton(
            self, variable=self.selection_tipo, 
            command=lambda: receptor_of_tipo_person("Adulto")
        )
        self.adultos_check.grid(row=0, column=1, padx=5, pady=5)
        
        # Label y Radiobutton para "Niñas"
        self.ninas_label = tk.Label(self, text="Niñas")
        self.ninas_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.ninas_check = tk.Radiobutton(
            self, variable=self.selection_tipo, 
            command=lambda: receptor_of_tipo_person("Niñas")
        )
        self.ninas_check.grid(row=1, column=1, padx=5, pady=5)
        
        # Label y Radiobutton para "Niños"
        self.ninos_label = tk.Label(self, text="Niños")
        self.ninos_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.ninos_check = tk.Radiobutton(
            self, variable=self.selection_tipo, 
            command=lambda: receptor_of_tipo_person("Niños")
        )
        self.ninos_check.grid(row=2, column=1, padx=5, pady=5)


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

    def actualizar_imc(self, tipe_person, valor):
        """Actualiza el texto mostrado en la caja del IMC"""
        # self.imc_box.config(text=valor)
        print(f""""
            Persona: {tipe_person}
            IMC    : {valor}
        """)

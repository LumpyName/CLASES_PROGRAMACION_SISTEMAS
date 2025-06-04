def formatear_numero(num: float) -> float:
    """
    Formatea un número según las siguientes reglas:
    - Si tiene decimales, muestra hasta 3 decimales.
    - Si tiene decimales distintos de .0, los muestra hasta 2 o 3 decimales.
    """
    if num == int(num):  # Si es entero (2.0 -> 2)
        return int(num)
    else:
        return round(num, 3)  # Redondea a 3 decimales si tiene más


class Rangos:
    def __init__(self, desde, hasta):
        self.desde = desde
        self.hasta = hasta

    def status(self, probar):
        return self.desde <= probar < self.hasta

# float("-inf") el infinito negativo
# float("inf") el infinito positivo

class NucleoPrograma:

    def __init__(self):
        self.persona = None

        self.peso = None
        self.altura = None
    
    def tipo_persona(self, persona):
        if persona in ["adultos", "ninos", "ninas"]:
            self.persona = persona
    
    def el_peso(self, peso):
        try:
            self.peso = formatear_numero(float(peso))
        except ValueError:
            self.peso = None

    def la_altura(self, altura):
        try:
            self.altura = formatear_numero(float(altura))
        except ValueError:
            self.altura = None
    
    def calcular_imc(self, notificacion_error: function, mostrar_resultados: function):
        if all([self.persona, self.peso, self.altura]):
            mostrar_resultados(
                persona=self.persona, imc=round(self.peso / (self.altura)**2, 2)
            )
            return

        notificacion_error(
            persona=self.persona, peso=self.peso, altura=self.altura
        )
        return


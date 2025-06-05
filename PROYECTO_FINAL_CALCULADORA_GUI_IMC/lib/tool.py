"""Herramientas necesarias para la APP"""

def _formatear_numero(num: float) -> float:
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
        self.__persona = None

        self.peso = None
        self.altura = None
    
    def tipo_persona(self, persona):
        self.__persona = persona
    
    def __el_peso(self, peso):
        try:
            self.peso = _formatear_numero(float(peso))
        except ValueError:
            self.peso = None

    def __la_altura(self, altura):
        try:
            self.altura = _formatear_numero(float(altura))
        except ValueError:
            self.altura = None
    
    def calcular_imc(
            self, get_peso:callable, get_altura:callable,
            notificacion_error:callable, mostrar_resultados:callable,
            clasificado:callable
        ):
        """
    Parámetros:
        Calcula el IMC utilizando funciones externas para obtener datos y mostrar resultados.

        get_peso (callable): Función que retorna el peso como número flotante.

        get_altura (callable): Función que retorna la altura como número flotante.

        notificacion_error (callable): Se le pasan tres argumentos nombrados:
            - persona (str or None)
            - peso (float or None)
            - altura (float or None)

        mostrar_resultados (callable): Se le pasan tres argumentos nombrados:
            - persona (str)
            - valor_imc (float)
            - clasificado_imc (str)

        clasificado (callable): Se le pasan dos argumentos posicionales:
            - persona (str)
            - IMC (float)
        """

        # Obteniendo el peso y su estatura
        self.__el_peso(get_peso())
        self.__la_altura(get_altura())

        IMC = round(self.peso / (self.altura)**2, 2)
        if all([self.__persona, self.peso, self.altura]):
            mostrar_resultados(
                persona=self.__persona, valor_imc=IMC,
                clasificado_imc=clasificado(self.__persona, IMC)
            )
            return

        notificacion_error(
            persona=self.__persona, peso=self.peso, altura=self.altura
        )
        return

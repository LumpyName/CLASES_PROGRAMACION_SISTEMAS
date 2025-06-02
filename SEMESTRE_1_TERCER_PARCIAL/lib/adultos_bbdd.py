from .tool import Rangos

tabla_adultos = { # Seccion adultos
    "Bajo peso": Rangos(float("-inf"), 18.5).status,
    "Peso normal": Rangos(18.5, 24.9).status,
    "Sobrepeso": Rangos(25.0, 29.9).status,
    "Obesidad grado 1": Rangos(30.0, 34.9).status,
    "Obesidad grado 2": Rangos(35.0, 39.9).status,
    "Obesidad grado 3": Rangos(40.0, float("inf")).status,
}
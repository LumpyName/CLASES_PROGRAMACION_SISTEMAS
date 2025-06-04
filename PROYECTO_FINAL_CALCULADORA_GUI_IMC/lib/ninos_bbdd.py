from .tool import Rangos

tabla_ninos = { # Seccion niño
    "Bajo peso": Rangos(float("-inf"), 14.5).status,
    "Peso saludable": Rangos(14.5, 19.0).status,
    "Riesgo de sobrepeso": Rangos(19.1, 21.5).status,
    "Sobrepeso": Rangos(21.5, float("inf")).status,
}

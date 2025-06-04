from .tool import Rangos

tabla_nina = { # Seccion niña
    "Bajo peso": Rangos(float("-inf"), 14.0).status,
    "Peso saludable": Rangos(14.0, 18.1).status,
    "Riesgo de sobrepeso": Rangos(18.1, 20.5).status,
    "Sobrepeso": Rangos(20.5, float("inf")).status,
}
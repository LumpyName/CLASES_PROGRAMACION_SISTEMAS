class Rangos:
    def __init__(self, desde, hasta):
        self.desde = desde
        self.hasta = hasta

    def status(self, probar):
        return self.desde <= probar < self.hasta

# float("-inf") el infinito negativo
# float("inf") el infinito positivo


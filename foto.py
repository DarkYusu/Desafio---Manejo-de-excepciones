from error import DimensionError

class Foto:
    MAX = 1000  # Valor máximo permitido para ancho y alto

    def __init__(self, ancho, alto):
        self._ancho = ancho
        self._alto = alto

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, value):
        # Requerimiento 3: Lanzar una excepción de tipo DimensionError si el nuevo valor no cumple con las condiciones y asignar el nuevo valor al atributo de instancia si es válido.
        if value < 1 or value > self.MAX:
            raise DimensionError("Valor de ancho inválido", dimension=value, maximo=self.MAX)
        self._ancho = value

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, value):
        if value < 1 or value > self.MAX:
            raise DimensionError("Valor de alto inválido", dimension=value, maximo=self.MAX)
        self._alto = value

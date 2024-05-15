# Requerimiento 1: Crear la excepción DimensionError derivada de Exception.
class DimensionError(Exception):
    def __init__(self, mensaje, dimension=None, maximo=None):
        #Sobreescribir el constructor, recibiendo los parámetros mensaje, dimension y maximo y asignándoles los respectivos atributos de instancia.
        super().__init__(mensaje)
        self.mensaje = mensaje
        self.dimension = dimension
        self.maximo = maximo

    # Requerimiento 2: Sobrecargar el método __str__ y crear y retornar un mensaje utilizando los atributos mensaje, dimension y maximo.
    def __str__(self):
        if self.dimension is None and self.maximo is None:
            return super().__str__()
        else:
            parts = [self.mensaje]
            if self.dimension is not None:
                parts.append(f"Dimension: {self.dimension}")
            if self.maximo is not None:
                parts.append(f"Máximo permitido: {self.maximo}")
            return " - ".join(parts)

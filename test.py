from error import DimensionError
from foto import Foto

try:
    raise DimensionError("Error básico")
except DimensionError as e:
    print("Mensaje básico de la excepción:", str(e))


try:
    raise DimensionError("Error detallado", dimension=500, maximo=1000)
except DimensionError as e:
    print("Mensaje detallado de la excepción:", str(e))

foto = Foto(800, 600)
print("Dimensiones iniciales:", foto.ancho, "x", foto.alto)

try:
    foto.ancho = 1200
except DimensionError as e:
    print("Error al asignar ancho:", str(e))

try:
    foto.alto = -100
except DimensionError as e:
    print("Error al asignar alto:", str(e))

print("Dimensiones después de intentar asignar valores inválidos:", foto.ancho, "x", foto.alto)

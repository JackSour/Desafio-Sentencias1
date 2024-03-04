
import random
import sys

# Ingreso de datos por parte de usuario
usuario = sys.argv[1]

# Opciones validas
opciones = ["piedra", "papel", "tijera"]

# Verifica si se proporciona el argumento adecuado
if len(sys.argv) != 2 or sys.argv[1] not in (opciones):
    print("Argumento inválido: Debe ser piedra, papel o tijera.")
    sys.exit()

# Seleccion random
npc = random.choice(opciones)

# Imprimir selecciones
print("Tu jugaste", usuario)
print("Computadora jugó", npc)

# Lógica para determinar el resultado
# Empate
if usuario == npc:
    print("¡Empate!")
# Ganaste
elif((usuario == "piedra" and npc == "tijera") or \
    (usuario == "papel" and npc == "piedra") or \
    (usuario == "tijera" and npc == "papel")): 
    print("¡Ganaste!")
# Perdiste
else:
    print("¡Perdiste!")
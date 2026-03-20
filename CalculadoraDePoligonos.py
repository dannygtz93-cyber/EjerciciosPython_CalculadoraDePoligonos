# ==========================#
#  INPUTS
# ==========================#

from math import pi

# ==========================#
#  CONSTANTES GLOBALES
# ==========================#

TITULO = "Calculadora de poligonos"
VERSION = "0.2.7"

# ==========================#
#  FUNCIONES DE INTERFAZ (UI)
# ==========================#

def impr_titulo_version():
  print(f"{TITULO} v{VERSION}\n")

def impr_instrucciones():
  print(f"Puedo calcular el área de una figura elegida: {MENU_INTERACTIVO}\n")

def pedir_respuesta():

  while True:

    try:

      figura = int(input(f"📐 ¿Que figura quieres calcular? {OPCIONES}: "))
      print()

      if figura in FIGURAS:
        return figura

      else:
        print(f"Ingresa solo {OPCIONES}\n")

    except ValueError:
      print()
      print(f"Ingresa solo {OPCIONES}\n")
    
def pedir_numero(mensaje):

  while True:

    try:

      numero = float(input(mensaje))
      return numero

    except ValueError:
      print()
      print("Ingresa solo números\n")

def preguntar_reinicio():

  while True:
    
    respuesta = input("\n¿Quieres hacer otro calculo? (s/n): ").strip().lower()
    print()

    if respuesta in ("s", "si"):
      print("🧮 Nuevo calculo")
      print()
      return True

    elif respuesta in ("n", "no"):
      return False

    else:
      print("Responde solo: s o n\n")

# ==========================#
#  LOGICA DE NEGOCIO (CORE)
# ==========================#

def area_rectangulo(base, altura):

  return base * altura

def area_triangulo(base, altura):

  return (base * altura) / 2

def area_circulo(radio):
  return pi * (radio ** 2)

# ==========================#
# CONFIGURACIÓN DEL SISTEMA
# ==========================#

FIGURAS = {
  1: ("Rectángulo", area_rectangulo, ["la base", "la altura"]),
  2: ("Triángulo", area_triangulo, ["la base", "la altura"]),
  3: ("Círculo", area_circulo, ["el radio"])
}

OPCIONES = ", ".join(map(str, FIGURAS.keys()))

MENU = []

for clave, datos in FIGURAS.items():

  clave = clave
  datos = datos[0]

  texto = (f"{clave}. {datos}")
  
  MENU.append(texto)

MENU_INTERACTIVO = ", ".join(MENU)

# ==========================#
#  ORQUESTACIÓN (FLUJO)
# ==========================#
 
def calcular_area():

  figura = pedir_respuesta()

  nombre, funcion, parametros = FIGURAS[figura]

  datos = []

  for parametro in parametros:

    numero = pedir_numero(f"Ingresa {parametro}: ")

    datos.append(numero)
  
  area = funcion(*datos)

  print("\n" + "=" * 40)
  print(f"✅ El área de tu {nombre} es: {area:.2f}")
  print("=" * 40)

# ==========================#
#  ENTRY POINT
# ==========================#

def main ():

  impr_titulo_version()
  impr_instrucciones()

  while True:

    calcular_area()

    if not preguntar_reinicio():
      print("¡Gracias por usar la calculadora!\n")
      break

if __name__ == "__main__":
    main()

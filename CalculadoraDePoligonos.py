from math import pi

TITULO = "Calculadora de poligonos"
VERSION = "0.2.5"

def impr_titulo_version():
  print(f"{TITULO} v{VERSION}\n")

def impr_instrucciones():
  print(f"Puedo calcular el área de una figura elegida: 1. Rectángulo, 2. Triángulo y 3. Círculo\n")

def pedir_respuesta():

  while True:

    try:

      figura = int(input(f"¿Que figura quieres calcular? {OPCIONES}: "))
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
    
    respuesta = input("¿Quieres hacer otro calculo? (s/n): ").strip().lower()
    print()

    if respuesta in ("s", "si"):
      print("🧮 Nuevo calculo")
      print()
      return True

    elif respuesta in ("n", "no"):
      return False

    else:
      print("Responde solo: s o n\n")

def area_rectangulo(base, altura):

  return base * altura

def area_triangulo(base, altura):

  return (base * altura) / 2

def area_circulo(radio):
  return pi * (radio ** 2)

FIGURAS = {
  1: ("Rectángulo", area_rectangulo, ["la base", "la altura"]),
  2: ("Triángulo", area_triangulo, ["la base", "la altura"]),
  3: ("Círculo", area_circulo, ["el radio"])
}

OPCIONES = ", ".join(map(str, FIGURAS.keys()))
 
def calcular_area():

  figura = pedir_respuesta()

  nombre, funcion, parametros = FIGURAS[figura]

  datos = []

  for parametro in parametros:

    numero = pedir_numero(f"Ingresa tu {parametro}: ")

    datos.append(numero)
  
  area = round(funcion(*datos), 2)

  print()
  print(f"El area de tu {nombre} es = {area}")
  print()

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
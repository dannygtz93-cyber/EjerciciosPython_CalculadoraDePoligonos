from math import pi

TITULO = "Calculadora de poligonos"
VERSION = "0.2.4"

def impr_titulo_version():
  print(f"{TITULO} v{VERSION}\n")

RESPUESTAS_VALIDAS = {1, 2, 3}

def impr_instrucciones():
  print(f"Puedo calcular el área de una figura elegida: 1. Rectángulo, 2. Triángulo y 3. Circulo\n")

def pedir_respuesta():

  while True:

    try:

      figura = int(input("¿Que figura quieres calcular? (1= Rectángulo, 2= Triangulo, 3= Círculo): "))
      print()

      if figura in RESPUESTAS_VALIDAS:
        return figura

      else:
        print("Ingresa solo 1, 2 ó 3\n")

    except ValueError:
      print()
      print("Ingresa solo 1, 2 ó 3\n")
    
def pedir_numero(mensaje):

  while True:

    try:

      numero = float(input(mensaje))
      return numero

    except ValueError:
      print()
      print("Ingresa solo números\n")

def area_rectangulo(base, altura):

  return base * altura

def area_triangulo(base, altura):

  return (base * altura) / 2

def area_circulo(radio):
  return pi * (radio ** 2)

FIGURAS = {
  1: ("Rectángulo", area_rectangulo),
  2: ("Triángulo", area_triangulo),
  3: ("Círculo", area_circulo)
}
 
def calculo_poligono():

  figura = pedir_respuesta()

  nombre, funcion = FIGURAS[figura]

  if figura == 3:
    
    radio = pedir_numero("¿Cual es el radio?: ")

    area = funcion(radio)

  else:
   
    base = pedir_numero("¿Cual es la base?: ")
    altura = pedir_numero("¿Cual es la altura?: ")

    area = funcion(base, altura)

  print()
  print(f"El area de tu {nombre} es= {area}")
  print()

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


def main ():

  impr_titulo_version()
  impr_instrucciones()

  while True:

    calculo_poligono()

    if not preguntar_reinicio():
      print("¡Gracias por usar la calculadora!\n")
      break

if __name__ == "__main__":
    main()
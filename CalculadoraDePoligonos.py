TITULO = "Calculadora de poligonos"
VERSION = "0.1.3"

def impr_titulo_version():
  print(f"{TITULO} v{VERSION}\n")

RESPUESTAS_VALIDAS = {1, 2}

def impr_instrucciones():
  print(f"Puedo calcular el área de una figura elegida: 1. Rectangulo ó 2. Triangulo\n")

def pedir_respuesta():

  while True:

    try:

      figura = int(input("¿Que figura quieres calcular? (1 ó 2): "))
      print()

      if figura in RESPUESTAS_VALIDAS:
        return figura

      else:
        print("Ingresa solo 1 ó 2\n")

    except ValueError:
      print()
      print("Ingresa solo 1 ó 2\n")
    
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
 
def calculo_poligono():

  figura = pedir_respuesta()
   
  base = pedir_numero("¿Cual es la base?: ")
  altura = pedir_numero("¿Cual es la altura?: ")

  if figura == 1:

    area = area_rectangulo(base, altura)

  else:

    area = area_triangulo(base, altura)

  print()
  print("El area de tu figura es= ",area)
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
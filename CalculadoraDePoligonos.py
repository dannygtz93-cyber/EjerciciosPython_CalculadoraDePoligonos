TITULO = "Calculadora de poligonos"
VERSION = "0.1.2"

def impr_titulo_version():
  print(f"{TITULO} v{VERSION}\n")

RESPUESTAS_VALIDAS = {1, 2}

def impr_instrucciones():
  print("Puedo calcular el área de una figura elegida: 1. rectangulo, 2. triangulo\n")

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

def calculo_poligono():

  figura = pedir_respuesta()
  base = pedir_numero("¿Cual es la base?: ")
  altura = pedir_numero("¿Cual es la altura?: ")

  if figura == 1:

    area = base * altura

    print()
    print(f"El área de tu rectangulo es = ", area)
    print()

  else:

    area = (base * altura)/2

    print()
    print(f"El área de tu triangulo es = ", area)
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
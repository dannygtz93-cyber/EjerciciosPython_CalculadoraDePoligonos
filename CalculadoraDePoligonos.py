TITULO = "Calculadora de poligonos"
VERSION = "0.0.1"

def impr_titulo_version():
  print(f"{TITULO} v{VERSION}\n")

def impr_instrucciones():
  print("Puedo calcular el área de un poligono\n")

def calculo_poligono():

  while True:

    try:

      base = int(input("¿Cual es la base? = "))
      altura = int(input("¿Cual es la altura? = "))
      print()

      area = base * altura

      print(f"El área de tu poligono es = ", area)
      break

    except ValueError:
      print("Ingresa solo numeros\n")

def main ():
  impr_titulo_version()
  impr_instrucciones()
  calculo_poligono()

if __name__ == "__main__":
    main()

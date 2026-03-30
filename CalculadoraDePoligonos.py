# ==========================#
#  INPUTS
# ==========================#

from math import pi, tan

# ==========================#
#  CONSTANTES GLOBALES
# ==========================#

TITULO = "Calculadora de poligonos"
VERSION = "0.5.0"

# ==========================#
#  FUNCIONES DE INTERFAZ (UI)
# ==========================#

def impr_titulo_version():
  print(f"{TITULO} v{VERSION}\n")

def impr_instrucciones():
  print(f"¡Bienvenido a la {TITULO}! Puedo calcular el area y el perimetro de una figura elegida:\n")

def pedir_respuesta():

  while True:

    try:

      print(MENU_INTERACTIVO)
      figura = int(input("\n📐 ¿Qué figura quieres calcular?: "))
      print()

      if 1 <= figura <= len(FIGURAS):
        return figura

      else:
        print(f"Ingresa un número entre 1 y {len(FIGURAS)}\n")

    except ValueError:
      print(f"\n❌ Ingresa un número entre 1 y {len(FIGURAS)}\n")

def pedir_tipo_calculo():

    print("1. Área")
    print("2. Perímetro")
    print()

    while True:
        opcion = input("¿Qué deseas calcular?: ")
        print()

        if opcion in ("1", "2"):
            return opcion

        print("Ingresa 1 o 2")
    
def pedir_entrada(mensaje, minimo, tipo_esperado=float):
    while True:
        try:
            valor_raw = input(mensaje)
            if tipo_esperado == int:
                numero = float(valor_raw)
                if not numero.is_integer():
                    print("❌ El número de lados debe ser un entero (sin decimales).")
                    continue
                numero = int(numero)
            else:
                numero = float(valor_raw)

            if numero >= minimo:
                return numero
            
            print(f"❌ El valor debe ser mayor o igual a {minimo}")
        except ValueError:
            print(f"❌ Entrada inválida. Por favor ingresa un número {'entero' if tipo_esperado == int else 'válido'}.")

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
#  CLASES
# ==========================#

class Figura:
  def __init__(self, nombre, params):
    self.nombre = nombre
    self.params = params

  def area(self):
    pass

  def perimetro(self):
    pass

class Rectangulo(Figura):
   
  def __init__(self):
    params = [
            {"mensaje": "la base", "min": 0.1, "tipo": float},
            {"mensaje": "la altura", "min": 0.1, "tipo": float}
            ]
    super().__init__("Rectángulo", params)

  def area(self, base, altura):
    return base * altura
  
  def perimetro(self, base, altura):
    return 2 * (base + altura)
   
class Triangulo(Figura):
   
  def __init__(self):
    params = [
            {"mensaje": "la base", "min": 0.1, "tipo": float},
            {"mensaje": "la altura", "min": 0.1, "tipo": float}
            ]
    super().__init__("Triángulo", params)

  def area(self, base, altura):
    return (base * altura) / 2
  
  def perimetro(self, *args):
    print("Perímetro no disponible para esta figura")
    return None
  
class Circulo(Figura):
   
  def __init__(self):
    params = [
            {"mensaje": "el radio", "min": 0.1, "tipo": float}
            ]
    super().__init__("Círculo", params)

  def area(self, radio):
    return pi * (radio ** 2)
  
  def perimetro(self, radio):
    return 2 * pi * radio
  
class PoligonoRegular(Figura):
   
  def __init__(self):
    params = [
            {"mensaje": "el número de lados", "min": 3, "tipo": int},
            {"mensaje": "la longitud de un lado", "min": 0.1, "tipo": float}
            ]
    super().__init__("Polígono regular", params)

  def area(self, n_lados, lado):
    apotema = lado / (2 * tan(pi / n_lados))
    perimetro = n_lados * lado
    return (perimetro * apotema) / 2
  
  def perimetro(self, n_lados, lado):
    return n_lados * lado
  
class Trapecio(Figura):

  def __init__(self):
    params = [
            {"mensaje": "la base mayor", "min": 0.1, "tipo": float},
            {"mensaje": "la base menor", "min": 0.1, "tipo": float},
            {"mensaje": "la altura", "min": 0.1, "tipo": float}
            ]
    super().__init__("Trapecio", params)

  def area(self, base_mayor, base_menor, altura):
    return ((base_mayor + base_menor) * altura) / 2
  
  def perimetro(self, *args):
    print("Perímetro no disponible para esta figura")
    return None
  
class Elipse(Figura):

  def __init__(self):
    params = [
            {"mensaje": "el semieje mayor (a)", "min": 0.1, "tipo": float},
            {"mensaje": "el semieje menor (b)", "min": 0.1, "tipo": float}
            ]
    super().__init__("Elipse", params)

  def area(self, a, b):
    return pi * a * b
  
  def perimetro(self, a, b):
    return pi * (3*(a+b) - ((3*a + b)*(a + 3*b))**0.5)

# ==========================#
# CONFIGURACIÓN DEL SISTEMA
# ==========================#

FIGURAS = [
  Rectangulo(),
  Triangulo(),
  Circulo(),
  PoligonoRegular(),
  Trapecio(),
  Elipse()
]

MENU = []

for indice, figura in enumerate (FIGURAS, 1):
  texto = f"{indice}. {figura.nombre}"
  MENU.append(texto)

MENU_INTERACTIVO = "\n".join(MENU)

# ==========================#
#  ORQUESTACIÓN (FLUJO)
# ==========================#
 
def calcular_figura():

    figura_id = pedir_respuesta()
    config = FIGURAS[figura_id - 1]

    tipo = pedir_tipo_calculo()

    argumentos = []
    for param in config.params:
        valor = pedir_entrada(
            f"Ingresa {param['mensaje']}: ",
            minimo=param["min"],
            tipo_esperado=param["tipo"]
        )
        argumentos.append(valor)

    if tipo == "1":
        resultado = config.area(*argumentos)
        texto = "área"
    else:
        resultado = config.perimetro(*argumentos)
        texto = "perímetro"

    print("\n" + "=" * 45)
    print(f"✅ El {texto} de tu {config.nombre} es: {resultado:.2f}")
    print("=" * 45)

# ==========================#
#  ENTRY POINT
# ==========================#

def main ():

  impr_titulo_version()
  impr_instrucciones()

  while True:

    calcular_figura()

    if not preguntar_reinicio():
      print("¡Gracias por usar la calculadora!\n")
      break

if __name__ == "__main__":
    main()

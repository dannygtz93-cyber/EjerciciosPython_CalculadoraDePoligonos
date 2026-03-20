# ==========================#
#  INPUTS
# ==========================#

from math import pi, tan

# ==========================#
#  CONSTANTES GLOBALES
# ==========================#

TITULO = "Calculadora de poligonos"
VERSION = "0.3.8"

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
#  LOGICA DE NEGOCIO (CORE)
# ==========================#

def area_rectangulo(base, altura):

  return base * altura

def area_triangulo(base, altura):

  return (base * altura) / 2

def area_circulo(radio):
  return pi * (radio ** 2)

def area_poligono_regular(n_lados, lado):
    apotema = lado / (2 * tan(pi / n_lados))
    perimetro = n_lados * lado
    return (perimetro * apotema) / 2

# ==========================#
# CONFIGURACIÓN DEL SISTEMA
# ==========================#

FIGURAS = {
    1: {
        "nombre": "Rectángulo",
        "funcion": area_rectangulo,
        "params": [
            {"nombre": "la base", "min": 0.1, "tipo": float},
            {"nombre": "la altura", "min": 0.1, "tipo": float}
        ]
    },
    2: {
        "nombre": "Triángulo",
        "funcion": area_triangulo,
        "params": [
            {"nombre": "la base", "min": 0.1, "tipo": float},
            {"nombre": "la altura", "min": 0.1, "tipo": float}
        ]
    },
    3: {
        "nombre": "Círculo",
        "funcion": area_circulo,
        "params": [
            {"nombre": "el radio", "min": 0.1, "tipo": float}
        ]
    },
    4: {
        "nombre": "Polígono Regular",
        "funcion": area_poligono_regular,
        "params": [
            {"nombre": "el número de lados", "min": 3, "tipo": int},
            {"nombre": "la longitud de un lado", "min": 0.1, "tipo": float}
        ]
    }
}

OPCIONES = ", ".join(map(str, FIGURAS.keys()))

MENU = []

for clave, config in FIGURAS.items():
  nombre = config["nombre"]
  texto = f"{clave}. {nombre}"
  MENU.append(texto)

MENU_INTERACTIVO = ", ".join(MENU)

# ==========================#
#  ORQUESTACIÓN (FLUJO)
# ==========================#
 
def calcular_area():
    figura_id = pedir_respuesta()
    config = FIGURAS[figura_id]
    
    argumentos = []
    for param in config["params"]:
      valor = pedir_entrada(
        f"Ingresa {param['nombre']}: ",
        minimo=param["min"],
        tipo_esperado=param["tipo"]
    )
      argumentos.append(valor)
    
    resultado = config["funcion"](*argumentos)
    print(f"\n✅ El área de tu {config['nombre']} es: {resultado:.2f}")

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

# Changelog
Todos los cambios importantes de este proyecto serán documentados en este archivo.

El formato está basado en Keep a Changelog y este proyecto usa Versionado Semántico.

---

## [0.0.2] - 2026-03-13

### Añadido
- Se agregó un bloque `try-except` para manejar errores de tipo `ValueError`. Ahora el programa no se cierra si el usuario ingresa letras.
- Estructura principal mejorada con la función `if __name__ == "__main__":`.

### Cambiado
- Se refactorizó el código en funciones específicas (`impr_titulo_version`, `impr_instrucciones`, `calculo_poligono`) para una mejor lectura.

---

## [0.0.1] - 2026-02-20

### Añadido
- Versión inicial del script.
- Lógica básica de cálculo: $área = base \times altura$.
- Impresión básica de resultados en consola.
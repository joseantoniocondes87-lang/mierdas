# mierdas

Código listo para usar - Ready-to-use code utilities

## 📚 Descripción

Una colección de utilidades en Python listas para usar en tus proyectos. Funciones simples pero útiles para el día a día.

## 🚀 Uso Rápido

```python
from utils import contar_palabras, calcular_promedio, es_palindromo

# Contar palabras en un texto
texto = "Hola mundo desde Python"
print(contar_palabras(texto))  # 4

# Calcular promedio
numeros = [10, 20, 30, 40]
print(calcular_promedio(numeros))  # 25.0

# Verificar palíndromo
print(es_palindromo("anita lava la tina"))  # True
```

## 📦 Funciones Disponibles

### Funciones de Texto
- `contar_palabras(texto)` - Cuenta palabras en un texto
- `invertir_texto(texto)` - Invierte un texto
- `es_palindromo(texto)` - Verifica si es palíndromo
- `limpiar_espacios(texto)` - Elimina espacios extra
- `capitalizar_palabras(texto)` - Capitaliza cada palabra
- `contar_vocales(texto)` - Cuenta las vocales

### Funciones Numéricas
- `calcular_promedio(numeros)` - Calcula el promedio
- `encontrar_maximo(numeros)` - Encuentra el máximo
- `encontrar_minimo(numeros)` - Encuentra el mínimo

### Funciones de Listas
- `eliminar_duplicados(lista)` - Elimina duplicados manteniendo orden

## 🎯 Ejemplos

Ejecuta el archivo de ejemplos para ver todas las funciones en acción:

```bash
python ejemplos.py
```

## 💡 Ejemplos de Código

```python
# Limpiar texto
from utils import limpiar_espacios
texto = "  Hola    mundo   "
print(limpiar_espacios(texto))  # "Hola mundo"

# Encontrar el número más grande
from utils import encontrar_maximo
numeros = [15, 42, 8, 23, 16]
print(encontrar_maximo(numeros))  # 42

# Eliminar duplicados
from utils import eliminar_duplicados
lista = [1, 2, 2, 3, 1, 4]
print(eliminar_duplicados(lista))  # [1, 2, 3, 4]
```

## 📄 Licencia

Código libre para usar como quieras.

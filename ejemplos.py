"""
Ejemplos de uso de las utilidades
Examples of using the utilities
"""

from utils import (
    contar_palabras,
    invertir_texto,
    es_palindromo,
    calcular_promedio,
    encontrar_maximo,
    encontrar_minimo,
    limpiar_espacios,
    capitalizar_palabras,
    contar_vocales,
    eliminar_duplicados
)


def ejemplos_texto():
    """Ejemplos de funciones de texto"""
    print("=== EJEMPLOS DE TEXTO ===\n")
    
    # Contar palabras
    texto = "Hola mundo, esto es un ejemplo"
    print(f"Texto: '{texto}'")
    print(f"Número de palabras: {contar_palabras(texto)}")
    print()
    
    # Invertir texto
    print(f"Texto invertido: '{invertir_texto(texto)}'")
    print()
    
    # Palíndromo
    palindromo = "anita lava la tina"
    print(f"'{palindromo}' es palíndromo: {es_palindromo(palindromo)}")
    print()
    
    # Limpiar espacios
    texto_sucio = "  Hola    mundo   con   espacios   extra  "
    print(f"Texto original: '{texto_sucio}'")
    print(f"Texto limpio: '{limpiar_espacios(texto_sucio)}'")
    print()
    
    # Capitalizar
    texto_min = "hola mundo desde python"
    print(f"Original: '{texto_min}'")
    print(f"Capitalizado: '{capitalizar_palabras(texto_min)}'")
    print()
    
    # Contar vocales
    texto_vocales = "Programación en Python"
    print(f"'{texto_vocales}' tiene {contar_vocales(texto_vocales)} vocales")
    print()


def ejemplos_numeros():
    """Ejemplos de funciones numéricas"""
    print("=== EJEMPLOS DE NÚMEROS ===\n")
    
    numeros = [15, 23, 8, 42, 16, 4, 89, 12]
    print(f"Lista de números: {numeros}")
    print(f"Promedio: {calcular_promedio(numeros)}")
    print(f"Máximo: {encontrar_maximo(numeros)}")
    print(f"Mínimo: {encontrar_minimo(numeros)}")
    print()


def ejemplos_listas():
    """Ejemplos de funciones de listas"""
    print("=== EJEMPLOS DE LISTAS ===\n")
    
    lista_duplicados = [1, 2, 3, 2, 4, 1, 5, 3, 6, 4]
    print(f"Lista original: {lista_duplicados}")
    print(f"Sin duplicados: {eliminar_duplicados(lista_duplicados)}")
    print()
    
    palabras = ["hola", "mundo", "hola", "python", "mundo", "código"]
    print(f"Palabras originales: {palabras}")
    print(f"Sin duplicados: {eliminar_duplicados(palabras)}")
    print()


if __name__ == "__main__":
    ejemplos_texto()
    ejemplos_numeros()
    ejemplos_listas()
    
    print("=== PRUEBA INTERACTIVA ===\n")
    print("Puedes importar estas funciones en tu propio código:")
    print("from utils import contar_palabras, calcular_promedio")

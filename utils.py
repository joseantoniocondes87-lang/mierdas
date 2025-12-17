"""
Utilidades listas para usar - Ready-to-use utilities
Una colección de funciones útiles para el día a día
"""


def contar_palabras(texto):
    """
    Cuenta el número de palabras en un texto.
    
    Args:
        texto (str): El texto a analizar
        
    Returns:
        int: Número de palabras
    """
    if not texto:
        return 0
    return len(texto.split())


def invertir_texto(texto):
    """
    Invierte un texto.
    
    Args:
        texto (str): El texto a invertir
        
    Returns:
        str: Texto invertido
    """
    return texto[::-1]


def es_palindromo(texto):
    """
    Verifica si un texto es un palíndromo.
    
    Args:
        texto (str): El texto a verificar
        
    Returns:
        bool: True si es palíndromo, False si no
    """
    texto_limpio = texto.lower().replace(" ", "")
    return texto_limpio == texto_limpio[::-1]


def calcular_promedio(numeros):
    """
    Calcula el promedio de una lista de números.
    
    Args:
        numeros (list): Lista de números
        
    Returns:
        float: Promedio de los números
    """
    if not numeros:
        return 0
    return sum(numeros) / len(numeros)


def encontrar_maximo(numeros):
    """
    Encuentra el número máximo en una lista.
    
    Args:
        numeros (list): Lista de números
        
    Returns:
        int/float: El número máximo
    """
    if not numeros:
        return None
    return max(numeros)


def encontrar_minimo(numeros):
    """
    Encuentra el número mínimo en una lista.
    
    Args:
        numeros (list): Lista de números
        
    Returns:
        int/float: El número mínimo
    """
    if not numeros:
        return None
    return min(numeros)


def limpiar_espacios(texto):
    """
    Elimina espacios extra de un texto.
    
    Args:
        texto (str): El texto a limpiar
        
    Returns:
        str: Texto sin espacios extra
    """
    return " ".join(texto.split())


def capitalizar_palabras(texto):
    """
    Capitaliza la primera letra de cada palabra.
    
    Args:
        texto (str): El texto a capitalizar
        
    Returns:
        str: Texto con palabras capitalizadas
    """
    return texto.title()


def contar_vocales(texto):
    """
    Cuenta el número de vocales en un texto.
    
    Args:
        texto (str): El texto a analizar
        
    Returns:
        int: Número de vocales
    """
    vocales = "aeiouAEIOUáéíóúÁÉÍÓÚ"
    return sum(1 for char in texto if char in vocales)


def eliminar_duplicados(lista):
    """
    Elimina elementos duplicados de una lista manteniendo el orden.
    
    Args:
        lista (list): La lista con posibles duplicados
        
    Returns:
        list: Lista sin duplicados
    """
    vistos = set()
    resultado = []
    for item in lista:
        if item not in vistos:
            vistos.add(item)
            resultado.append(item)
    return resultado

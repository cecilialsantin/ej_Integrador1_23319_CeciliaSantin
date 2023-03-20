import ej3
from ej3 import diccionario_palabra_frecuencia

def palabra_mas_frecuente(diccionario_palabra_frecuencia):
    max_palabra = ''
    max_frequencia = 0
    for palabra, frequencia in diccionario_palabra_frecuencia.items():
        if frequencia > max_frequencia:
            max_palabra = palabra
            max_frequencia = frequencia
    return max_palabra, max_frequencia

print(f"La palabra más frecuente y su frecuencia es: {palabra_mas_frecuente(diccionario_palabra_frecuencia)}" )



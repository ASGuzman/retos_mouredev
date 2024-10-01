"""
Reto #1
¿ES UN ANAGRAMA?
Dificultad: MEDIA

Enunciado: Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Boolean) según sean o no anagramas.
Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
NO hace falta comprobar que ambas palabras existan.
Dos palabras exactamente iguales no son anagrama.

Para saber si dos palabras son anagramas, necesitamos asegurarnos de que:
- Tienen las mismas letras.
- Cada letra aparece la misma cantidad de veces en ambas palabras.

"""
from collections import Counter

def son_anagramas(palabra1: str, palabra2: str) -> bool:
    palabra1_minuscula = palabra1.lower()
    palabra2_minuscula = palabra2.lower()
    palabra1_norm = palabra2_minuscula.replace(" ","")
    palabra2_norm = palabra1_minuscula.replace(" ","")
    if palabra1_norm == palabra2_norm:
        return False
    
    conteo1 = Counter(palabra1_norm)
    conteo2 = Counter(palabra2_norm)

    return conteo1 == conteo2

resultado = son_anagramas("amor", "roma")
print(resultado)

resultado2 = son_anagramas("amor", "amo")
print(resultado2)
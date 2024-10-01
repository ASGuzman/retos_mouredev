""" 
Reto #3
¿ES UN NÚMERO PRIMO?
Dificultad: MEDIA
Enunciado: Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.

¿Que es un numero primo? 
Un número primo es un número natural mayor que 1 que solo tiene dos divisores positivos: 1 y él mismo. 
En otras palabras, no se puede dividir exactamente (sin dejar residuo) por ningún otro número aparte de 1 
y el número primo en cuestión

¿Por qué verificar hasta numero // 2?
Si un número es divisible por un número mayor que su mitad, el resultado sería mayor que el número mismo. Por ejemplo, para 10, el único número que puede ser un divisor válido menor que 10 es 5, ya que cualquier número mayor que 5 multiplicado por un número entero dará como resultado un número mayor que 10.
Sin embargo, es más eficiente verificar solo hasta la raíz cuadrada del número. Esto es porque cualquier factor mayor que la raíz cuadrada ya tendrá un factor correspondiente que es menor.

"""
def main ():
    for numero in range (1,101):
        if num_primo(numero):
            print(numero)

def num_primo(numero: int) -> bool:
    if numero <= 1: 
        return False
    if numero == 2:
        return True
    for num in range(2,numero):
        if numero % num == 0:
            return False
    return True

main()

"""
Reto #2
LA SUCESIÓN DE FIBONACCI
Dificultad: DIFÍCIL

Enunciado: Escribe un programa que imprima los 50 primeros números de la sucesión de Fibonacci empezando en 0.
La serie Fibonacci se compone por una sucesión de números en la que el siguiente siempre es la suma de los dos anteriores.
0, 1, 1, 2, 3, 5, 8, 13...

 """

def sucesion_fibonacci():
    num_ant = 0
    num_actual = 1
    for i in range(50):
        print(num_ant)
        siguiente = num_ant + num_actual
        num_ant = num_actual
        num_actual =siguiente

sucesion_fibonacci()

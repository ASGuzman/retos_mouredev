"""
Reto #4
  ÁREA DE UN POLÍGONO
  Dificultad: FÁCIL
 
 Enunciado: Crea UNA ÚNICA FUNCIÓN (importante que sólo sea una) que sea capaz de calcular y retornar el área de un polígono.
 - La función recibirá por parámetro sólo UN polígono a la vez.
 - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 - Imprime el cálculo del área de un polígono de cada tipo.

"""

def AreaPoligono(tipo_poligono: str, base: float = None, alt: float = None, lado: float = None) -> float:
    if tipo_poligono == "Rectangulo":
        if base is not None and alt is not None:
            area = base * alt
            print(f"Área del Rectángulo: {area}")
        else:
            print("Por favor, proporciona la base y la altura para el Rectángulo.")
    
    elif tipo_poligono == "Cuadrado":
        if lado is not None:
            area = lado * lado
            print(f"Área del Cuadrado: {area}")
        else:
            print("Por favor, proporciona el lado para el Cuadrado.")

    elif tipo_poligono == "Triangulo":
        if base is not None and alt is not None:
            area = 1/2 * base * alt
            print(f"Área del Triángulo: {area}")
        else:
            print("Por favor, proporciona la base y la altura para el Triángulo.")

    else:
        print("Tipo de polígono incorrecto.")


AreaPoligono("Cuadrado",lado=5)
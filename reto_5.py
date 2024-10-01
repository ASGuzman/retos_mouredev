"""
Reto #5
ASPECT RATIO DE UNA IMAGEN
Dificultad: DIFÍCIL

Enunciado: Crea un programa que se encargue de calcular el aspect ratio de una imagen a partir de una url.
- Nota: Esta prueba no se puede resolver con el playground online de Kotlin. Se necesita Android Studio.
- Url de ejemplo: https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png
- Por ratio hacemos referencia por ejemplo a los "16:9" de una imagen de 1920*1080px.

"""

import requests  #Importa la biblioteca requests, que se utiliza para hacer solicitudes HTTP, permitiéndonos obtener datos de una URL.
from PIL import Image #Importa la clase Image de la biblioteca Pillow (PIL). Esta biblioteca se utiliza para abrir, manipular y guardar imágenes en varios formatos
from io import BytesIO # Importa BytesIO, que es una clase de la biblioteca io que permite manejar datos binarios en memoria como si fueran un archivo. Esto es útil para abrir imágenes directamente desde bytes.
from threading import Thread #Importa la clase Thread que se utiliza para crear hilos de ejecución. Esto nos permite realizar operaciones en segundo plano, como descargar la imagen sin bloquear el resto del programa.
from math import isclose, floor #Importa las funciones isclose (para comparar números en punto flotante con una tolerancia) y floor (para redondear hacia abajo), aunque en este caso solo isclose se utiliza.

class Challenge5:  #Una clase es un modelo para crear objetos que encapsulan datos y funciones.

    def aspect_ratio(self, url: str): #Define un método llamado aspect_ratio que acepta una URL como argumento. self es una referencia al objeto actual de la clase.
        thread = Thread(target=self._calculate_aspect_ratio, args=(url,)) #Crea un nuevo hilo (Thread). El target especifica que el hilo ejecutará el método _calculate_aspect_ratio, y args pasa la URL como argumento a ese método.
        thread.start() #Inicia la ejecución del hilo. Esto ejecutará el método _calculate_aspect_ratio en segundo plano, permitiendo que el programa principal siga funcionando.

    def _calculate_aspect_ratio(self, url: str):
        aspect_ratio_str = None  #Inicializa una variable aspect_ratio_str que se utilizará para almacenar la cadena del aspecto ratio.
        
        try:
            # Obtener la imagen desde la URL
            response = requests.get(url)  #Hace una solicitud GET a la URL proporcionada. response contendrá la respuesta del servidor, incluyendo los datos de la imagen.
            image = Image.open(BytesIO(response.content))  #Convierte el contenido de la respuesta (los bytes de la imagen) en un objeto BytesIO, y luego abre la imagen usando PIL. Esto permite trabajar con la imagen en memoria.
            
            height = image.height
            width = image.width
            aspect_ratio = self.rational_aspect_ratio(height / width) #Llama al método rational_aspect_ratio, pasando la relación de aspecto (altura/anchura) como argumento. Este método calculará el aspecto racional de la relación.
            aspect_ratio_str = f"{aspect_ratio[1]}:{aspect_ratio[0]}" #Formatea la cadena para mostrar el aspecto ratio como "ancho". aspect_ratio es una tupla donde el primer elemento es la altura y el segundo la anchura.
            
            print(f"El aspect ratio es {aspect_ratio_str}")
        except Exception as e:
            print("No se ha podido calcular el aspect ratio:", e)

    def rational_aspect_ratio(self, aspect_ratio: float):  #Define un método que calcula la representación racional del aspecto ratio, a partir de un número decimal.
        precision = 1.0E-6
        x = aspect_ratio
        a = round(x)
        q = (1, 0, a, 1)  # (h1, k1, h, k)

        while not isclose(x, a, abs_tol=precision * q[3] ** 2):
            x = 1.0 / (x - a)
            a = round(x)
            q = (q[2], q[3], q[0] + a * q[2], q[1] + a * q[3])
        
        return (q[2], q[3])  # Retornar (h, k)

# Ejemplo de uso
challenge = Challenge5()
url_imagen = "https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png"
challenge.aspect_ratio(url_imagen)

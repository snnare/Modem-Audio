import numpy as np

def prueba(txt):
    print("Cargando.... ", txt)

while True:
    texto = input("Ingresa un texto (presiona 'q' para salir): ")
    if texto.lower() == 'q':
        break
    else:
        # Hacer algo con el texto ingresado
        #print("Texto ingresado:", texto)
        prueba(texto)
        pass

print("Adios")
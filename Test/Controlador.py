class Controlador:
    def __init__(self):
        self.mensaje("")

    def mensaje(self, mensaje):
        print(mensaje)

x =  Controlador()
x.mensaje("Hola")
import tkinter as tk 
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from Controlador.Transmisor_FSK import Transmitir
import os
import sounddevice as sd




# Funcion para abrir archivos (txt,  bin)
def openFile():
     File = filedialog.askopenfile(mode = 'r', 
                                   title="Seleccione el archivo",  
                                   initialdir="C:/", 
                                   filetypes=(("Archivos de Texto", "*.txt"),
                                   ("Archivos Binarios","*.bin")))
     if File:
          PATH = os.path.abspath(File.name)
     with open(PATH) as file_object:
          leer = file_object.read()
          print(leer)


def agregar_texto():
    texto = entrada_texto.get()  # Obtener el texto de la caja de entrada
    area_texto.insert(tk.END, "Tu:"+texto + "\n")  # Agregar el texto al área de texto


# Envia el mensaje usando FSK
def send_message():
    tx = Transmitir(space_freq=1000, mark_freq=2000, baud=4, sample_rate=44100)
    # signal = tx.transmisor.transmit_text(entrada_texto.get())
    # print(signal)

    sd.play(signal,44100)
    sd.wait()

# Centrar pantall
def center_window(root):
    # Obtener el ancho y alto de la pantalla
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calcular las coordenadas para centrar la ventana
    window_width = 500  # Ancho de la ventana
    window_height = 600  # Alto de la ventana
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    # Establecer la geometría de la ventana para centrarla
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")


    
root = tk.Tk()
root.title("Proyecto Chat")
center_window(root)
root.resizable(False, False)

# Estilo visual
style = ttk.Style()
style.configure('TButton', font=('Arial', 12), padding=5)
style.configure('TEntry', font=('Arial', 12), padding=5)
style.configure('TText', font=('Arial', 12), padding=5)


# Area visualización de Texto
area_texto = tk.Text(root, wrap='word')
area_texto.pack(fill='both', expand=True, padx=10, pady=10)

# Crear la caja de entrada para escribir el texto
entrada_texto = ttk.Entry(root)
entrada_texto.pack(padx=10, pady=5, fill='x')

# Crear el botón para agregar texto
boton_agregar = ttk.Button(root, text="Enviar", command=agregar_texto)
boton_agregar.pack(padx=10, pady=5, fill='x')

# Crear el botón para adjuntar archivo
boton_adjuntar = ttk.Button(root, text="Adjuntar Archivo", command=openFile)
boton_adjuntar.pack(padx=10, pady=5, fill='x')


root.mainloop()

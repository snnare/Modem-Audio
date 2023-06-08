import tkinter as tk
from tkinter import filedialog
import os

root = tk.Tk()
root.geometry("400x400")



def openFile():
     File = filedialog.askopenfile(mode = 'r', 
                                   title="Seleccione el archivo",  
                                   initialdir="C:/", 
                                   filetypes=(("Archivos de Texto", "*.txt"),
                                   ("Archivos Binarios","*.bin")))
     if File:
          PATH = os.path.abspath(File.name)
    

     #print(File)
     with open(PATH) as file_object:
          leer = file_object.read()
          print(leer)




adjuntar = tk.Button(root, text = "Open", command= openFile)
adjuntar.pack()


root.mainloop()
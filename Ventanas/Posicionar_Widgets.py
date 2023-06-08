import tkinter as tk

root = tk.Tk()
root.geometry("400x300")
root.title("Posicionamiento con GRID")

btn1 = tk.Button(root, text="Boton 1", width=10, height= 5)
btn2 = tk.Button(root, text="Boton 2", width=10, height= 5)
btn3 = tk.Button(root, text="Boton 3", width=10, height= 5)


btn1.grid(row= 0 , column= 0)
btn2.grid(row=1, column= 2)


root.mainloop()
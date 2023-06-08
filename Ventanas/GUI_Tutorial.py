import tkinter as tk

root = tk.Tk()
root.geometry('400x400')


txtField = tk.Entry(root, font="Helvetica 16")
txtField.pack()

def getText():
    prubea = txtField.get()
    print("Hola ", prubea)
button1 = tk.Button(root, text="click", command=getText)
button1.pack()

root.mainloop()

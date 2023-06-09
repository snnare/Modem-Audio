import tkinter as tk

root = tk.Tk()
root.geometry('500x400')
root.resizable(False, False)
root.title('Tkinter Hub')
root.eval('tk::PlaceWindow . center')

options_frame = tk.Frame(root, bg='#c3c3c3')

def home_page():
    home_frame = tk.Frame(main_frame)

    lb = tk.Label(home_frame, text='Home Page')
    lb.pack()

    home_frame.pack(pady=20
                    )


# Boton de Ventana 1
home_btn =  tk.Button(options_frame, 
                      text='Home', 
                      font=('Bold', 15),
                      fg="#158aff", 
                      bd=0,
                      bg='#c3c3c3',
                      command = home_page)

home_btn.place(x=10, y=10)


# Boton de Ventana 2
menu_btn =  tk.Button(options_frame, 
                      text='Menu', 
                      font=('Bold', 15),
                      fg="#158aff", 
                      bd=0,
                      bg='#c3c3c3')

menu_btn.place(x=10, y=50)



options_frame.pack(side=tk.LEFT)
options_frame.pack_propagate(False)
options_frame.configure(width=100, height=400)


main_frame = tk.Frame(root, 
                      highlightbackground='black',
                      highlightthickness=2)
main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)
main_frame.configure(height=400, width=500)



root.mainloop()
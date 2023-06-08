import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk

def adjuntar_archivo():
    global archivo_adjunto
    archivo = filedialog.askopenfilename()
    if archivo:
        archivo_adjunto = archivo
        # Mostrar el nombre del archivo en el área de chat
        nombre_archivo = archivo.split("/")[-1]
        area_chat.config(state=tk.NORMAL)
        area_chat.insert(tk.END, "Adjunto: " + nombre_archivo + "\n")
        area_chat.config(state=tk.DISABLED)
        print("Archivo adjuntado:", archivo)
        boton_enviar.config(state=tk.NORMAL)  # Habilitar el botón de enviar después de adjuntar el archivo

def enviar_mensaje():
    global archivo_adjunto
    mensaje = entrada_texto.get("1.0", "end-1c")
    if not mensaje and not archivo_adjunto:
        messagebox.showerror("Error", "No se ha enviado ningún mensaje y/o adjuntado ningún archivo")
        return

    # Mostrar el mensaje en el área de chat
    area_chat.config(state=tk.NORMAL)
    if mensaje:
        area_chat.insert(tk.END, "Yo: " + mensaje + "\n")
    if archivo_adjunto:
        nombre_archivo = archivo_adjunto.split("/")[-1]
        area_chat.insert(tk.END, "Adjunto: " + nombre_archivo + "\n")
        area_chat.insert(tk.END, "Archivo enviado\n")  # Mostrar "Archivo enviado" en el área del chat
        archivo_adjunto = ""  # Reiniciar el archivo adjunto después de enviarlo
    area_chat.config(state=tk.DISABLED)

    entrada_texto.delete("1.0", tk.END)

ventana = tk.Tk()
ventana.title("Chat")

# Obtener dimensiones de la pantalla
screen_width = ventana.winfo_screenwidth()
screen_height = ventana.winfo_screenheight()

# Calcular posición x e y para centrar la ventana
x = (screen_width - 600) // 2
y = (screen_height - 600) // 2

ventana.geometry(f"600x600+{x}+{y}")

# Marco para el área del chat
marco_chat = tk.Frame(ventana)
marco_chat.pack(fill=tk.BOTH, expand=True)

# Campo de desplazamiento para el chat
scroll_chat = tk.Scrollbar(marco_chat)
scroll_chat.pack(side=tk.RIGHT, fill=tk.Y)

# Área de texto para mostrar el chat
area_chat = tk.Text(marco_chat, yscrollcommand=scroll_chat.set)
area_chat.pack(fill=tk.BOTH, expand=True)
scroll_chat.config(command=area_chat.yview)

# Deshabilitar edición en el área de chat
area_chat.config(state=tk.DISABLED)

# Campo de entrada de texto
entrada_texto = tk.Text(ventana, height=3)
entrada_texto.pack(fill=tk.X, padx=10, pady=10)

# Botón de adjuntar archivo
#imagen_adjuntar = tk.PhotoImage(file="clip_icon.png").subsample(10, 10)  # Redimensionar a 10x10 píxeles
boton_adjuntar = tk.Button(ventana, command=adjuntar_archivo, borderwidth=0, highlightthickness=0)
boton_adjuntar.pack(side=tk.LEFT, padx=10)

# Botón de enviar mensaje con ícono
#imagen_enviar = tk.PhotoImage(file="enviar_icon.png").subsample(10, 10)  # Redimensionar a la mitad del tamaño original
boton_enviar = ttk.Button(ventana, command=enviar_mensaje, style='TButton')
boton_enviar.pack(side=tk.RIGHT, padx=10)

archivo_adjunto = ""

ventana.mainloop()
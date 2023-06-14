import tkinter as tk
from tkinter import ttk, filedialog


class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Menú Lateral")
        self.geometry("400x300")

        # Estilo para el menú lateral
        estilo_menu = ttk.Style()
        estilo_menu.configure("EstiloMenu.TFrame", background="#f1f1f1")

        # Estilo para los botones del menú
        estilo_botones = ttk.Style()
        estilo_botones.configure(
            "EstiloBotones.TButton",
            background="#b0bec5",
            foreground="#ffffff",
            font=("Arial", 12, "bold"),
            width=10,
        )

        # Estilo para los labels
        estilo_labels = ttk.Style()
        estilo_labels.configure("EstiloLabels.TLabel", background="#ffffff", font=("Arial", 12))

        # Contenedor principal
        self.contenedor = ttk.Frame(self)
        self.contenedor.pack(side="top", fill="both", expand=True)

        # Menú lateral
        self.menu_lateral = ttk.Frame(self.contenedor, style="EstiloMenu.TFrame", width=100)
        self.menu_lateral.pack(side="left", fill="y")

        # Botones del menú
        self.btn_home = ttk.Button(self.menu_lateral, text="Home", style="EstiloBotones.TButton", command=self.mostrar_home)
        self.btn_menu = ttk.Button(self.menu_lateral, text="Menu", style="EstiloBotones.TButton", command=self.mostrar_menu)

        self.btn_home.pack(pady=10)
        self.btn_menu.pack(pady=10)

        # Contenedor de la ventana actual
        self.ventana_actual = None
        self.mostrar_home()

    def mostrar_home(self):
        if self.ventana_actual is not None:
            self.ventana_actual.destroy()

        self.ventana_actual = ttk.Frame(self.contenedor)
        self.ventana_actual.pack(fill="both", expand=True)

        # Botón para abrir el explorador de archivos
        btn_cargar_archivo = ttk.Button(self.ventana_actual, text="Cargar Archivo", command=self.abrir_archivo)
        btn_cargar_archivo.pack(pady=10)

        # Etiqueta para mostrar el contenido del archivo
        self.lbl_contenido_archivo = ttk.Label(self.ventana_actual, text="Contenido del archivo:", style="EstiloLabels.TLabel")
        self.lbl_contenido_archivo.pack(pady=10)

        # Campo de entrada para escribir texto
        self.entry_texto = tk.Entry(self.ventana_actual)
        self.entry_texto.pack(pady=10)
        self.entry_texto.bind("<Return>", self.mostrar_texto)

        # Etiqueta para mostrar el texto ingresado
        self.lbl_texto = ttk.Label(self.ventana_actual, text="Texto ingresado:", style="EstiloLabels.TLabel")
        self.lbl_texto.pack(pady=10)

    def abrir_archivo(self):
        archivo = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])
        if archivo:
            with open(archivo, "r") as file:
                contenido = file.read()
                self.lbl_contenido_archivo.config(text="Contenido del archivo:\n" + contenido)

    def mostrar_texto(self, event):
        texto = self.entry_texto.get()
        self.lbl_texto.config(text="Texto ingresado:\n" + texto)


ventana = VentanaPrincipal()
ventana.mainloop()

"""             Importación de Módulos           """

import customtkinter
from tkinter import ttk
from .vista_inventarios import AgregarInventarioVentana

class PanelInventario(customtkinter.CTkFrame):
    
    """ Panel que mostrará los inventarios a ver """
    
    def __init__(self, padre, volver_func):
        super().__init__(padre) # , fg_color="#ecf0f1" , fg_color="#ecf0f1"
        
        # Configurar el grid principal 
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)  # Añadir una fila más para el botón

        # Menú de opciones 
        self.combobox = customtkinter.CTkOptionMenu(self,
                                                    values=["option 1", "option 2"],
                                                    command=self.llamar_menu_opciones)
        self.combobox.grid(row=0, column=0, sticky="nw", padx=10, pady=10)
        self.combobox.set("option 1")  # Set initial value

        # Mostrar el panel
        self.mostrar_panel()
        
        # Botón para agregar inventario
        self.boton_agregar_inventario = customtkinter.CTkButton(self, text="Agregar Inventarios",
                                                                width=100, height=32,
                                                                command=self.abrir_agregar_inventario)
        
        self.boton_agregar_inventario.grid(row=2, column=0, sticky="sw", padx=10, pady=10)
        
        # Botón para subir inventario
        self.boton_subir_inventario = customtkinter.CTkButton(self, text="Subir Inventario",
                                                              width=100, height=32,
                                                              command = self.cargar_archivo)
        
        self.boton_subir_inventario.grid(row=2, column=0, sticky="s", padx=10, pady=10)

        # Botón para volver a la vista principal en la esquina inferior derecha
        self.boton_volver = customtkinter.CTkButton(self, text="Volver", command=volver_func,
                                                    width=100, height=32)
        self.boton_volver.grid(row=2, column=0, sticky="se", padx=10, pady=10)
        
    def llamar_menu_opciones(self, elegir):
        
        """ función que va a manejar las opciones de elegir los inventarios """
        print(f"Option selected: {elegir}")

    def mostrar_panel(self):
        """ Función que muestra el panel """
        label_titulo = customtkinter.CTkLabel(self, text="Bienvenidos a Panel de Inventarios",
                                              font=("Arial", 24), text_color="#021b2b")
        label_titulo.grid(row=0, column=0, pady=20, sticky="n")  

        # Ejemplo como se verán las tablas cuando se consulten los inventarios 
        datos = [
            ("Item 1", "Descripción 1", 10),
            ("Item 2", "Descripción 2", 20),
            ("Item 3", "Descripción 3", 30)
        ]

        arbol = ttk.Treeview(self, columns=("Item", "Descripción", "Cantidad"), show="headings")
        arbol.heading("Item", text="Item")
        arbol.heading("Descripción", text="Descripción")
        arbol.heading("Cantidad", text="Cantidad")
        arbol.grid(row=1, column=0, sticky="nsew")  

        for item in datos:
            arbol.insert("", "end", values=item)
    
    def abrir_agregar_inventario(self):
        """ Función para abrir la ventana de agregar inventario """
        ventana = AgregarInventarioVentana(self)
        ventana.lift()
        ventana.focus_set()

    def cargar_archivo(self):
        
        """         Funsión para cargar archivos excel          """
        print("esto se esta cargando")
        
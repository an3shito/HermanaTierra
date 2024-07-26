"""          Importación de Módulos      """

import customtkinter
from inventarios.consultas_inventario import ConsultasInventarios
from inventarios.consultas_cardex import ConsultasCardex

class DashBoardPrincipal(customtkinter.CTkFrame):
    """Clase que representa la vista principal"""

    def __init__(self, master, mostrar_principal):
        super().__init__(master)
        self.mostrar_principal = mostrar_principal
        self.consulta_inventario = None
        self._configurar_interfaz()

    def _configurar_interfaz(self):
        # Configurar el layout con un menú lateral y un área principal
        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=5)
        self.rowconfigure(0, weight=1)
        
        # Menú lateral
        self.menu_frame = customtkinter.CTkFrame(self, width=200, corner_radius=0)
        self.menu_frame.grid(row=0, column=0, sticky="nsw")
        
        # Configurar el grid del menú lateral
        for i in range(6):
            self.menu_frame.rowconfigure(i, weight=0)
        self.menu_frame.rowconfigure(6, weight=1)
        
        # Etiqueta del menú
        self.label_menu = customtkinter.CTkLabel(self.menu_frame, text="Menú", font=("Arial", 20))
        self.label_menu.grid(row=0, column=0, pady=20, padx=10)
        
        # Botones del menú
        self.boton_inventario = customtkinter.CTkButton(self.menu_frame, text="Inventario", command=self.mostrar_inventario)
        self.boton_inventario.grid(row=1, column=0, pady=10, padx=20, sticky="ew")
        
        self.boton_bodega = customtkinter.CTkButton(self.menu_frame, text="Bodega", command=self.mostrar_bodega)
        self.boton_bodega.grid(row=2, column=0, pady=10, padx=20, sticky="ew")
        
        self.boton_cardex = customtkinter.CTkButton(self.menu_frame, text="Cardex", command=self.mostrar_bodega)
        self.boton_cardex.grid(row=3, column=0, pady=10, padx=20, sticky="ew")
        
        self.boton_salir = customtkinter.CTkButton(self.menu_frame, text="Salir", command=self.mostrar_principal)
        self.boton_salir.grid(row=6, column=0, pady=10, padx=20, sticky="s")
        
        # Área principal
        self.area_principal = customtkinter.CTkFrame(self)
        self.area_principal.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        
        # Configurar el grid del área principal
        self.area_principal.columnconfigure(0, weight=1)
        self.area_principal.rowconfigure(0, weight=1)
        
        # Etiqueta de bienvenida en el área principal
        self.label_bienvenida = customtkinter.CTkLabel(self.area_principal, text="Bienvenido al Dashboard de Hermana Tierra", font=("Arial", 24))
        self.label_bienvenida.grid(row=0, column=0, padx=20, pady=20, sticky="n")

    def mostrar_inventario(self):
        """  funcion que mostrara las elecciones de inventario """
        # Limpiar el área principal
        for widget in self.area_principal.winfo_children():
            widget.destroy()
        
        # Crear una instancia de ConsultasInventarios y mostrarla en el área principal
        self.consulta_inventario = ConsultasInventarios(self.area_principal)
        self.consulta_inventario.grid(row=0, column=0, sticky="nsew")
    
    def mostrar_bodega(self):
        """  funcion que mostrara las elecciones de bodega """
        # Limpiar el área principal
        for widget in self.area_principal.winfo_children():
            widget.destroy()
        
         # Crear una instancia de ConsultasInventarios y mostrarla en el área principal
        self.consulta_cardex = ConsultasCardex(self.area_principal)
        self.consulta_cardex.grid(row=0, column=0, sticky="nsew")

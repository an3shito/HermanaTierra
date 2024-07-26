"""          Importación de Módulos      """

import customtkinter
from inventarios.inventario_utilesOf import UtilesDeOficinas

class ConsultasInventarios(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
         # Configurar el grid principal
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        
        # Menú de opciones para agregar datos a los tipos de inventarios 
        self.combobox = customtkinter.CTkOptionMenu(self,
                                                    values=["1. Inventario de Utiles", "2. Inventario de Servicios", "3. Inventario de Medicina"],
                                                    command=self.llamar_inventario_opciones)
        self.combobox.grid(row=0, column=0, sticky="nw", padx=10, pady=10)
        self.combobox.set("Elige una Opción")  # valor inicial 
        
        # Frame para mostrar el contenido del inventario
        self.content_frame = customtkinter.CTkFrame(self, fg_color="#3b3b3b", corner_radius=10)
        self.content_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        self.content_frame.grid_columnconfigure(0, weight=1)
        self.content_frame.grid_rowconfigure(0, weight=1)

    def llamar_inventario_opciones(self, elegir):
        """ Función que va a manejar las opciones de elegir los inventarios """
        
        print(f"Option selected: {elegir}")
        
        # Limpiar el frame de contenido antes de mostrar uno nuevo
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        if elegir == "1. Inventario de Utiles":
            inventario_utiles_frame = UtilesDeOficinas(self.content_frame)
            inventario_utiles_frame.grid(row=0, column=0, sticky="nsew")
        elif elegir == "2. Inventario de Servicios":
            pass

""" Módudulos """

import customtkinter

class InventarioUtilesOficina(customtkinter.CTkFrame):
    """ Representa la vista del inventario de utiles de oficina """
    def __init__(self, master, regresar_callback):
        super().__init__(master, fg_color="#fff5e1")
        
        self.regresar_callback = regresar_callback
        
        # Configurar el grid dentro del frame
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        
        # Crear los elementos de la vista de inventario
        self.label_inventario = customtkinter.CTkLabel(self, text="Vista de Inventario de Útiles de Oficina", text_color="#3b3b3b", font=("Arial", 16))
        self.label_inventario.grid(column=0, row=0, padx=10, pady=10)
        
        self.boton_regresar = customtkinter.CTkButton(self, text="Regresar", width=120, height=32, fg_color="#d9534f", command=self.regresar_callback)
        self.boton_regresar.grid(column=0, row=1, padx=10, pady=10)
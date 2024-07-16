"""          Importación de Módulos      """
import customtkinter

class InventarioMedicinas(customtkinter.CTkFrame):
    
    """ Clase que refresenta el formulario de medicinas """
    def __init__(self, master):
        
        super().__init__(master, fg_color="#fff5e1")
        
        # Configurar el grid dentro del frame
        
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)
        for i in range(9):
            self.rowconfigure(i, weight=1)
        
        # Crear los elementos de la vista de inventario
        self.label_inventario = customtkinter.CTkLabel(self, text="Inventario de Medicinas", 
                                                       text_color="#3b3b3b", font=("Arial", 16))
        self.label_inventario.grid(column=1, row=0, columnspan=2, padx=10, pady=10, sticky="w")
        
        # Campos del formulario
        
        self.label_nombre_suministro = customtkinter.CTkLabel(self, text="Nombre Suministro", text_color="#3b3b3b", font=("Arial", 12))
        self.label_nombre_suministro.grid(column=0, row=1, padx=10, pady=5, sticky="e")
        self.entry_nombre_suministro = customtkinter.CTkEntry(self, fg_color="#E8A023")
        self.entry_nombre_suministro.grid(column=1, row=1, padx=10, pady=5, sticky="ew")
        
        self.label_presentacion = customtkinter.CTkLabel(self, text="Presentación", text_color="#3b3b3b", font=("Arial", 12))
        self.label_presentacion.grid(column=0, row=2, padx=10, pady=5, sticky="e")
        self.entry_presentacion = customtkinter.CTkEntry(self)
        self.entry_presentacion.grid(column=1, row=2, padx=10, pady=5, sticky="ew")
        
        self.label_lote = customtkinter.CTkLabel(self, text="Lote", text_color="#3b3b3b", font=("Arial", 12))
        self.label_lote.grid(column=0, row=3, padx=10, pady=5, sticky="e")
        self.entry_lote = customtkinter.CTkEntry(self)
        self.entry_lote.grid(column=1, row=3, padx=10, pady=5, sticky="ew")
        
        self.label_fv = customtkinter.CTkLabel(self, text="F/V", text_color="#3b3b3b", font=("Arial", 12))
        self.label_fv.grid(column=0, row=4, padx=10, pady=5, sticky="e")
        self.entry_fv = customtkinter.CTkEntry(self)
        self.entry_fv.grid(column=1, row=4, padx=10, pady=5, sticky="ew")
        
        self.label_cantidad = customtkinter.CTkLabel(self, text="Cantidad", text_color="#3b3b3b", font=("Arial", 12))
        self.label_cantidad.grid(column=0, row=5, padx=10, pady=5, sticky="e")
        self.entry_cantidad = customtkinter.CTkEntry(self)
        self.entry_cantidad.grid(column=1, row=5, padx=10, pady=5, sticky="ew")
        
        self.label_precio = customtkinter.CTkLabel(self, text="Precio", text_color="#3b3b3b", font=("Arial", 12))
        self.label_precio.grid(column=0, row=6, padx=10, pady=5, sticky="e")
        self.entry_precio = customtkinter.CTkEntry(self)
        self.entry_precio.grid(column=1, row=6, padx=10, pady=5, sticky="ew")
        
        self.label_total = customtkinter.CTkLabel(self, text="Total", text_color="#3b3b3b", font=("Arial", 12))
        self.label_total.grid(column=0, row=7, padx=10, pady=5, sticky="e")
        self.entry_total = customtkinter.CTkEntry(self)
        self.entry_total.grid(column=1, row=7, padx=10, pady=5, sticky="ew")
        
        # Agregar botones 
        
        self.boton_agregar = customtkinter.CTkButton(self, text="Agregar", width=120, height=32)
        self.boton_agregar.grid(column=0, row=8, padx=10, pady=10, sticky="ew")
        
        self.boton_eliminar = customtkinter.CTkButton(self, text="Eliminar", width=120, height=32)
        self.boton_eliminar.grid(column=1, row=8, padx=10, pady=10, sticky="ew")
        
        self.boton_buscar = customtkinter.CTkButton(self, text="Buscar", width=120, height=32)
        self.boton_buscar.grid(column=2, row=8, padx=10, pady=10, sticky="ew")
      
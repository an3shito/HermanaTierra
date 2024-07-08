import customtkinter
from inventarios.inventario_utiles_oficina import InventarioUtilesOficina

class MainApp(customtkinter.CTk):
    """ Representa la vista principal """
    
    def __init__(self):
        super().__init__()
        
        self.title("Hermana Tierra")
        self.resizable(0, 0)
        self.config(bg="#1b676b")
        
        # Dimensiones iniciales de la ventana
        self.ancho_ventana = 320
        self.altura_ventana = 420
        self._configurar_geometria(self.ancho_ventana, self.altura_ventana)
        
        # Colocar frame que irá en el centro para visualizar los botones de opciones
        self.frame = customtkinter.CTkFrame(self, fg_color="#519548")
        self.frame.grid(column=0, row=0, sticky="nsew", padx=50, pady=50)
        
        # Configurar el grid dentro del frame
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=1)
        self.frame.rowconfigure(1, weight=1)
        self.frame.rowconfigure(2, weight=1)
        self.frame.rowconfigure(3, weight=1)
        
        # Crear los botones y posicionarlos en el grid del frame
        self.boton_inventario = customtkinter.CTkButton(self.frame, text="Inventarios", width=120, height=32, command=self.mostrar_inventario)
        self.boton_inventario.grid(column=0, row=1, padx=10, pady=10)
        
        self.boton_bodega = customtkinter.CTkButton(self.frame, text="Bodega", width=120, height=32)
        self.boton_bodega.grid(column=0, row=2, padx=10, pady=10)
        
        self.boton_carro = customtkinter.CTkButton(self.frame, text="Carro", width=120, height=32)
        self.boton_carro.grid(column=0, row=3, padx=10, pady=10)
        
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        
    def _configurar_geometria(self, ancho, altura):
        """Configura la geometría de la ventana y la centra en la pantalla."""
        ancho_pantalla = self.winfo_screenwidth()
        altura_pantalla = self.winfo_screenheight()
        posicion_x = (ancho_pantalla // 2) - (ancho // 2)
        posicion_y = (altura_pantalla // 2) - (altura // 2)
        self.geometry(f'{ancho}x{altura}+{posicion_x}+{posicion_y}')
    
    def mostrar_inventario(self):
        # Ocultar los botones principales y el frame
        self.frame.grid_forget()
        
        # Cambiar el tamaño de la ventana
        self.ancho_ventana_inventario = 640
        self.altura_ventana_inventario = 480
        self._configurar_geometria(self.ancho_ventana_inventario, self.altura_ventana_inventario)
        
        # Crear y mostrar la vista de inventario
        self.inventario_view = InventarioUtilesOficina(self, self.mostrar_principal)
        self.inventario_view.grid(column=0, row=0, sticky="nsew")
    
    def mostrar_principal(self):
        # Ocultar la vista de inventario
        self.inventario_view.grid_forget()
        
        # Cambiar el tamaño de la ventana de nuevo al tamaño original
        self._configurar_geometria(self.ancho_ventana, self.altura_ventana)
        
        # Mostrar el frame principal y los botones
        self.frame.grid(column=0, row=0, sticky="nsew", padx=50, pady=50)
        
if __name__ == "__main__":       
    app = MainApp()
    app.mainloop()

"""          Importación de Módulos      """

import customtkinter
from inventarios.panel_inventarios import PanelInventario
from inventarios.dashboard import DashBoardPrincipal
from bodega.panel_bodega import PanelBodega


class MainApp(customtkinter.CTk):
    
    """ Representa la vista principal """
    
    def __init__(self):
        super().__init__()
        
        self.title("Hermana Tierra")
        #self.resizable(0, 0)
        
        # Dimensiones iniciales de la ventana
        self.ancho_ventana = 320
        self.altura_ventana = 400
        self.ancho_ventana_inventario = 840
        self.altura_ventana_inventario = 580
        self.ancho_ventana_bodega = 840
        self.altura_ventana_bodega = 580
        
        # Dimensiones para el frame del dashboard 
        self.ancho_dashboard = 1350
        self.altura_dashboard = 620
                
        self._configurar_geometria(self.ancho_ventana, self.altura_ventana)
        
        # Colocar frame que irá en el centro para visualizar los botones de opciones
        self.frame = customtkinter.CTkFrame(self)
        self.frame.grid(column=0, row=0, sticky="nsew", padx=50, pady=50)
        
        # Configurar el grid dentro del frame
        self.frame.columnconfigure(0, weight=1)
        for i in range(4):
            self.frame.rowconfigure(i, weight=1)
        
        # Crear los botones y posicionarlos en el grid del frame
        self.boton_inventario = customtkinter.CTkButton(self.frame, text="Inventarios", 
                                                        width=120, height=32, command=self.mostrar_inventario)
        self.boton_inventario.grid(column=0, row=1, padx=10, pady=10)
        
        self.boton_bodega = customtkinter.CTkButton(self.frame, text="Ingresar", 
                                                    width=120, height=32, command= self.mostrar_dashboard)
        self.boton_bodega.grid(column=0, row=2, padx=10, pady=10)
        
        self.boton_carro = customtkinter.CTkButton(self.frame, text="Cardex", width=120, height=32)
        self.boton_carro.grid(column=0, row=3, padx=10, pady=10)
        
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        
        # Inicializar inventario_view como None
        self.inventario_view = None
        self.bodega_view = None
        self.dashboard_view = None
        
    def _configurar_geometria(self, ancho, altura):
        
        """   Función que configura la geometría de la ventana y la centra en la pantalla.   """
        
        ancho_pantalla = self.winfo_screenwidth()
        altura_pantalla = self.winfo_screenheight()
        posicion_x = (ancho_pantalla // 2) - (ancho // 2)
        posicion_y = (altura_pantalla // 2) - (altura // 2)
        self.geometry(f'{ancho}x{altura}+{posicion_x}+{posicion_y}')
    
    def mostrar_inventario(self):
        
        """ Función que muestra el panel del inventario """
        
        # Ocultar los botones principales y el frame
        self.frame.grid_forget()
        
        # Cambiar el tamaño de la ventana
        self._configurar_geometria(self.ancho_ventana_inventario, self.altura_ventana_inventario)
        
        # Crear y mostrar la vista de inventario
        self.inventario_view = PanelInventario(self, self.mostrar_principal)
        self.inventario_view.grid(column=0, row=0, sticky="nsew")
    
    def mostrar_bodega(self):
        """    Función que mostrará la ventana de bodega   """
        
        # Ocultar los botones principales y el frame
        self.frame.grid_forget()
        
        # Cambiar el tamaño de la ventana
        self._configurar_geometria(self.ancho_ventana_bodega, self.altura_ventana_bodega)
        
        # Crear y mostrar la vista de bodega
        self.bodega_view = PanelBodega(self, self.mostrar_principal)
        self.bodega_view.grid(column=0, row=0, sticky="nsew")
    
    def mostrar_dashboard(self):
        """ Función que mostrará la ventana de bodega """
    
        # Ocultar los botones principales y el frame
        self.frame.grid_forget()
    
        # Cambiar el tamaño de la ventana
        self._configurar_geometria(self.ancho_dashboard, self.altura_dashboard)
    
        # Crear y mostrar la vista del dashboard
        self.dashboard_view = DashBoardPrincipal(self, self.mostrar_principal)
        self.dashboard_view.grid(column=0, row=0, sticky="nsew")
     
            
    def mostrar_principal(self):
        
        """ Función que muestra el panel principal """
        
        # Ocultar la vista de inventario o bodega
        if self.inventario_view:
            self.inventario_view.grid_forget()
            self.inventario_view.destroy()  
            self.inventario_view = None
        if self.bodega_view:
            self.bodega_view.grid_forget()
            self.bodega_view.destroy()  
            self.bodega_view = None
        if self.dashboard_view:
            self.dashboard_view.grid_forget()
            self.dashboard_view.destroy()  
            self.dashboard_view = None
            
        # Cambiar el tamaño de la ventana de nuevo al tamaño original
        self._configurar_geometria(self.ancho_ventana, self.altura_ventana)
        
        # Mostrar el frame principal y los botones
        self.frame.grid(column=0, row=0, sticky="nsew", padx=50, pady=50)
        
if __name__ == "__main__":
           
    app = MainApp()
    app.mainloop()

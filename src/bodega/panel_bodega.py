
import customtkinter


class PanelBodega(customtkinter.CTkFrame):
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
        
        # Botón para compras de fondos de ministerio
        self.boton_compras_fm = customtkinter.CTkButton(self, text="Compras Fondos Ministerio",
                                                                width=100, height=32,
                                                                )
        
        self.boton_compras_fm.grid(row=2, column=0, sticky="sw", padx=10, pady=10)
        
        # Botón para ver donaciones
        self.boton_donaciones = customtkinter.CTkButton(self, text="Donaciones",
                                                              width=100, height=32,
                                                              )
        
        self.boton_donaciones.grid(row=2, column=0, sticky="s", padx=10, pady=10)

        # Botón para volver a la vista principal en la esquina inferior derecha
        self.boton_volver = customtkinter.CTkButton(self, text="Volver", command=volver_func,
                                                    width=100, height=32)
        self.boton_volver.grid(row=2, column=0, sticky="se", padx=10, pady=10)
        
    def llamar_menu_opciones(self, elegir):
        
        """ función que va a manejar las opciones de elegir lo de bodega """
        print(f"Option selected: {elegir}")

    def mostrar_panel(self):
        """ Función que muestra el panel """
        label_titulo = customtkinter.CTkLabel(self, text="Bienvenidos a Panel de Bodega",
                                              font=("Arial", 24), text_color="#021b2b")
        label_titulo.grid(row=0, column=0, pady=20, sticky="n")
    
   
        
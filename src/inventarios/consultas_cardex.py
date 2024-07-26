"""          Importación de Módulos      """

import customtkinter
import tkinter as tk
from tkinter import ttk

class ConsultasCardex(customtkinter.CTkFrame):
    """ clases """
    def __init__(self, master):
        super().__init__(master)

        # Configurar el grid principal
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        # Frame principal para contener el formulario y la tabla
        self.main_frame = customtkinter.CTkFrame(self)
        self.main_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        
        self.main_frame.grid_columnconfigure(1, weight=3)
        
        # Titulo del Formulario
        self.label_titulo_cardex = customtkinter.CTkLabel(self.main_frame, text="Cardex", font=("Arial", 16))
        self.label_titulo_cardex.grid(row=0, column=0, columnspan=2, sticky="ew", padx=5, pady=5)
        
        # Frame para la información del artículo
        self.info_frame = customtkinter.CTkFrame(self.main_frame)
        self.info_frame.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)

        self.info_frame.grid_columnconfigure(1, weight=1)
        self.info_frame.grid_columnconfigure(3, weight=1)
        self.info_frame.grid_rowconfigure(0, weight=1)

        
        self.label_articulo = customtkinter.CTkLabel(self.info_frame, text="Artículo:")
        self.label_articulo.grid(row=0, column=0, sticky="w", padx=10, pady=5)
        
        
        self.entrada_articulo = customtkinter.CTkComboBox(self.info_frame, values=["Incaparina Instantanea ", 
                                                                                 "Incaparina Coccion rapida", 
                                                                                 "Garbanzo",
                                                                                 "Frijol Blanco",
                                                                                 "Frijol Colorado",
                                                                                 "Tortillas tostadas",
                                                                                 "Salsa Soya",
                                                                                 "Atun en agua",
                                                                                 "Pasta",
                                                                                 "Maizena",
                                                                                 "Canela",
                                                                                 "Aceite de Olivo",
                                                                                 "Salsa Naturas",
                                                                                 "Sopa Maggi",
                                                                                 "Cabello nido",
                                                                                 "Aceite 1/5 litro",
                                                                                 "Librera",
                                                                                 "Harina de Arroz",
                                                                                 "Incaparina",
                                                                                 "Incaparina Crecimax",
                                                                                 "Incaparina Maternal",
                                                                                 "Protemas",
                                                                                 "Arginin Forte",
                                                                                 "Cabello fino",
                                                                                 "Korn Flakes Kellogs",
                                                                                 "Avena",
                                                                                 "13 cereales",
                                                                                 "Pasta Ina",
                                                                                 "Azucar",
                                                                                 "Aceite"])
        self.entrada_articulo.grid(row=0, column=1, sticky="ew", padx=10, pady=5)
        self.entrada_articulo.set("")

        self.label_responsable = customtkinter.CTkLabel(self.info_frame, text="Responsable:")
        self.label_responsable.grid(row=0, column=2, sticky="w", padx=10, pady=5)
        self.entrada_responsable = customtkinter.CTkEntry(self.info_frame)
        self.entrada_responsable.grid(row=0, column=3, sticky="ew", padx=10, pady=5)

        self.label_especificaciones = customtkinter.CTkLabel(self.info_frame, text="Especificaciones:")
        self.label_especificaciones.grid(row=1, column=0, sticky="w", padx=10, pady=5)
        self.entrada_especificaciones = customtkinter.CTkEntry(self.info_frame)
        self.entrada_especificaciones.grid(row=1, column=1, sticky="ew", padx=10, pady=5)

        self.label_cargo = customtkinter.CTkLabel(self.info_frame, text="Cargo:")
        self.label_cargo.grid(row=1, column=2, sticky="w", padx=10, pady=5)
        self.entrada_cargo = customtkinter.CTkEntry(self.info_frame)
        self.entrada_cargo.grid(row=1, column=3, sticky="ew", padx=10, pady=5)

        self.label_descripcion = customtkinter.CTkLabel(self.info_frame, text="Descripción:")
        self.label_descripcion.grid(row=2, column=0, sticky="w", padx=10, pady=5)
        self.entrada_descripcion = customtkinter.CTkEntry(self.info_frame)
        self.entrada_descripcion.grid(row=2, column=1, sticky="ew", padx=10, pady=5)
        
        self.label_fecha = customtkinter.CTkLabel(self.info_frame, text="Fecha:")
        self.label_fecha.grid(row=3, column=0, sticky="w", padx=10, pady=5)
        self.entrada_fecha = customtkinter.CTkEntry(self.info_frame)
        self.entrada_fecha.grid(row=3, column=1, sticky="ew", padx=10, pady=5)
        
        self.label_no_referencia = customtkinter.CTkLabel(self.info_frame, text="Número de Refencia:")
        self.label_no_referencia.grid(row=4, column=0, sticky="w", padx=10, pady=5)
        self.entrada_no_referencia = customtkinter.CTkEntry(self.info_frame)
        self.entrada_no_referencia.grid(row=4, column=1, sticky="ew", padx=10, pady=5)
        
        self.label_remitente_destinatario = customtkinter.CTkLabel(self.info_frame, text="Remitente/Destinatario:")
        self.label_remitente_destinatario.grid(row=5, column=0, sticky="w", padx=10, pady=5)
        self.entrada_remi_desti = customtkinter.CTkEntry(self.info_frame)
        self.entrada_remi_desti.grid(row=5, column=1, sticky="ew", padx=10, pady=5)
        
        self.label_cantidad_entrada = customtkinter.CTkLabel(self.info_frame, text="Cantidad entrada:")
        self.label_cantidad_entrada.grid(row=6, column=0, sticky="w", padx=10, pady=5)
        self.entrada_cantidad_entrada = customtkinter.CTkEntry(self.info_frame)
        self.entrada_cantidad_entrada.grid(row=6, column=1, sticky="ew", padx=10, pady=5)
        
        

        self.label_firma = customtkinter.CTkLabel(self.info_frame, text="Firma:")
        self.label_firma.grid(row=2, column=2, sticky="w", padx=10, pady=5)
        self.entrada_firma = customtkinter.CTkEntry(self.info_frame)
        self.entrada_firma.grid(row=2, column=3, sticky="ew", padx=10, pady=5)
        
        
        self.label_precio_unitario = customtkinter.CTkLabel(self.info_frame, text="Precio Unitario entrada:")
        self.label_precio_unitario.grid(row=3, column=2, sticky="w", padx=10, pady=5)
        self.entrada_precio_unitario = customtkinter.CTkEntry(self.info_frame)
        self.entrada_precio_unitario.grid(row=3, column=3, sticky="ew", padx=10, pady=5)
        
        
        self.label_valor_total_entrada = customtkinter.CTkLabel(self.info_frame, text="Valor Total Entrada:")
        self.label_valor_total_entrada.grid(row=4, column=2, sticky="w", padx=10, pady=5)
        self.entrada_valor_total_entrada = customtkinter.CTkEntry(self.info_frame)
        self.entrada_valor_total_entrada.grid(row=4, column=3, sticky="ew", padx=10, pady=5)
        
        self.label_fecha_vencimiento = customtkinter.CTkLabel(self.info_frame, text="Fecha Vencimiento:")
        self.label_fecha_vencimiento.grid(row=5, column=2, sticky="w", padx=10, pady=5)
        self.entrada_fecha_vencimiento = customtkinter.CTkEntry(self.info_frame)
        self.entrada_fecha_vencimiento.grid(row=5, column=3, sticky="ew", padx=10, pady=5)
        
        self.label_no_lote = customtkinter.CTkLabel(self.info_frame, text="Número de Lote:")
        self.label_no_lote.grid(row=6, column=2, sticky="w", padx=10, pady=5)
        self.entrada_no_lote = customtkinter.CTkEntry(self.info_frame)
        self.entrada_no_lote.grid(row=6, column=3, sticky="ew", padx=10, pady=5)

        # Niveles de Seguridad
        self.label_niveles_seguridad = customtkinter.CTkLabel(self.info_frame, text="Niveles de Seguridad")
        self.label_niveles_seguridad.grid(row=0, column=4, padx=10, pady=5)
        self.entrada_niveles_seguridad = customtkinter.CTkComboBox(self.info_frame, values=["Máximo",
                                                                                            "Mínimo"])
        self.entrada_niveles_seguridad.grid(row=0, column=5, padx=10, pady=5)
        self.entrada_niveles_seguridad.set("")
        
        
        self.label_cantidad_salida = customtkinter.CTkLabel(self.info_frame, text="Cantidad de Salida")
        self.label_cantidad_salida.grid(row=1, column=4,sticky="w", padx=10, pady=5)
        self.entrada_cantidad_salida = customtkinter.CTkEntry(self.info_frame)
        self.entrada_cantidad_salida.grid(row=1, column=5, padx=10, pady=5)
        
        self.label_precio_salida = customtkinter.CTkLabel(self.info_frame, text="Precio de Salida")
        self.label_precio_salida.grid(row=2, column=4, sticky="w", padx=10, pady=5)
        self.entrada_precio_salida = customtkinter.CTkEntry(self.info_frame)
        self.entrada_precio_salida.grid(row=2, column=5, padx=10, pady=5)
        
        self.label_ajustes = customtkinter.CTkLabel(self.info_frame, text="Ajustes")
        self.label_ajustes.grid(row=3, column=4, sticky="w",padx=10, pady=5)
        self.entrada_ajustes = customtkinter.CTkComboBox(self.info_frame, values=["+",
                                                                                  "-"])
        self.entrada_ajustes.grid(row=3, column=5, padx=10, pady=5)
        self.entrada_ajustes.set("")
        
        self.label_cantidad_saldo = customtkinter.CTkLabel(self.info_frame, text="Cantidad de Saldo")
        self.label_cantidad_saldo.grid(row=4, column=4, sticky="w", padx=10, pady=5)
        self.entrada_cantidad_saldo = customtkinter.CTkEntry(self.info_frame)
        self.entrada_cantidad_saldo.grid(row=4, column=5, padx=10, pady=5)
        
        self.label_precio_saldo = customtkinter.CTkLabel(self.info_frame, text="Precio de Saldos")
        self.label_precio_saldo.grid(row=5, column=4, sticky="w", padx=10, pady=5)
        self.entrada_precio_saldo = customtkinter.CTkEntry(self.info_frame)
        self.entrada_precio_saldo.grid(row=5, column=5, padx=10, pady=5)
        
        self.label_observacion = customtkinter.CTkLabel(self.info_frame, text="Observaciones")
        self.label_observacion.grid(row=6, column=4, sticky="w", padx=10, pady=5)
        self.entrada_observacion = customtkinter.CTkEntry(self.info_frame)
        self.entrada_observacion.grid(row=6, column=5, padx=10, pady=5)

        # Botón para guardar datos en la tabla
        self.button_guardar = customtkinter.CTkButton(self.info_frame, text="Guardar", command=self.guardar_datos)
        self.button_guardar.grid(row=7, column=0,  padx=10, pady=10)
        
        self.button_mostrar = customtkinter.CTkButton(self.info_frame, text="Mostrar", command=self.guardar_datos)
        self.button_mostrar.grid(row=7, column=1,  padx=10, pady=10)
        
        self.button_eliminar = customtkinter.CTkButton(self.info_frame, text="Eliminar", command=self.guardar_datos)
        self.button_eliminar.grid(row=7, column=2,  padx=10, pady=10)
    

        # Frame para la tabla
        self.table_frame = customtkinter.CTkFrame(self.main_frame)
        self.table_frame.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)
        
        # Configurar el grid del table_frame
        self.table_frame.columnconfigure(0, weight=1)
        self.table_frame.rowconfigure(0, weight=1)
        
        # Tabla
        self.treeview = ttk.Treeview(self.table_frame, columns=("Artículo",
                                                                "Especificación",
                                                                "Descripción",
                                                                "Responsable",
                                                                "Cargo",
                                                                "Nivel De Seguridad",
                                                                "Firma",
                                                                "Fecha",
                                                                "Número de Referencia", 
                                                                "Remitente / Destinatario", 
                                                                "Cantidad Entradas", 
                                                                "P.U.", 
                                                                "Valor Total", 
                                                                "Fecha de Vencimiento", 
                                                                "Número de Lote", 
                                                                "Cantidad Salida", 
                                                                "Precio Salida", 
                                                                "Ajuste", 
                                                                "Cantidad Saldos", 
                                                                "Precio Saldos", 
                                                                "Observaciones"), show='headings')
        
        # Configuración de encabezados
        self.treeview.heading("Artículo", text="Artículo")
        self.treeview.heading("Especificación", text="Especificación")
        self.treeview.heading("Descripción", text="Descripción")
        self.treeview.heading("Responsable", text="Responsable")
        self.treeview.heading("Cargo", text="Cargo")
        self.treeview.heading("Nivel De Seguridad", text="Nivel De Seguridad")
        self.treeview.heading("Firma", text="Firma")
        self.treeview.heading("Fecha", text="Fecha")
        self.treeview.heading("Número de Referencia", text="Número de Referencia")
        self.treeview.heading("Remitente / Destinatario", text="Remitente / Destinatario")
        self.treeview.heading("Cantidad Entradas", text="Cantidad")
        self.treeview.heading("P.U.", text="P.U.")
        self.treeview.heading("Valor Total", text="Valor Total")
        self.treeview.heading("Fecha de Vencimiento", text="Fecha de Vencimiento")
        self.treeview.heading("Número de Lote", text="Número de Lote")
        self.treeview.heading("Cantidad Salida", text="Cantidad")
        self.treeview.heading("Precio Salida", text="Precio Salida")
        self.treeview.heading("Ajuste", text="Ajuste")
        self.treeview.heading("Cantidad Saldos", text="Cantidad Saldos")
        self.treeview.heading("Precio Saldos", text="Precio Saldos")
        self.treeview.heading("Observaciones", text="Observaciones")
        
        # Ajustar el ancho de las columnas
        self.treeview.column("Artículo", width=100)
        self.treeview.column("Especificación", width=150)
        self.treeview.column("Descripción", width=150)
        self.treeview.column("Responsable", width=150)
        self.treeview.column("Cargo", width=150)
        self.treeview.column("Nivel De Seguridad", width=150)
        self.treeview.column("Firma", width=150)
        self.treeview.column("Fecha", width=80)
        self.treeview.column("Número de Referencia", width=120)
        self.treeview.column("Remitente / Destinatario", width=150)
        self.treeview.column("Cantidad Entradas", width=80)
        self.treeview.column("P.U.", width=50)
        self.treeview.column("Valor Total", width=100)
        self.treeview.column("Fecha de Vencimiento", width=120)
        self.treeview.column("Número de Lote", width=100)
        self.treeview.column("Cantidad Salida", width=80)
        self.treeview.column("Precio Salida", width=100)
        self.treeview.column("Ajuste", width=80)
        self.treeview.column("Cantidad Saldos", width=80)
        self.treeview.column("Precio Saldos", width=100)
        self.treeview.column("Observaciones", width=200)
        
        self.treeview.grid(row=0, column=0, sticky="nsew")
        
        # Agregar CTkScrollbar vertical
        self.scrollbar_vertical = customtkinter.CTkScrollbar(self.table_frame, orientation="vertical", command=self.treeview.yview)
        self.treeview.configure(yscrollcommand=self.scrollbar_vertical.set)
        self.scrollbar_vertical.grid(row=0, column=1, sticky="ns")

        # Agregar CTkScrollbar horizontal
        self.scrollbar_horizontal = customtkinter.CTkScrollbar(self.table_frame, orientation="horizontal", command=self.treeview.xview)
        self.treeview.configure(xscrollcommand=self.scrollbar_horizontal.set)
        self.scrollbar_horizontal.grid(row=1, column=0, sticky="ew")

    def guardar_datos(self):
        
        """ funcion """
        # Obtener los datos de las entradas
        articulo = self.entrada_articulo.get()
        responsable = self.entrada_responsable.get()
        especificaciones = self.entrada_especificaciones.get()
        cargo = self.entrada_cargo.get()
        descripcion = self.entrada_descripcion.get()
        firma = self.entrada_firma.get()
        seguridad = self.entrada_niveles_seguridad.get()
        fecha = self.entrada_fecha.get()
        remitente_destinatorio = self.entrada_remi_desti.get()
        cantidad_entrada = self.entrada_cantidad_entrada.get()
        precio_unitario = self.entrada_precio_unitario.get()
        valor_total = self.entrada_valor_total_entrada.get()
        fecha_vencimiento = self.entrada_fecha_vencimiento.get()
        numero_lote = self.entrada_no_lote.get()
        cantidad_salida = self.entrada_cantidad_salida.get()
        precio_salida = self.entrada_precio_salida.get()
        ajuste = self.entrada_ajustes.get()
        cantidad_saldos = self.entrada_cantidad_saldo.get()
        precio_saldos = self.entrada_precio_saldo.get()
        observaciones = self.entrada_observacion.get()
        
        
        # Insertar los datos en la tabla
        self.treeview.insert('', 'end', values=(articulo, responsable, 
                                                especificaciones, cargo, 
                                                descripcion, firma, seguridad,
                                                fecha, remitente_destinatorio,
                                                cantidad_entrada, precio_unitario,
                                                valor_total, fecha_vencimiento, numero_lote,
                                                cantidad_salida, precio_salida,
                                                ajuste, cantidad_saldos, precio_saldos,
                                                observaciones))

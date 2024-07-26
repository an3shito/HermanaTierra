"""          Importación de Módulos      """

import customtkinter
import tkinter as tk
from tkinter import ttk

class UtilesDeOficinas(customtkinter.CTkFrame):

    def __init__(self, master):
        super().__init__(master)
        
        self._configurar_interfaz()
    
    def _configurar_interfaz(self):
        # Configurar el layout
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        
        self.label_tituloIn = customtkinter.CTkLabel(self, text="Inventario Utiles de oficina", font=("Arial",32))
        self.label_tituloIn.grid(row=0, column=0, columnspan=2, sticky="ew", padx=5, pady=5)
        
        # Frame para el formulario
        self.form_frame = customtkinter.CTkFrame(self)
        self.form_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        
        # Frame para la tabla
        self.table_frame = customtkinter.CTkFrame(self)
        self.table_frame.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)
        
        # Configurar el grid del form_frame
        for i in range(10):
            self.form_frame.rowconfigure(i, weight=1)
        self.form_frame.columnconfigure(0, weight=1)
        
        # Etiquetas y entradas del formulario
        self.label_nombre = customtkinter.CTkLabel(self.form_frame, text="Nombre del Suministro:")
        self.label_nombre.grid(row=0, column=0, sticky="w", padx=10, pady=5)
        self.entry_nombre = customtkinter.CTkEntry(self.form_frame)
        self.entry_nombre.grid(row=0, column=1, sticky="ew", padx=10, pady=5)

        self.label_presentacion = customtkinter.CTkLabel(self.form_frame, text="Presentación:")
        self.label_presentacion.grid(row=1, column=0, sticky="w", padx=10, pady=5)
        self.entry_presentacion = customtkinter.CTkEntry(self.form_frame)
        self.entry_presentacion.grid(row=1, column=1, sticky="ew", padx=10, pady=5)

        self.label_lote = customtkinter.CTkLabel(self.form_frame, text="Lote:")
        self.label_lote.grid(row=2, column=0, sticky="w", padx=10, pady=5)
        self.entry_lote = customtkinter.CTkEntry(self.form_frame)
        self.entry_lote.grid(row=2, column=1, sticky="ew", padx=10, pady=5)

        self.label_fv = customtkinter.CTkLabel(self.form_frame, text="F/V:")
        self.label_fv.grid(row=3, column=0, sticky="w", padx=10, pady=5)
        self.entry_fv = customtkinter.CTkEntry(self.form_frame)
        self.entry_fv.grid(row=3, column=1, sticky="ew", padx=10, pady=5)

        self.label_cantidad = customtkinter.CTkLabel(self.form_frame, text="Cantidad:")
        self.label_cantidad.grid(row=4, column=0, sticky="w", padx=10, pady=5)
        self.entry_cantidad = customtkinter.CTkEntry(self.form_frame)
        self.entry_cantidad.grid(row=4, column=1, sticky="ew", padx=10, pady=5)

        self.label_precio = customtkinter.CTkLabel(self.form_frame, text="Precio:")
        self.label_precio.grid(row=5, column=0, sticky="w", padx=10, pady=5)
        self.entry_precio = customtkinter.CTkEntry(self.form_frame)
        self.entry_precio.grid(row=5, column=1, sticky="ew", padx=10, pady=5)

        self.label_total = customtkinter.CTkLabel(self.form_frame, text="Total:")
        self.label_total.grid(row=6, column=0, sticky="w", padx=10, pady=5)
        self.entry_total = customtkinter.CTkEntry(self.form_frame)
        self.entry_total.grid(row=6, column=1, sticky="ew", padx=10, pady=5)
        
        # Botones
        self.boton_guardar = customtkinter.CTkButton(self.form_frame, text="Guardar", command=self.guardar_datos)
        self.boton_guardar.grid(row=7, column=0, pady=10, padx=10, sticky="ew")
        
        self.boton_mostrar = customtkinter.CTkButton(self.form_frame, text="Mostrar", command=self.mostrar_datos)
        self.boton_mostrar.grid(row=7, column=1, pady=10, padx=10, sticky="ew")
        
        self.boton_buscar = customtkinter.CTkButton(self.form_frame, text="Buscar", command=self.buscar_datos)
        self.boton_buscar.grid(row=8, column=0, pady=10, padx=10, sticky="ew")
        
        self.boton_eliminar = customtkinter.CTkButton(self.form_frame, text="Eliminar", command=self.eliminar_datos)
        self.boton_eliminar.grid(row=8, column=1, pady=10, padx=10, sticky="ew")
        
        self.boton_cargar_archivos = customtkinter.CTkButton(self.form_frame, text="Cargar Archivos", command=self.cargar_archivos)
        self.boton_cargar_archivos.grid(row=9, column=0, columnspan=2, pady=10, padx=10, sticky="ew")

        # Configurar el grid del table_frame
        self.table_frame.columnconfigure(0, weight=1)
        self.table_frame.rowconfigure(0, weight=1)
        
        # Tabla
        self.treeview = ttk.Treeview(self.table_frame, columns=("Nombre", "Presentación", "Lote", "FV", "Cantidad", "Precio", "Total"), show='headings')
        self.treeview.heading("Nombre", text="Nombre del Suministro")
        self.treeview.heading("Presentación", text="Presentación")
        self.treeview.heading("Lote", text="Lote")
        self.treeview.heading("FV", text="F/V")
        self.treeview.heading("Cantidad", text="Cantidad")
        self.treeview.heading("Precio", text="Precio")
        self.treeview.heading("Total", text="Total")
        
        # Ajustar el ancho de las columnas
        self.treeview.column("Nombre", width=150)
        self.treeview.column("Presentación", width=100)
        self.treeview.column("Lote", width=100)
        self.treeview.column("FV", width=70)
        self.treeview.column("Cantidad", width=70)
        self.treeview.column("Precio", width=100)
        self.treeview.column("Total", width=100)
        
        self.treeview.grid(row=0, column=0, sticky="nsew")
        
        # Agregar CTkScrollbar
        self.scrollbar = customtkinter.CTkScrollbar(self.table_frame, orientation="vertical", command=self.treeview.yview)
        self.treeview.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.grid(row=0, column=1, sticky="ns")

    def guardar_datos(self):
        """  Función para guardar los datos del formulario en la tabla"""
        nombre = self.entry_nombre.get()
        presentacion = self.entry_presentacion.get()
        lote = self.entry_lote.get()
        fv = self.entry_fv.get()
        cantidad = self.entry_cantidad.get()
        precio = self.entry_precio.get()
        total = self.entry_total.get()
        
        self.treeview.insert("", "end", values=(nombre, presentacion, lote, fv, cantidad, precio, total))
        
        # Limpiar entradas
        self.entry_nombre.delete(0, tk.END)
        self.entry_presentacion.delete(0, tk.END)
        self.entry_lote.delete(0, tk.END)
        self.entry_fv.delete(0, tk.END)
        self.entry_cantidad.delete(0, tk.END)
        self.entry_precio.delete(0, tk.END)
        self.entry_total.delete(0, tk.END)

    def mostrar_datos(self):
        # Función para mostrar todos los datos (por ahora no hace nada)
        pass

    def buscar_datos(self):
        # Función para buscar datos (por ahora no hace nada)
        pass

    def eliminar_datos(self):
        """ Función para eliminar el dato seleccionado """
        selected_item = self.treeview.selection()
        if selected_item:
            self.treeview.delete(selected_item)

    def cargar_archivos(self):
        # Función para cargar archivos (por ahora no hace nada)
        pass


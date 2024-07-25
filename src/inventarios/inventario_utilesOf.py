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
        self.rowconfigure(0, weight=1)
        
        # Frame para el formulario
        self.form_frame = customtkinter.CTkFrame(self)
        self.form_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        
        # Frame para la tabla
        self.table_frame = customtkinter.CTkFrame(self)
        self.table_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        
        # Configurar el grid del form_frame
        for i in range(6):
            self.form_frame.rowconfigure(i, weight=1)
        self.form_frame.columnconfigure(0, weight=1)
        
        # Etiquetas y entradas del formulario
        self.label_nombre = customtkinter.CTkLabel(self.form_frame, text="Nombre:")
        self.label_nombre.grid(row=0, column=0, sticky="w", padx=10, pady=5)
        self.entry_nombre = customtkinter.CTkEntry(self.form_frame)
        self.entry_nombre.grid(row=0, column=1, sticky="ew", padx=10, pady=5)

        self.label_cantidad = customtkinter.CTkLabel(self.form_frame, text="Cantidad:")
        self.label_cantidad.grid(row=1, column=0, sticky="w", padx=10, pady=5)
        self.entry_cantidad = customtkinter.CTkEntry(self.form_frame)
        self.entry_cantidad.grid(row=1, column=1, sticky="ew", padx=10, pady=5)

        self.label_precio = customtkinter.CTkLabel(self.form_frame, text="Precio:")
        self.label_precio.grid(row=2, column=0, sticky="w", padx=10, pady=5)
        self.entry_precio = customtkinter.CTkEntry(self.form_frame)
        self.entry_precio.grid(row=2, column=1, sticky="ew", padx=10, pady=5)

        self.label_fecha = customtkinter.CTkLabel(self.form_frame, text="Fecha de Ingreso:")
        self.label_fecha.grid(row=3, column=0, sticky="w", padx=10, pady=5)
        self.entry_fecha = customtkinter.CTkEntry(self.form_frame)
        self.entry_fecha.grid(row=3, column=1, sticky="ew", padx=10, pady=5)
        
        self.boton_guardar = customtkinter.CTkButton(self.form_frame, text="Guardar", command=self.guardar_datos)
        self.boton_guardar.grid(row=4, column=0, columnspan=2, pady=10, padx=10, sticky="ew")
        
        # Configurar el grid del table_frame
        self.table_frame.columnconfigure(0, weight=1)
        self.table_frame.rowconfigure(0, weight=1)
        
        # Tabla
        self.treeview = ttk.Treeview(self.table_frame, columns=("Nombre", "Cantidad", "Precio", "Fecha"), show='headings')
        self.treeview.heading("Nombre", text="Nombre")
        self.treeview.heading("Cantidad", text="Cantidad")
        self.treeview.heading("Precio", text="Precio")
        self.treeview.heading("Fecha", text="Fecha de Ingreso")
        
        self.treeview.grid(row=0, column=0, sticky="nsew")
        
        # Agregar CTkScrollbar
        self.scrollbar = customtkinter.CTkScrollbar(self.table_frame, orientation="vertical", command=self.treeview.yview)
        self.treeview.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.grid(row=0, column=1, sticky="ns")

    def guardar_datos(self):
        # Función para guardar los datos del formulario en la tabla
        nombre = self.entry_nombre.get()
        cantidad = self.entry_cantidad.get()
        precio = self.entry_precio.get()
        fecha = self.entry_fecha.get()
        
        self.treeview.insert("", "end", values=(nombre, cantidad, precio, fecha))
        
        # Limpiar entradas
        self.entry_nombre.delete(0, tk.END)
        self.entry_cantidad.delete(0, tk.END)
        self.entry_precio.delete(0, tk.END)
        self.entry_fecha.delete(0, tk.END)
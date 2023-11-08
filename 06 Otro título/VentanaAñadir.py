# Mayo 20, 2023. 2:11 a.m.

import tkinter as tk
from tkinter import ttk, messagebox

class VentanaAñadir(tk.Tk):
    def __init__(self, ventana_principal):
        super().__init__()
        self.title("Añadir self.Producto")
        self.resizable(False, False)

        self.cuadro_datos = ttk.Frame(self)

        self.producto = ttk.Label(self.cuadro_datos, text="Producto")
        self.precio = ttk.Label(self.cuadro_datos, text="Precio")
        self.fecha = ttk.Label(self.cuadro_datos, text="Fecha")

        self.producto_ = ttk.Entry(self.cuadro_datos)
        self.precio_ = ttk.Entry(self.cuadro_datos)
        self.fecha_ = ttk.Entry(self.cuadro_datos)

        self.producto.grid(sticky=tk.W, row=0, column=0, padx=10, pady=10)
        self.precio.grid(sticky=tk.W, row=1, column=0, padx=10, pady=10)
        self.fecha.grid(sticky=tk.W, row=2, column=0, padx=10, pady=10)

        self.producto_.grid(row=0, column=1, padx=10, pady=10)
        self.precio_.grid(row=1, column=1, padx=10, pady=10)
        self.fecha_.grid(row=2, column=1, padx=10, pady=10)

        self.cuadro_datos.grid(row=0, column=0)

        cuadro_botones = ttk.Frame(self)

        self.aceptar = ttk.Button(cuadro_botones, text="Aceptar", command=lambda: self.función_aceptar(ventana_principal))
        self.cancelar = ttk.Button(cuadro_botones, text="Cancelar", command=self.destroy)

        self.aceptar.grid(row=0, column=0, padx=10, pady=10)
        self.cancelar.grid(row=0, column=1, padx=10, pady=10)

        cuadro_botones.grid(row=1, column=0)

        self.mainloop()
    
    def función_aceptar(self, ventana_principal):
        agregando = [self.producto_.get(), self.precio_.get(), self.fecha_.get()]
        existentes = []
        for elemento in ventana_principal.lista_compras.get_children():
            datos = []
            for subelemento in ventana_principal.lista_compras.item(elemento)["values"]:
                datos.append(str(subelemento))
            existentes.append(datos)
        if agregando in existentes:
            contenido_repetido = f"El elemento no se agregó porque ya existía:\n\n\
                Producto: {agregando[0]}\n\
                Precio: {agregando[1]}\n\
                Fecha: {agregando[2]})"
            messagebox.showwarning("Elementos Repetidos", contenido_repetido)
        else:
            ventana_principal.lista_compras.insert("", tk.END, values=(agregando[0], agregando[1], agregando[2]))
        self.destroy()

# Mayo 20, 2023. 2:28 a.m.
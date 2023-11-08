# Mayo 20, 2023. 1:10 a.m.

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import VentanaAñadir

class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Finanzas")

        self.libro = ttk.Notebook(self)

        self.pestaña_compras = ttk.Frame(self)

        self.cuadro_lista = ttk.Frame(self.pestaña_compras)

        self.títulos = ("Producto", "Precio", "Fecha")

        self.lista_compras = ttk.Treeview(self.cuadro_lista, columns=self.títulos, show="headings")

        self.lista_compras.heading("Producto", text="Producto")
        self.lista_compras.heading("Precio", text="Precio")
        self.lista_compras.heading("Fecha", text="Fecha")

        self.lista_compras.column("Producto", width=200, anchor=tk.W)
        self.lista_compras.column("Precio", width=200, anchor=tk.W)
        self.lista_compras.column("Fecha", width=200, anchor=tk.W)

        self.lista_compras.pack(side=tk.LEFT, padx=0, pady=0, ipadx=0, ipady=0, expand=True)

        self.lista_deslizar = ttk.Scrollbar(self.cuadro_lista, orient=tk.VERTICAL, command=self.lista_compras.yview)
        self.lista_compras.configure(yscroll=self.lista_deslizar.set)
        self.lista_deslizar.pack(side=tk.RIGHT, fill=tk.Y, padx=0, pady=0, ipadx=0, ipady=0)

        self.cuadro_lista.pack(side=tk.TOP, padx=0, pady=0, ipadx=0, ipady=0)

        self.cuadro_botones = ttk.Frame(self.pestaña_compras)
        self.boton_añadir = ttk.Button(self.cuadro_botones, text="Añadir", command=self.función_añadir)
        self.boton_quitar = ttk.Button(self.cuadro_botones, text="Quitar", command=self.función_quitar)
        self.boton_abrir = ttk.Button(self.cuadro_botones, text="Abrir", command=self.función_abrir)
        self.boton_guardar = ttk.Button(self.cuadro_botones, text="Guardar", command=self.función_guardar)

        self.boton_añadir.pack(side=tk.LEFT, padx=0, pady=0, ipadx=0, ipady=0)
        self.boton_quitar.pack(side=tk.LEFT, padx=0, pady=0, ipadx=0, ipady=0)
        self.boton_abrir.pack(side=tk.LEFT, padx=0, pady=0, ipadx=0, ipady=0)
        self.boton_guardar.pack(side=tk.LEFT, padx=0, pady=0, ipadx=0, ipady=0)

        self.cuadro_botones.pack(side=tk.BOTTOM, padx=0, pady=0, ipadx=0, ipady=0)

        pestaña_gráfica = ttk.Frame(self)

        self.libro.add(self.pestaña_compras, text="Lista")
        self.libro.add(pestaña_gráfica, text="Gráfica")

        self.libro.pack(padx=0, pady=0, ipadx=0, ipady=0)

        self.mainloop()
    
    def función_añadir(self):
        ventana_añadir = VentanaAñadir.VentanaAñadir(self)

    def función_quitar(self):
        self.lista_compras.delete(self.lista_compras.selection())

    def función_abrir(self):
        for nombre in filedialog.askopenfilenames(title="Importar", initialdir="...", filetypes=[("LightyDataFile", ".ldf")]):
            existentes = []
            for elemento in self.lista_compras.get_children():
                datos = []
                for subelemento in self.lista_compras.item(elemento)["values"]:
                    datos.append(str(subelemento))
                existentes.append(datos)
            agregar = []
            repetidos = []
            archivo = open(nombre, "r")
            for línea in archivo.readlines():
                if línea[-1] == "\n":
                    línea = línea[:-1]
                datos = línea.split(",")
                agregar.append(datos)
                for existente in existentes:
                    if datos == existente:
                        repetidos.append(datos)
                        agregar.remove(datos)
            if repetidos:
                contenido_repetido = f"Los siguientes elementos ya existían y se omitieron:"
                for repetido in repetidos:
                    contenido_repetido += f"\n\n\
                        Producto: {repetido[0]}\n\
                        Precio: {repetido[1]}\n\
                        Fecha: {repetido[2]})"
                messagebox.showwarning("Elementos Repetidos", contenido_repetido)
            for elemento in agregar:
                self.lista_compras.insert("", tk.END, values=(elemento[0], elemento[1], elemento[2]))

    def función_guardar(self):
        archivo = filedialog.asksaveasfile(mode='w', defaultextension=".ldf")
        if archivo:
            datos = ""
            for elemento in self.lista_compras.get_children():
                subdatos = []
                for subelemento in self.lista_compras.item(elemento)["values"]:
                    subdatos.append(subelemento)
                datos += f"{subdatos[0]},{subdatos[1]},{subdatos[2]}\n"
            archivo.write(datos)
            archivo.close()

# Mayo 20, 2023. 2:10 a.m.
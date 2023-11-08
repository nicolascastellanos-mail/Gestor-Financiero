# 1 de Abril de 2023. 3:44 a.m.

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Primer Concepto")

notebook = ttk.Notebook(root)
notebook.pack(padx=10, pady=10)

listbox_tab = ttk.Frame(root)

titles = ("item", "cost", "date")

product_list = ttk.Treeview(listbox_tab, columns=titles, show="headings")

product_list.heading("item", text="Artículo")
product_list.heading("cost", text="Precio")
product_list.heading("date", text="Fecha de Compra")

product_list.column("item", width=200, anchor=tk.W)
product_list.column("cost", width=100, anchor=tk.W)
product_list.column("date", width=150, anchor=tk.W)

product_list.grid(row=0, column=0)

scroll = ttk.Scrollbar(listbox_tab, orient=tk.VERTICAL, command=product_list.yview)
product_list.configure(yscroll=scroll.set)
scroll.grid(row=0, column=1, sticky=tk.NS)

buttons = ttk.Frame(listbox_tab)
buttons.grid(row=1, column=0, sticky=tk.W)

add = ttk.Button(buttons, text="Añadir")
add.grid(row=0, column=0 ,pady=10)

remove = ttk.Button(buttons, text="Quitar")
remove.grid(row=0, column=1 ,pady=10)

import_ = ttk.Button(buttons, text="Importar")
import_.grid(row=0, column=2 ,pady=10)

export = ttk.Button(buttons, text="Exportar")
export.grid(row=0, column=3 ,pady=10)

notebook.add(listbox_tab, text="Historial")

graph_tab = ttk.Frame(root)

notebook.add(graph_tab, text="Gráfica")

root.mainloop()

# 1 de Abril de 2023. 4:13 a.m.

# Añadidos botones de importar y exportar a las 11:19 a.m.

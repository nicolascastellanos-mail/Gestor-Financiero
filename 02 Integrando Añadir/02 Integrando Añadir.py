# 1 de Abril de 2023. 11:32 a.m.

import tkinter as tk
from tkinter import ttk

def add_function():
	def define_item():
		product_list.insert("", tk.END, values=(str(name_entry.get()), str(cost_entry.get()), str(date_entry.get())))
		add_root.destroy()

	add_root = tk.Tk()
	add_root.title("Añadir")

	name_label = ttk.Label(add_root, text="Nombre del artículo:")
	name_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

	name_entry = ttk.Entry(add_root)
	name_entry.grid(row=0, column=1, padx=10, pady=10, sticky=tk.EW)

	cost_label = ttk.Label(add_root, text="Precio del artículo:")
	cost_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

	cost_entry = ttk.Entry(add_root)
	cost_entry.grid(row=1, column=1, padx=10, pady=10, sticky=tk.EW)

	date_label = ttk.Label(add_root, text="Fecha de compra yyyy/mm/dd:")
	date_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

	date_entry = ttk.Entry(add_root)
	date_entry.grid(row=2, column=1, padx=10, pady=10, sticky=tk.EW)

	buttons_frame = ttk.Frame(add_root)
	buttons_frame.grid(row=3, column=1, sticky=tk.W)

	accept_button = ttk.Button(buttons_frame, text="Aceptar", command=define_item)
	accept_button.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

	cancel_button = ttk.Button(buttons_frame, text="Cancelar", command=add_root.destroy) # TODO fix command
	cancel_button.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

	add_root.mainloop()

def remove_function():
	product_list.delete(product_list.selection())

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

add = ttk.Button(buttons, text="Añadir", command=add_function)
add.grid(row=0, column=0 ,pady=10)

remove = ttk.Button(buttons, text="Quitar", command=remove_function)
remove.grid(row=0, column=1 ,pady=10)

import_ = ttk.Button(buttons, text="Importar")
import_.grid(row=0, column=2 ,pady=10)

export = ttk.Button(buttons, text="Exportar")
export.grid(row=0, column=3 ,pady=10)

notebook.add(listbox_tab, text="Historial")

graph_tab = ttk.Frame(root)

notebook.add(graph_tab, text="Gráfica")

root.mainloop()

# 1 de Abril de 2023. 11:58 a.m.

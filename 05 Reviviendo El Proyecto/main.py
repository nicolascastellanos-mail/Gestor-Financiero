# 17 de Mayo de 2023. 8:07 p.m.

from DateF import validate

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def add_window():
	def define_item():
		product_list.insert("", tk.END, values=(str(name_entry.get()), str(cost_entry.get()), str(date_entry.get())))
		add_root.destroy()
		graph_function()

	def validate_text(event):
		pass
		"""
		original = date_entry.get()
		validated = validate(original)
		date_entry.delete(0, tk.END)
		date_entry.insert(0, validated)
		"""

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

	date_label = ttk.Label(add_root, text="Fecha de compra dd/mm/yyyy:")
	date_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

	date_entry = ttk.Entry(add_root)
	date_entry.grid(row=2, column=1, padx=10, pady=10, sticky=tk.EW)

	date_keys = [
	"1",
	"2",
	"3",
	"4",
	"5",
	"6",
	"7",
	"8",
	"9",
	"0",
	"<space>"
	]

	for date_key in date_keys:
		date_entry.bind(date_key, validate_text)

	buttons_frame = ttk.Frame(add_root)
	buttons_frame.grid(row=3, column=1, sticky=tk.W)

	accept_button = ttk.Button(buttons_frame, text="Aceptar", command=define_item)
	accept_button.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

	cancel_button = ttk.Button(buttons_frame, text="Cancelar", command=add_root.destroy) # TODO fix command
	cancel_button.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

	add_root.mainloop()

def remove_function():
	product_list.delete(product_list.selection())

def import_function():
	for name in filedialog.askopenfilenames(title="Importar", initialdir="...", filetypes=[("LightyDataFile", ".ldf")]):
		file = open(name, "r")
		for line in file.readlines():
			if line[-1] == "\n":
				line = line[:-1]
			data = line.split(",")
			product_list.insert("", tk.END, values=(data[0], data[1], data[2]))
	graph_function()

def graph_function():
	history = {}
	for item in product_list.get_children():
		if product_list.item(item)["values"][2] not in history.keys():
			history[product_list.item(item)["values"][2]] = int(product_list.item(item)["values"][1])
			continue
		history[product_list.item(item)["values"][2]] += int(product_list.item(item)["values"][1])
	dates = list(history.keys())
	spends = [float(money) for money in list(history.values())]
	
	histogram = plt.figure(tight_layout=True)
	gs = gridspec.GridSpec(2, 2)

	ax = histogram.add_subplot(gs[0, :])

	ax.plot(0, max(spends), len(spends))
	ax.set_xlabel("Date")
	ax.set_ylabel("Spend")
	ax.set_xticks(np.linspace(0, len(dates), len(dates)))
	ax.set_xticklabels(dates, rotation='vertical', fontsize=10)

	ax.plot(np.linspace(0, len(dates), len(dates)), spends)

	histogram.align_labels()

	graph_canvas = FigureCanvasTkAgg(histogram, master=graph_tab)

	graph_canvas.draw()

	graph_canvas.get_tk_widget().pack()

root = tk.Tk()
root.title("Shopping Manager")

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

add = ttk.Button(buttons, text="Añadir", command=add_window)
add.grid(row=0, column=0 ,pady=10)

remove = ttk.Button(buttons, text="Quitar", command=remove_function)
remove.grid(row=0, column=1 ,pady=10)

import_ = ttk.Button(buttons, text="Abrir", command=import_function)
import_.grid(row=0, column=2 ,pady=10)

export = ttk.Button(buttons, text="Guardar")
export.grid(row=0, column=3 ,pady=10)

notebook.add(listbox_tab, text="Historial")

graph_tab = ttk.Frame(root)

notebook.add(graph_tab, text="Gráfica")

root.mainloop()

# 17 de Mayo de 2023. 10:06 p.m.
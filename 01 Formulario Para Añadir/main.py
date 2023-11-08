# 1 de Abril de 2023. 11:20 a.m.

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Añadir")

name_label = ttk.Label(root, text="Nombre del artículo:")
name_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

name_string = tk.StringVar()
name_entry = ttk.Entry(root, textvariable=name_string)
name_entry.grid(row=0, column=1, padx=10, pady=10, sticky=tk.EW)

cost_label = ttk.Label(root, text="Precio del artículo:")
cost_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

cost_string = tk.StringVar()
cost_entry = ttk.Entry(root, textvariable=cost_string)
cost_entry.grid(row=1, column=1, padx=10, pady=10, sticky=tk.EW)

date_label = ttk.Label(root, text="Fecha de compra yyyy/mm/dd:")
date_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

date_string = tk.StringVar()
date_entry = ttk.Entry(root, textvariable=date_string)
date_entry.grid(row=2, column=1, padx=10, pady=10, sticky=tk.EW)

buttons_frame = ttk.Frame(root)
buttons_frame.grid(row=3, column=1, pady=10, sticky=tk.W)

accept_button = ttk.Button(buttons_frame, text="Aceptar")
accept_button.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

cancel_button = ttk.Button(buttons_frame, text="Cancelar")
cancel_button.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

root.mainloop()

# 1 de Abril de 2023. 11:32 a.m.

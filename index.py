import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

def items_selected(event):
    selected_indices = listbox.curselection()
    selected_lista = ",".join([listbox.get(i) for i in selected_indices])
    msg = f'Selecionar: {selected_lista}'
    showinfo(title='Informacion', message=msg)

window = tk.Tk()
window.title("Lista de la compra")
window.geometry("300x300")

lista = ('Naranjas', 'Pomas', 'Peras', 'Castañas', 'Piñas', 'Pomelo', 'Melon', 'Sandia')

varible = tk.Variable(value=lista)
listbox = tk.Listbox(window, listvariable=varible, height=6, selectmode=tk.EXTENDED)

listbox.pack(expand=True, fill=tk.BOTH)

listbox.bind('<<ListboxSelect>>', items_selected)

window.mainloop()
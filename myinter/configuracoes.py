from tkinter import *

class Configuracoes:
  def __init__(self, master):
    from .menu_barra import MenuBarra
    for widget in master.winfo_children():
      widget.destroy()
    self.master = master
    self.master.title("Configurações")
    self.master.geometry('1300x650')
    self.menu = MenuBarra(self.master)
    self.base = Frame(self.master)
    self.base.pack(pady = 20)
    self.titulo = Label(self.base, text='Configurações', font=('Garamond','40'))
    self.titulo.pack(pady = 20)
    self.texto = Label(self.base, text='Em desenvolvimento', font=('Arial','14','bold'))
    self.texto.pack(pady = 20)
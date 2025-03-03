from tkinter import *
from tkinter import messagebox 

class MenuBarra:
  def __init__(self, master):
    self.master = master
    self.menubar = Menu(self.master)
  
    self.janelas = Menu(self.menubar, tearoff=0)
    self.janelas.add_command(label="Home", command=self.abrirHome)
    self.janelas.add_command(label="Jogar", command=self.abrirJogo)
    self.janelas.add_command(label="Configurações", command=self.abrirConfiguracoes)
    self.janelas.add_command(label="Sair", command=self.sair)
    self.menubar.add_cascade(label="Janelas", menu=self.janelas)
    self.master.config(menu=self.menubar)

  def abrirHome(self, *args, **kwargs):
    #if messagebox.askyesno(title="Confirmação", message="Ao mudar janela você pode perder informações da seed!\nConfirma saída?"):
      from .home import Home
      janela = Toplevel(Home(self.master))

  def abrirJogo(self, *args, **kwargs):
    #if messagebox.askyesno(title="Confirmação", message="Ao mudar janela pode perder informações da seed!\nConfirma saída?"):
      from .jogo import Jogo
      janela = Toplevel(Jogo(self.master))

  def abrirConfiguracoes(self, *args, **kwargs):
    #if messagebox.askyesno(title="Confirmação", message="Ao mudar janela você pode perder informações da seed!\nConfirma saída?"):
      from .configuracoes import Configuracoes
      janela = Toplevel(Configuracoes(self.master))

  def sair(self, *args, **kwargs):
    if messagebox.askyesno(title="Confirmação", message="Confirma saída?"):
      self.master.destroy()
from tkinter import *

class Home:
  def __init__(self, master):
    from .menu_barra import MenuBarra
    for widget in master.winfo_children():
      widget.destroy()
    self.master = master
    self.master.title("Home")
    self.master.geometry('1300x650')
    self.menu = MenuBarra(self.master)
    self.base = Frame(self.master)
    self.base.pack(pady = 20)

    self.cen = Frame(self.base)
    self.cen.grid(row=0, column=0, columnspan=2)

    self.esq = Frame(self.base)
    self.esq.grid(row=1, column=0, pady=70, padx=200)
    
    self.dir = Frame(self.base)
    self.dir.grid(row=1, column=1, pady=70, padx=200)

    self.titulo = Label(self.cen, text='Vida', font=('Garamond','45'))
    self.titulo.pack(pady=10)
    self.texto = Label(self.cen, text='Em desenvolvimento', font=('Arial','14','bold'))
    self.texto.pack(pady=10)
    


    self.botoes = Frame(self.esq)
    self.botoes.grid()
    
    self.botao_abrirConfiguracoes = Button(self.botoes, text='Configurações', fg='black', bg='#7CCD7C',
                                           font=('Arial','16', 'bold'), relief=RIDGE, height=2, width=12,
                                           command=self.menu.abrirConfiguracoes)
    self.botao_abrirConfiguracoes.grid(row=0, column=0, padx=20)
    
    self.botao_abrirJogo = Button(self.botoes, text='Jogar', fg='black', bg='#7CCD7C',
                                  font=('Arial','16', 'bold'), relief=RIDGE, height=2, width=12,
                                  command=self.menu.abrirJogo)
    self.botao_abrirJogo.grid(row=0, column=1, padx=20)

    self.botao_abrirSair = Button(self.botoes, text='Sair', fg='black', bg='#7CCD7C',
                                  font=('Arial','16', 'bold'), relief=RIDGE, height=2, width=12,
                                  command=self.menu.sair)
    self.botao_abrirSair.grid(row=0, column=2, padx=20)



    self.sobre = Frame(self.dir)
    self.sobre.grid()

    self.titulo = Label(self.sobre, text='Sobre', font=('Garamond','35'))
    self.titulo.pack(pady = 20)
    self.texto1 = Label(self.sobre, text='Esta é minha implementação do Jogo da Vida de Conway.', font=('Arial','14','bold'))
    self.texto1.pack(pady = 20)
    self.texto2 = Label(self.sobre, text='Código: Carlos de Moura\ngithub.com/carlosdemoura', font=('Arial','14','bold'))
    self.texto2.pack()
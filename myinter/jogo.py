from tkinter import *
from tkinter import ttk, filedialog, messagebox
from matplotlib import colors, pyplot as plt
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from platform import platform
from pathlib import Path

from myseed.evoluir import evoluir
from myseed.geradora import gerar_seed, centralizar, cortar_seed
from myseed.girar import rodar, vespelhar, hespelhar, transpor
from myseed.seedtxt import importar, exportar
#from myseed import centralizar, cortar_seed, gerar_seed, evoluir, rodar, vespelhar, hespelhar, transpor, importar, exportar

class Jogo:
  def __init__(self, master):
    from .menu_barra import MenuBarra
    for widget in master.winfo_children():
      widget.destroy()
    self.master = master
    self.master.title("Principal")
    self.master.geometry('1300x650')
    self.menu = MenuBarra(self.master)
    self.titulo_geral = Label(self.master, text='jogo da vida', font=('Garamond', '20'))
    self.titulo_geral.pack(pady=10)
    self.tipo = 1 #1 BOTOES      0 GRÁFICO
    self.n = 25
    
    self.grade_geral = Frame(self.master)
    self.grade_geral.pack(pady=5)

    self.grade_girar = Frame(self.grade_geral)
    self.grade_girar.grid(row=0, column=0, padx=50, pady=0)
    self.girar_imagens = []
    self.girar_botoes = []
    self.girar_args = ({'file': './imagens/horario.png',     'command': self.rodar_tk},
                       {'file': './imagens/antihorario.png', 'command': lambda: self.rodar_tk(3)},
                       {'file': './imagens/vespelhar.png',   'command': self.vespelhar_tk},
                       {'file': './imagens/hespelhar.png',   'command': self.hespelhar_tk},
                       {'file': './imagens/transpor.png',    'command': self.transpor_tk})
    for i, arg in enumerate(self.girar_args):
      self.girar_imagens.append( PhotoImage(file=arg['file']) )
      self.girar_botoes.append( Button(self.grade_girar, image=self.girar_imagens[i], height=30, width=30, command=arg['command']) ) 
      self.girar_botoes[i].grid(row=i, column=0, padx=0, pady=20)

    self.grade_jogo = Frame(self.grade_geral)
    self.grade_jogo.grid(row=0, column=1, padx=20, pady=0)
    self.titulo_grade = Label(self.grade_jogo, text=f'Geração 0', font=('Arial','16'))
    self.titulo_grade.pack()
    self.grade = Frame(self.grade_jogo)
    self.grade.pack()
    self.seed = [[0 for _ in range(self.n)] for _ in range(self.n)]
    self.state = [[0 for _ in range(self.n)] for _ in range(self.n)]
    self.state_i = 0
    
    self.criar_botoes()
    self.rodape = Frame(self.grade_geral)
    self.rodape.grid(row=1, column=1, pady=10)
    self.radios_f = Frame(self.rodape)
    self.radios_f.grid(row=0, column=0)
    self.radios = []
    radios_args = ({'text': "Grade", 'value':1, 'command': self.criar_botoes}, {'text': "Gráfico", 'value':0,'command': self.criar_grafico})
    for i, arg in enumerate(radios_args):
      self.radios.append( Radiobutton(self.radios_f, **arg) )
      self.radios[i].grid(row=0, column=i)
    
    self.frame_n = Frame(self.rodape)
    self.frame_n.grid(row=0, column=1, padx=100)
    self.label_n = Label(self.frame_n, text='n ', font=('Arial','12')).grid(row=0, column=0)
    self.entry_n = ttk.Entry(self.frame_n, font=('Arial','12'), width=4)
    self.entry_n.insert(0, "25")
    self.entry_n.grid(row=0, column=1)
    self.botao_n = Button(self.frame_n, text='Ok', fg='black', bg='#7CCD7C', font=('Arial','12'), relief=RIDGE, command=self.alterarn).grid(row=0, column=2, padx=10)


    self.comandos = Frame(self.grade_geral)
    self.comandos.grid(row=0, column=2, padx=20, pady=0)
    self.comandos1 = Frame(self.comandos)
    self.comandos1.grid(row=1, column=0, padx=0, pady=50)
    self.comandos1_botoes = []
    args1 = ({'text': 'Importar Seed', 'command': self.importar_seed}, {'text': "Exportar Seed", 'command': lambda: self.exportar_seed(self.seed)}, {'text': "Exportar State", 'command': lambda: self.exportar_seed(self.state)})
    for i, arg in enumerate(args1):
      self.comandos1_botoes.append( Button(self.comandos1, fg='black', bg='#7CCD7C', font=('Arial','12'), relief=RIDGE, **arg) )
      self.comandos1_botoes[i].grid(row=0, column=i, padx=20, pady=0)

    self.comandos2 = Frame(self.comandos)
    self.comandos2.grid(row=2, column=0, padx=0, pady=40)
    self.comandos2_botoes = []
    args2 = ({'text': 'Gerar Seed', 'command': self.criar_seed},  {'text': "Limpar quadro", 'command': self.limpar_quadro},  {'text': "Reset Seed", 'command': self.zerar_seed})
    for i, arg in enumerate(args2):
      self.comandos2_botoes.append( Button(self.comandos2, fg='black', bg='#7CCD7C', font=('Arial','12'), relief=RIDGE, **arg) )
      self.comandos2_botoes[i].grid(row=0, column=i, padx=20, pady=0)
    
    self.comandos3 = Frame(self.comandos)
    self.comandos3.grid(row=3, column=0, padx=0, pady=40)
    self.label_inicio = Label(self.comandos3, text='Inicio', font=('Arial','12')).grid(row=0, column=0)
    self.entry_inicio = ttk.Entry(self.comandos3, font=('Arial','12'))
    self.entry_inicio.grid(row=0, column=1)
    self.label_fim = Label(self.comandos3, text='Fim', font=('Arial','12')).grid(row=1, column=0)
    self.entry_fim = ttk.Entry(self.comandos3, font=('Arial','12'))
    self.entry_fim.grid(row=1, column=1)
    self.label_passo = Label(self.comandos3, text='Passo', font=('Arial','12')).grid(row=2, column=0)
    self.entry_passo = ttk.Entry(self.comandos3, font=('Arial','12'))
    self.entry_passo.grid(row=2, column=1)
    self.animar_seed = Button(self.comandos3, text='Animar', fg='black', bg='#7CCD7C', font=('Arial','12'), relief=RIDGE, command=self.geracoes).grid(row=1, column=2, padx=60)

    self.comandos4 = Frame(self.comandos)
    self.comandos4.grid(row=4, column=0, padx=0, pady=40)
    self.comandos4_botoes = []
    args4 = ({'text': '<<', 'command': lambda x=True: self.involuir(passo=x)},  {'text': "<", 'command': self.involuir},  {'text': ">", 'command': self.evoluir_tk},  {'text': ">>", 'command':  lambda x=True: self.evoluir_tk(passo=x)})
    for i, arg in enumerate(args4):
      self.comandos4_botoes.append( Button(self.comandos4, fg='black', bg='#7CCD7C', font=('Arial','12'), relief=RIDGE, **arg) )
      self.comandos4_botoes[i].grid(row=0, column=i, padx=20, pady=0)
  
    self.avisos_frame = Frame(self.master)
    self.avisos_frame.pack(pady=10)
    self.avisos = Label(self.avisos_frame, text='', font=('Arial','16', 'bold'), fg='red')
    self.avisos.pack(pady=10)
  
  
  def alterarn(self):
    n = min(150, int(self.entry_n.get()))
    if n != self.n:
      self.seed = centralizar(self.seed, n) if n > self.n else cortar_seed(self.seed, n)
      self.state = centralizar(self.state, n) if n > self.n else cortar_seed(self.state, n)
      self.n = n
      if n > 25:
        self.criar_grafico()
      else:
        self.criar_botoes() if self.tipo else self.criar_grafico()

  def criar_grafico(self, *args, **kwargs):
    self.print_plt(seed=self.state if self.state_i else self.seed)
    self.tipo = 0
  
  def criar_botoes(self, *args, **kwargs):
    if self.n <= 25:
      for widget in self.grade.winfo_children():
        widget.destroy()
      largura_pixel = int(600 * 0.8 / self.n)
      self.pixel = PhotoImage(width=largura_pixel, height=largura_pixel)
      self.botoes = [[0 for _ in range(self.n)] for _ in range(self.n)]
      seed = self.state if self.state_i else self.seed
      for i in range(self.n):
        for j in range(self.n):
          self.botoes[i][j] = Button(self.grade, image=self.pixel, bg='white' if seed[i][j] else 'black', borderwidth=0, compound="c", command=lambda coor=(i, j): self.clique(coor) )
          self.botoes[i][j].grid(row=i, column=j)
      self.tipo = 1
  
  def clique(self, coor, *args, **kwargs):
    i, j = coor
    self.botoes[i][j]['bg'] = 'white' if self.botoes[i][j]['bg'] == 'black' else 'black'
    if not self.state_i:
      self.seed[i][j] = int(not bool(self.seed[i][j]))
    else:
      self.state[i][j] = int(not bool(self.state[i][j]))
  
  def criar_seed(self, *args, **kwargs):
    self.zerar_seed()
    self.seed = gerar_seed(n=int(self.n), borda=self.n)
    self.print_botoes(seed=self.seed) if self.tipo else self.print_plt(seed=self.seed)

  def print_tk(self):
    seed = self.state if self.state_i else self.seed
    self.print_botoes(seed=seed) if self.tipo else self.print_plt(seed=seed)

  def print_plt(self, seed='', titulo='', *args, **kwargs):
    for widget in self.grade.winfo_children():
      widget.destroy()
    fig = Figure(figsize=(5, 5), dpi=100)
    plot = fig.add_subplot(111)
    plot.pcolor(seed[::-1], cmap=colors.ListedColormap(['black', 'white']))
    plot.axis('off')
    self.grafico = FigureCanvasTkAgg(fig, master=self.grade)
    self.grafico.draw()
    self.grafico.get_tk_widget().configure(highlightthickness=0, borderwidth=0)
    self.grafico.get_tk_widget().pack()
    self.tipo = 0
    
  def print_botoes(self, seed='', titulo='', *args, **kwargs):
    for i in range(len(self.seed)):
      for j in range(len(self.seed[0])):
        self.botoes[i][j].config(bg='white' if seed[i][j] else 'black')

  def geracoes(self):
    inicio = self.entry_inicio.get()
    inicio = max(0, int(inicio)) if inicio != '' else 0
    passo = self.entry_passo.get()
    passo = int(passo) if passo != '' else 1
    fim = self.entry_fim.get()
    fim = int(fim) if fim != '' else inicio + 10 * passo + 1
    seed = evoluir(self.seed, inicio) if inicio else [[i for i in linha] for linha in self.seed]
    self.print_botoes(seed=seed) if self.tipo else self.print_plt(seed=seed)
    self.titulo_grade.config(text=f'Geração {inicio}')
    self.master.after( 1000, lambda: self.geracoes_after( seed, passo, inicio, min(10, int((fim-inicio)/passo)) ) )
    
  def geracoes_after(self, seed, passo, geracao, i):
    if i <= 0:
      self.state = seed
      self.state_i = geracao
      return True
    geracao += passo
    seed = evoluir(seed, passo)
    self.print_botoes(seed=seed) if self.tipo else self.print_plt(seed=seed)
    self.titulo_grade.config(text=f'Geração {geracao}')
    self.master.after(1000, lambda:self.geracoes_after(seed, passo, geracao,i-1))

  def evoluir_tk(self, event='', passo=False, *args, **kwargs):
    passo = max(int(self.entry_passo.get()), 1) if passo else 1
    if self.state_i:
      self.state = evoluir(self.state, passo)
    else:
      self.state = evoluir(self.seed, passo)
    self.print_botoes(seed=self.state) if self.tipo else self.print_plt(seed=self.state)
    self.state_i += passo
    self.titulo_grade.config(text=f'Geração {self.state_i}')
      
  def involuir(self, passo=False, *args, **kwargs):
    passo = max(int(self.entry_passo.get()), 1) if passo else 1
    if (self.state_i - passo) >= 0:
      self.state_i -= passo
      self.state = evoluir(self.seed, self.state_i)
      self.print_botoes(seed=self.state) if self.tipo else self.print_plt(seed=self.state)
      self.titulo_grade.config(text=f'Geração {self.state_i}')
      
  def zerar_seed(self, *args, **kwargs): ## não seria melhor nomear resetar_state
    self.state, self.state_i = [[0 for _ in range(self.n)] for _ in range(self.n)], 0
    self.titulo_grade.config(text=f'Geração {self.state_i}')
    self.print_botoes(seed=self.seed) if self.tipo else self.print_plt(seed=self.seed)
    
  def limpar_quadro(self, *args, **kwargs):
    from tkinter import messagebox 
    if messagebox.askyesno(title="Confirmação", message="Ao limpar o quadro você perderá a seed!\nContinua?"):
      self.seed = [[0 for _ in range(self.n)] for _ in range(self.n)]
      self.zerar_seed()

  def vespelhar_tk(self):
    self.seed = vespelhar(self.seed)
    self.state = vespelhar(self.state)
    self.print_tk()

  def hespelhar_tk(self):
    self.seed = hespelhar(self.seed)
    self.state = hespelhar(self.state)
    self.print_tk()

  def transpor_tk(self):
    self.seed = transpor(self.seed)
    self.state = transpor(self.state)
    self.print_tk()

  def rodar_tk(self, n=1):
    self.seed = rodar(self.seed, n)
    self.state = rodar(self.state, n)
    self.print_tk()

  def importar_seed(self, *args, **kwargs):
    file = filedialog.askopenfilename(initialdir = self.get_initial_dir(),
                                      title = "Buscar seed",
                                      filetypes = (("Text files", "*.txt*"),
                                                  ("all files", "*.*")))
    self.seed = centralizar(importar(file), self.n)
    self.zerar_seed()

  def exportar_seed(self, seed,*args, **kwargs):
    path = filedialog.askdirectory(initialdir = self.get_initial_dir(),
                                   title = "Buscar diretório")
    exportar(seed, path)

  def get_initial_dir(self):
    if "Windows" in platform():
      init = Path.home() / "Downloads"
    else:
      init = "/"
    return(init)
from matplotlib import colors, pyplot as plt
from time import sleep

def print_plt(seed, titulo=None, show=True):
  x = plt.figure(num=1, figsize=(100*len(seed), 100*len(seed[0])))
  plt.pcolor(seed[::-1], cmap=colors.ListedColormap(['black', 'white']))
  plt.title(titulo)
  plt.axis('off')
  if show:
    plt.show()
  try:
    return x
  finally:
    plt.clf()
    plt.figure().clear()
    plt.close()


def print_tk(seed, titulo=''):
  for i in range(len(seed)):
    for j in range(len(seed[0])):
      botoes[i][j]['bg'] = 'white' if seed[i][j] else 'black'

def print_terminal(seed, titulo=''):
  print(titulo.center(len(seed[0]), ' '))
  for linha in seed:
    for elemento in linha:
      print('■' if elemento else ' ', end='')
    print()


## GERAÇÕES (unificar funções abaixo e executar print conforme argumento de tipo)
def geracoes(seed, funcao_imprimir=print_tk, inicio=0, fim=10, passo=1):
  from .evoluir import evoluir
  if (fim-inicio)/passo>10:
    fim = inicio + 10*passo
  seed = evoluir(seed, inicio) if inicio else [[i for i in linha] for linha in seed]
  #funcao_imprimir = print_tk if tipo else print_plt
  
  while(inicio<=fim):
    funcao_imprimir(seed=seed, titulo=f'{inicio}ª geração')
    seed = evoluir(seed, passo)
    inicio += passo
    sleep(5)


def geracoes_tk(seed, inicio=0, fim=10, passo=1):
  from .evoluir import evoluir
  if (fim-inicio)/passo>30:
    fim = inicio + 30*passo
  if inicio:
    seed = evoluir(seed, inicio)
  while (inicio<=fim):
    print_tk(seed, titulo=f'{inicio}ª geração')
    seed = evoluir(seed, passo)
    inicio += passo
    sleep(1)


def geracoes_plt(seed, inicio=0, fim=10, passo=1):
  from .evoluir import evoluir
  if (fim-inicio)/passo>30:
    fim = inicio + 30*passo
  if inicio:
    seed = evoluir(seed, inicio)
  while (inicio<=fim):
    print_plt(seed, titulo=f'{inicio}ª geração')
    seed = evoluir(seed, passo)
    inicio += passo
    sleep(1)

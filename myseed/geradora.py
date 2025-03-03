from random import randint, uniform
import numpy as np

def centralizar(seed, f=100):
  if f<max(len(seed), len(seed[0])):
    return seed
  quant_zeros = int((f-len(seed[0]))/2)
  final = [[0 for i in range(quant_zeros)] + linha + [0 for i in range(f - quant_zeros - len(linha))] for linha in seed]
  quant_linhas = int((f-len(seed))/2)
  return [[0 for i in range(f)] for j in range(quant_linhas)] + final + [[0 for i in range(f)] for j in range(f - quant_linhas - len(seed))]

def gerar_seed(n, m=None, borda=0):
  if m is None:
    m = n
  return np.random.randint(2, size=(n, m))

'''
def gerar_seed(n=15, borda=25):
  from random import randint, uniform
  final = []
  for i in range(n):
    n_nucleo = randint(3,6)
    p = uniform(0.4, 0.6)
    nucleo = [[int(uniform(0,1) <= p) for i in range(n_nucleo)] for j in range(n_nucleo)]
  
    final += [[0 for i in range(n)] for j in range(randint(1,2))]
    inicio = randint(0, n-len(nucleo[0]))
    for cada in nucleo:
      final.append([0]*inicio + cada + [0]*(n-inicio-len(cada)))
    if len(final) >= n-7:
      break
  final += [[0 for i in range(n)] for j in range(n - len(final))]
  return centralizar(final, borda)
'''

def redimensionar_seed(seed, borda=25):
  return [( [int(v) for i, v in enumerate(linha) if i<borda] + [0 for _ in range(max(0, borda - len(linha)))] ) for j, linha in enumerate(seed) if j<borda] + [[0 for _ in range(borda)] for _ in range(max(0, borda - len(seed)))]


def cortar_seed(seed, borda=25):
  if borda>min(len(seed), len(seed[0])):
    return seed
  inicio_r = int((len(seed[0])-borda)/2)
  inicio_c = int((len(seed)-borda)/2)
  return [linha[inicio_r: inicio_r+borda] for linha in seed[inicio_c: inicio_c+borda]]



'''
def cortar_seed(seed, borda=25):
  if ( (len(seed)<borda) and (len(seed[0])<borda) ):
    return seed
  #return [( [int(v) for i, v in enumerate(linha) if i<borda] + [0 for _ in range(max(0, borda - len(linha)))] ) for j, linha in enumerate(seed) if j<borda] + [[0 for _ in range(borda)] for _ in range(max(0, borda - len(seed)))]

def centralizar0(seed, f=100):
  if f<max(len(seed), len(seed[0])):
    return seed
  final = []
  quant_zeros = int((f-len(seed[0]))/2)
  for i,v in enumerate(seed):
    final.append([0]*quant_zeros + v + [0]*(f-quant_zeros-len(seed)))
  quant_linhas = int((f-len(seed))/2)
  return [[0 for i in range(f)]]*quant_linhas + final + [[0 for i in range(f)]]*(f - quant_linhas - len(seed))
'''

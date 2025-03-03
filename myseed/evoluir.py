
#Quand l'horizon s'est fait trop noir
#Tous les oiseaux sont partis
#Sur les chemins de l'espoir

import numpy as np
from scipy.signal import convolve2d

def evoluir(seed, r=1):
  import numpy as np
  from scipy.signal import convolve2d
  seed = [[i for i in j] for j in seed]
  for i in range(r):
    conv = convolve2d(np.array(seed), [[1,1,1],[1,0,1],[1,1,1]], mode='same')
    for i in range(len(seed)):
      for j in range(len(seed[i])):
        seed[i][j] = int(2 <= conv[i][j] <= 3) if seed[i][j] else int(conv[i][j] == 3)
  return seed


## Com funções próprias; pronto; implementar depois
def radial(seed, raio=1):
  seed2 = [[cada for cada in linha] for linha in seed]
  conv = [[0 for _ in range(len(seed[0]))] for _ in range(len(seed))]
  
  seed2 = [[0 for _ in range(len(seed2[0])+(2*raio))]]*raio + seed2 + [[0 for _ in range(len(seed2[0])+2*raio)]]*raio
  for i in range(raio, len(seed2)-raio):
    seed2[i] = [0 for _ in range(raio)] + [h for h in seed2[i]] + [0 for _ in range(raio)]
  print('.')
  for i in range(raio, len(seed2)-raio):
    for j in range(raio, len(seed2[i])-raio):
      superior = seed2[i-raio][j-raio+1: j+raio]
      inferior = seed2[i+raio][j-raio+1: j+raio]
      direita = []
      esquerda = []
      for k in range(raio*2+1):
        esquerda.append(seed2[i-raio+k][j-raio])
        direita.append(seed2[i-raio+k][j+raio])
      conv[i-raio][j-raio] += sum(superior + inferior + esquerda + direita)
  return conv


def evoluir2(seed):
  conv = radial(seed)
  novo = [[0 for _ in range(len(seed[0]))] for _ in range(len(seed))]
  for i in range(len(novo)):
    for j in range(len(novo[i])):
      novo[i][j] = int(2 <= conv[i][j] <= 3) if seed[i][j] else int(conv[i][j] == 3)
  return novo

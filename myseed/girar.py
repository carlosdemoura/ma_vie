
def vespelhar(seed):
  return [[linha[len(linha)-1-i] for i in range(len(linha))] for linha in seed]


def hespelhar(seed):
  return [seed[len(seed)-1-i] for i in range(len(seed))]


def transpor(seed):
  girado = [[i for i in range(len(seed[0]))] for j in range(len(seed))]
  for i, linha in enumerate(seed):
    for j, v in enumerate(linha):
      girado[i][j] = seed[j][i]
  return girado


def rodar(seed, n=1):
  for i in range(n%4):
    seed = vespelhar(transpor(seed))
  return seed

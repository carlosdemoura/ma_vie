from os.path import exists

def importar(file, *args, **kwargs):
  with open(file, 'r') as f:
    seed = [[int(i) for i in linha[:-1]] for linha in f.readlines()]
  return seed


def exportar(seed, path, *args, **kwargs):
  texto = ""
  for linha in seed:
    texto += ''.join([str(i) for i in linha]) + '\n'
  file = f"{path}/seed.txt"
  cont = 0
  while exists(file):
    cont += 1
    file = f"{path}/seed-{cont}.txt"
  print(file)
  with open(file, 'w') as f:
    f.write(texto)

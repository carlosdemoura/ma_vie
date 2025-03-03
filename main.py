
from tkinter import Tk, mainloop
from myinter import Home, Jogo

def main():
  root = Tk()
  root.iconbitmap("./imagens/vida.ico")
  root.state('zoomed')
  Home(root)
  mainloop()

main()

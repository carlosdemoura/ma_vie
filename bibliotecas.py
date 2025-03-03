
from tkinter import *
from tkinter import ttk, filedialog, messagebox 
from os.path import exists
from random import randint, uniform
from scipy.signal import convolve2d
import numpy as np
from time import sleep
from matplotlib import colors, pyplot as plt
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

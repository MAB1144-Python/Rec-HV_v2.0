# animated_line_plot.py

from random import randint

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# create empty lists for the x and y data
x = []
y = []



x_d = []
y_d = []
graficar, = plt.plot([],[])
def funcion(x):
   x_d.append(x)
   y_d.append(y)
   graficar.set_data(x_d,y_d)
   return graficar


# create the figure and axes objects
fig, ax = plt.subplots(figsize = (15,4))

# run the animation
ani = FuncAnimation(fig, funcion, frames=np.linspace(0,7,500), blit=True)

plt.show()

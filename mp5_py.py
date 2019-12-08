import numpy as np
import matplotlib.pyplot as plt
from math import *

n = np.linspace(0,199,200)

def mp5(x):
    y = np.zeros(200)
    for z in n:
        z = int(z)
        if z == 0:
            y[z] = -1.5*x[z] + 2*x[z+1] - 0.5*x[z+2]
        elif z > 0 and z <= 198:
            y[z] = 0.5*x[z+1] - 0.5*x[z-1]    
        elif z == 199:
            y[z] = 1.5*x[z] - 2*x[z-1] + 0.5*x[z-2]

    plt.plot(n,x,label = "x(n)", color = "red")
    plt.plot(n,y,label = "y(n)", color = "purple")
    plt.legend()

# Type mp5(np.sin((3*pi*n)/100)) in the console to test
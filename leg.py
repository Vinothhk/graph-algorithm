import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import sympy as sp
from math import pi
""" fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = ax.plot([], [], 'r') """
coords_x = []
coords_y = []
theta1, theta2 = sp.symbols('theta1 theta2')
origin_x = 0.0
origin_y = 0.0
coords_x.append(origin_x)
coords_y.append(origin_y)

joint1_x = 1.1* np.sin(np.deg2rad(35))
joint1_y = 1.1* -np.cos(np.deg2rad(35))
coords_x.append(joint1_x)
coords_y.append(joint1_y)

joint2_x = joint1_x - (1.1 * np.sin(np.deg2rad(35)))
joint2_y = joint1_y - (1.1 * np.cos(np.deg2rad(35)))  
coords_x.append(joint2_x)
coords_y.append(joint2_y)
print(coords_x)
print(coords_y)
plt.plot(coords_x,coords_y,'-k')
plt.show()            
""" def init():
    ax.set_xlim(0, 2*np.pi)
    ax.set_ylim(-1, 1)
    return ln,

def update(frame):
    xdata.append(frame)
    ydata.append(np.sin(frame))
    ln.set_data(xdata, ydata)
    return ln,

ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 128),
                    init_func=init, blit=True) """

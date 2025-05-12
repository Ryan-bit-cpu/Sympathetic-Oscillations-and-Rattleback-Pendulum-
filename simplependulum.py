# Activate Qu-tip conda environment to run the code below
# Simple Pendulum without friction code

import numpy as np
from mpl_toolkits import mplot3d
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
plt.style.use('seaborn-poster')

#Define the variables
l = 0.27			# The length of the pendulum in meters.
w = 9.81/l			# Gravitational acceleration is 9.81 m/s^2.
x = []				# Store the data in an array for x and y
y = []

figure, ax = plt.subplots()

#Setting the limits for x and y on the graph
ax.set_xlim(0, 50)
ax.set_ylim(-40, 40)

#Plotting a single graph
line,  = ax.plot(0, 0) 

#Performing the animation
def animation_function(i):
    x.append(i)
    y.append(-(w)*np.sin(i))

    line.set_xdata(x)
    line.set_ydata(y)
    return line,

animation = FuncAnimation(figure,
                          func = animation_function,
                          frames = np.arange(0, 16*np.pi, 0.1),			# How long you want the simple pendulum to oscillate. 
                          interval = 16*np.pi)
                          
# Set axes labels and title
ax.set_xlabel('time (seconds)', labelpad=20)
ax.set_ylabel('Amplitude (meters)', labelpad=20)
ax.set_title('A Simple Pendulum')

plt.show()

# Activate Qu-tip conda environment to run the code below
# Coupled Pendulum

import numpy as np
from mpl_toolkits import mplot3d
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
plt.style.use('seaborn-poster')

#Define the variables. Gravitational acceleration is 9.81 m/s^2.
l1 = 2				# The length of pendulum 1 in meters.
l2 = 2				# The length of pendulum 2 in meters.
w1 = 9.81/l1			# Natural frequency of pendulum 1.
w2 = 9.81/l2			# Natural frequency of pendulum 2.
x = []				# Intialize x array for storage
y = []				# Intialize y array for storage

figure, ax = plt.subplots()

#Setting the limits for x and y
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

#Plotting a single graph
line,  = ax.plot(0, 0) 

#Performing the animation
def animation_function(i):
    y.append(0.5*(np.cos(i*w1*(1-(0.3)**2)**0.5) - np.cos(-i*(w2**2 + (1.01*w1)**2)**0.5)))		# The function of the coupled pendulum
    x.append(0.5*(np.cos(i*w1*(1-(0.3)**2)**0.5) + np.cos(-i*(w2**2 + (1.01*w1)**2)**0.5)))

    line.set_xdata(x)
    line.set_ydata(y)
    return line,

animation = FuncAnimation(figure,
                          func = animation_function,
                          frames = np.arange(0, 20*np.pi, 0.1),			# How long you want the coupled pendulum to oscillate. 
                          interval = 20*np.pi)
                          
# Set axes labels and title
ax.set_xlabel('Amplitude of Penedulum 1 (meters)', labelpad=20)
ax.set_ylabel('Amplitude of Penedulum 2 (meters)', labelpad=20)
ax.set_title('A Coupled Pendulum without Friction')

plt.show()

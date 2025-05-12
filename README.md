## Introduction ##

The python code is used to visualize through an animation using the matlibplot, numpy, and mpl_toolkits libraries. The mathematical formula of a coupled penedulum (Sympathetic Oscillations) can be described as:

/[ x(t) = 0.5*(cos(i*w1*(1-(0.3)^2)^0.5) - cos(-i*(w2^2 + (1.01*w1)^2)^0.5)) /]

The user can derive the formula above using Lagrangian Mechanics, and the Fourier Transform formula to convert positions of the hanging masses to frequency space. The deviation is long to write out by hand. The w1 and w2 for two hanging masses coupled together 
by some string or rod is the natural frequency of the each hanging mass. Changing the natural frequency or length of the hanging masses in the python code changes the ampitudes as a function of time of the two hanging masses, setting the length of the hanging masses to l1 = 2 and l2 = 2 or 5, the shape is a diamond or rhombus. 
If we change lengths l1 = 8 and l2 = 5, then the ampitudes creates an oscillating "C" image. 

### Python Installation ###

1.) Install Conda Environment:

        conda install -c qutip_env

2.) Install qutip within the newly created qutip vitual environment in conda

        pip install qutip

(Optional) You may need to install additional libraries using pip install

        pip install matlibplot

        pip install numpy

        pip install mpl_toolkits


### Link to Youtube Video ###

I have built a coupled pendulum and rattleback pendulum using my Dad's old carpentry tools out of cedar and walnut that has been milled. In the videos, I used a camping rope and 2 lbs. fishing weights, a nail, and 10 washers. 
The nail and ten washers of the rattleback pendulum shifts the center mass of the hanging mass off of the center of the hanging mass. The hanging mass oscillates clockwise, then oscillates counter-clockwise, then back to clockwise, and so on till friction slows the motion down.

https://youtu.be/TzDIh8okEC8

https://youtu.be/4wLvX1RgvFw

Rattleback Pendulum: https://youtu.be/Fa8OhN-7NiA

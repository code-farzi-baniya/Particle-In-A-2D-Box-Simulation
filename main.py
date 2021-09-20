import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

n_x = int(input('Enter the principle Quantum Number ,nx : '))   # principle quantum number nx
n_y = int(input('Enter the principle Quantum Number ,ny : '))   # principle quantum number ny 

Type_plot = input('Enter the type of plot you want - Surface, Wireframe, Contour : ')

l = 10 ** -9 #length of the particle in the box, manually set in the code

N = 100 # Meshsize
#set our 'x' and 'y' arrays
x,y = np.linspace(0,l,N),np.linspace(0,l,N)  #generate a(100) linearly spaced array from 0 to 'l'

# 'l' is preset variable
N = (2/l) #normalization constant for  Particle in a 2d box

#Asin(kx) --> Asin(n(pi)x/l)
def psi_3d(a,b):
    # defination of our wave function that fits the limitations
    psi_3d = N*(np.sin((n_x * np.pi * a)/l) * np.sin((n_y * np.pi * b)/l)) 
    return psi_3d 

# Making our wavefunction in the Z-Axis

X,Y = np.meshgrid(x,y) #for 'x' and  'y' respectively, meshgrid sets up a matrix for the two variables 'X' & 'Y' (capitals), 'x' and 'y' are preset arrays

psi = np.array([psi_3d(x,y) for x,y in zip(np.ravel(X),np.ravel(Y))])  #ravel returns a continuous flattened array,
#zip() is on interator tuple which joins similar objects together,
#psi_3d(x,y) calls the def function, then sets the a,b values as x,y values found in the Zip() brackets,
# this is all saved as an array in the variable 'Psi'

Psi = psi.reshape(X.shape) # Decreases the number of values in 'psi' from 10000 to 100 in comparison to 'X',
P_Density = Psi**2   # Probability Density 
#X.shape looks at the shape (no. of values) in 'X' then .reshape changes the shape of the array without changing it's data, variable saved as 'Psi'

#Plot our 2d box onto a 3d plane
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d') # generates a different plot for each graph, includes the size of the graph, makes dimension of the graph '3d'

if Type_plot == 'surface' or Type_plot == 'Surface' :
    ax.plot_surface(X, Y, Psi,cmap = plt.cm.winter_r) #includes the variables required to plot graph (x,y,z) , plots 'X' vs 'Y'  vs 'A*Psi'
elif Type_plot == 'contour' or Type_plot == 'Contour' :
    ax.contourf(X, Y, Psi)
elif Type_plot == 'wireframe' or Type_plot == 'Wireframe' :
    ax.plot_wireframe(X, Y, Psi,color = 'xkcd:sea green' )

#includes info of the curve

#labels our x,y,z axis
plt.xlabel('X')
plt.ylabel('Y')
ax.set_zlabel('Psi')
plt.title('Wave Function of Particle in a 2D Box for nx =  '+str(n_x)+' ,ny = '+str(n_y),color='red')                              # gives the graph a title
plt.savefig('2D Box Wave function.png')  

#Plot our 2d box onto a 3d plane
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d') #generates a different plot for each graph, includes the size of the graph, makes dimension of the graph '3d'
if Type_plot == 'surface' or Type_plot == 'Surface' :
    # ax.plot_surface(X, Y, P_Density,cmap = 'magma') #includes the variables required to plot graph (x,y,z) , plots 'X' 
    ax.plot_surface(X, Y, P_Density,cmap = plt.cm.winter_r)
    # vs 'Y' vs 'A*Psi'
elif Type_plot == 'contour' or Type_plot == 'Contour' :
    ax.contourf(X, Y, P_Density)
elif Type_plot == 'wireframe' or Type_plot == 'Wireframe' :
    ax.plot_wireframe(X, Y, P_Density,color = 'xkcd:coral')

#includes info of the curve 
#labels our x,y,z axis
plt.xlabel('X')
plt.ylabel('Y')
ax.set_zlabel('Psi^2')
plt.title('Probability Density of Particle in a 2D Box for nx =  '+str(n_x)+' ,ny = '+str(n_y),color='red') #gives the graph a title
plt.savefig('2D box Probability Density.png')   #saves the plot as well for us
plt.show()
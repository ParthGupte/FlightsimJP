import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D as ax
fig=plt.figure()
axe=plt.axes(projection='3d')
x=np.array([0,1,2,3])
y=np.array([0,1,2,3])
z=np.array([0,1,2,3])
axe.plot3D(x,y,z)
plt.show()

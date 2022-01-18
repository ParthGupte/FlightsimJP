import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D as ax
fig=plt.figure()
axe=plt.axes(projection='3d')
import vectors as vec
import math 
import time
import os
import objects as objs
import environment as env
import numpy as np

"""class object():
    def __init__(self, radius, mass, velocity, position):
        self.object_type = 'Sphere'
        self.object_radius = radius
        self.mass = mass
        self.velocity = velocity
        self.position = position
    def projection_area(self):
        return math.pi * ((self.object_radius)**2)
    def drag(self, environment,time):
        velocity_rel = self.velocity - environment.wind(time)
        drag = ((1/2) * environment.drag_coefficient * environment.density * self.projection_area() * vec.mod(velocity_rel)) * (-1) * (velocity_rel)
        return drag

class environment():
    def __init__(self, density):
        self.density = density
        self.drag_coefficient = 0.47
        self.g = -9.8 * vec.j
    def wind(self, time):
        return -1.*vec.i+1.*vec.j+0.*vec.k"""

 
def trajectory(objct, environment):#objct cause object is a reserve word even though it works its risky 
    to = time.time()
    t = to

    with open(r"coord1.txt", 'a') as file:
            file.write(str(list(objct.position)) +'\n')
            file.close()
    while vec.dot(objct.position, vec.k) >= 0:
        dt = time.time() - t
        t = time.time()
        objct.velocity = objct.velocity + (objct.mass*environment.g + objct.drag(environment, t)) * (dt/objct.mass)
        objct.position = objct.position + objct.velocity * dt
        with open(r"coord1.txt", 'a') as file:
            file.write(str(list(objct.position)) +'\n')
            file.close()
          
    with open(r"coord1.txt", 'r') as file:
        data = file.readlines()
    graph(data)
def graph(data):
        x = []
        y = []
        z = []
        for i in data:
            L = eval(i)
            x.append(L[0])
            y.append(L[1])
            z.append(L[2])
        xs=np.array(x[:-1])
        ys=np.array(y[:-1])
        zs=np.array(z[:-1])
        plt.plot(xs,ys,zs)
        plt.show()
def input_vector(name, dimension):# what is this redundant function? i hate it
    v = []
    print('{} components: '.format(name))
    for i in range(0, dimension):
        v.append(float(input('\t{}:'.format(i+1))))
    return vec.vec(v)
def main():
    radius = 1 #float(input('Radius: '))
    mass = 1 #float(input('Mass: '))
    velocity = input_vector('Velocity', 3)
    position = input_vector('Position', 3)
    density = 1.225 #float(input('Fluid Density: '))
    obj = objs.sphere(radius, mass, velocity, position)
    envrmnt = env.environment(density)#i am uncomfortable with 2 different things having the same name (can cause big problems) so i changed it

    trajectory(obj, envrmnt)
    os.system('type nul > coord1.txt')
    os.remove("coord1.txt")
main()

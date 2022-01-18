import numpy as np
import math as mt
def vec(L): #converts list to vector
    return np.array(L)

def dot(a,b): #dot product
    return sum(a*b)

def mod(V): #returns magnitude of vector
    return mt.sqrt(dot(V,V))

def cross(a,b): #cross product
    [a1,a2,a3]=a
    [b1,b2,b3]=b
    C=vec([(a2*b3)-(b2*a3),(b1*a3)-(a1*b3),(a1*b2)-(b1*a2)])
    return C

i=vec([1,0,0])
j=vec([0,1,0])
k=vec([0,0,1])

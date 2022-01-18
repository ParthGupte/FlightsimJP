import numpy as np
import vectors as v
import time as tm
import matplotlib.pyplot as pl
ro=v.vec([0,0,0])
r1=ro
D=v.vec([0,0,0])
m=1
g=v.vec([0,-9.8,0])
uo=v.vec(eval(input("u= ")))
u1=uo
to=tm.time()
t=to
while v.dot(r1,v.j)>=0:
    dt=tm.time()-t
    t=tm.time()
    print(dt)
    u2=u1+(m*g+D)*(dt/m)
    r2=r1+u1*dt
    print(r2,u2,t)
    file=open(r"G:\Parth notes\12th standard\Informatics Practices\Flight sim JP\coord1.txt",'a')
    file.write(str(list(r1))+'\n')
    file.close()
    u1=u2
    r1=r2
file=open(r"G:\Parth notes\12th standard\Informatics Practices\Flight sim JP\coord1.txt",'r')
data=file.readlines()
print(data)
x=[]
y=[]
for i in data:
    L=eval(i)
    x.append(L[0])
    y.append(L[1])
pl.plot(x,y)
pl.show()
    
    

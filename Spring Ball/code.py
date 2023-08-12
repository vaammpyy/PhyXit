import numpy as np
from vpython import *

m1=1
m2=1
k=10


canvas(width=1000,height=600)

p1=sphere(pos=vector(0,1,0),radius=0.5,color=color.yellow,mass=m1,make_trail=True,retain=20,force=vector(0,0,0))
p2=sphere(pos=vector(0,-1,0),radius=0.5,color=color.green,mass=m1,make_trail=True,retain=20,force=vector(0,0,0))
p3=sphere(pos=vector(3,0,0),radius=0.5,color=color.cyan,mass=m2,make_trail=True,retain=20,force=vector(0,0,0))

r12=helix(pos=p1.pos,axis=p2.pos-p1.pos,radius=0.25,stiff=k,coils=10)
r23=helix(pos=p2.pos,axis=p3.pos-p2.pos,radius=0.25,stiff=k*0.1,coils=5)
r31=helix(pos=p3.pos,axis=p1.pos-p3.pos,radius=0.25,stiff=k*100,coils=20)

com=m1*vector(-1,1,0)+m1*vector(-1,-1,0)+m2*vector(3,0,0)
com=com/(2*m1+m2)

L12_0=p1.pos-p2.pos
L23_0=p2.pos-p3.pos
L31_0=p3.pos-p1.pos


p1.velo=vector(10,0,0)
p2.velo=vector(0,-10,10)
p3.velo=-m1*(p1.velo+p2.velo)/m2

input("Press Enter to start")
i=0
dt=0.01

while (i<100000):
    rate(100)
    p1.pos=p1.pos+p1.velo*dt
    p2.pos=p2.pos+p2.velo*dt
    p3.pos=p3.pos+p3.velo*dt

    p1.force=-r12.stiff*((p1.pos-p2.pos)-L12_0)+r31.stiff*((p3.pos-p1.pos)-L31_0)
    p2.force=-r23.stiff*((p2.pos-p3.pos)-L23_0)+r12.stiff*((p1.pos-p2.pos)-L12_0)
    p3.force=-r31.stiff*((p3.pos-p1.pos)-L31_0)+r23.stiff*((p2.pos-p3.pos)-L23_0)

    p1.velo+=p1.force*dt/m1
    p2.velo+=p2.force*dt/m1
    p3.velo+=p3.force*dt/m2

#    p1.velo=cross(omega,p1.pos-com)
#    p2.velo=cross(omega,p2.pos-com)
#    p3.velo=cross(omega,p3.pos-com)


    r12.pos=p1.pos
    r12.axis=p2.pos-p1.pos
    r23.pos=p2.pos
    r23.axis=p3.pos-p2.pos
    r31.pos=p3.pos
    r31.axis=p1.pos-p3.pos

    i+=1

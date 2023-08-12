#def euler(x,dt):

import numpy as np

def projectile(v,theta,h,dt,t_end):
    x=0
    y=h
    theta=2*180/np.pi
    vx=v*np.cos(theta)
    vy=v*np.sin(theta)
    t=0
    i=0
    ax=0
    ay=-9.81
    fle= open("data.txt","w+")
    while (t<t_end):
        x+=vx*dt
        y+=vy*dt
        vx+=ax*dt
        vy+=ay*dt
        if y<0:
            y=0
            vy=0
            ay=0
        fle.write(f"{i} {t} {x} {y} {vx} {vy}\n")
        i+=1
        t+=dt
    fle.close()

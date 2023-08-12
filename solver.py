#def euler(x,dt):

import numpy as np

def projectile(v,theta,h,dt,t_end):
    x=0
    y=h
    theta=np.pi/180*theta
    vx=v*np.cos(theta)
    vy=v*np.sin(theta)
    t=0
    i=0
    ax=0
    ay=-9.81
    fle= open("data.txt","w+")
    while (t<t_end):
        fle.write(f"{i} {t} {x} {y} {vx} {vy}\n")
        x+=vx*dt
        y+=vy*dt
        vx+=ax*dt
        vy+=ay*dt
        if y<0:
            y=0
            vy=0
            ay=0
        i+=1
        t+=dt
    fle.close()

def simple_pendulum(m,l,th,dth,r,dt,t_end):
    th=np.pi/180*th
    dth=np.pi/180*dth
    t=0
    i=0
    t=0
    g=-9.81
    k=0.5*m*dth**2*l
    p=m*g*(l*np.cos(th))
    fle= open("data.txt","w+")
    x=l*np.sin(th)
    y=-l*np.cos(th)
    while (t<t_end):
        fle.write(f"{i} {t} {l} {th} {dth} {x} {y} {k} {p}\n")
        th+=dth*dt
        dth+=m*g*np.sin(th)*dt+(-dth)*np.abs(dth)*r**2/m*dt
        k=0.5*m*dth**2*l
        p=m*g*(l*np.cos(th))
        x=l*np.sin(th)
        y=-l*np.cos(th)
        i+=1
        t+=dt
    fle.close()

def spring_block(m,ks,x0,x,vx,mu,dt,t_end):
    t=0
    i=0
    g=9.81
    k=0.5*m*vx**2
    p=0.5*k*(x0-x)**2
    y=0
    fle= open("data.txt","w+")
    while (t<t_end):
        fle.write(f"{i} {t} {x0} {x} {y} {vx} {k} {p}\n")
        x+=vx*dt
        vx+=ks/m*((x0-x))*dt+(-np.sign(vx))*mu*g*dt
        # vx+=ks/m*((x0-x))*dt
        k=0.5*m*vx**2
        p=0.5*ks*(x0-x)**2
        i+=1
        t+=dt
    fle.close()

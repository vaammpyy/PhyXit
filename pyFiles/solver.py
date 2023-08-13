#def euler(x,dt):

import numpy as np
from random import choice

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
    fle= open("./tmp/data.txt","w+")
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
    fle= open("./tmp/data.txt","w+")
    x=l*np.sin(th)
    y=-l*np.cos(th)
    while (t<t_end):
        fle.write(f"{i} {t} {l} {th} {dth} {x} {y} {k} {p}\n")
        th+=dth*dt
        dth+=m*g*np.sin(th)*dt-dth*np.abs(dth)*r**2/m*dt
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
    fle= open("./tmp/data.txt","w+")
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

def random_walker(n,steps,a):
    n = int(n)
    x=[0]*n
    y=[0]*n
    step=0
    r=np.linspace(-1,1,1000)
    dictionary={'frame':[],'x':[],'y':[]}
    while (step<steps):
        dictionary["frame"].append(step)
        dictionary['x'].append(x)
        dictionary['y'].append(y)
        p=0
        x=[]
        y=[]
        while p<n:
            x.append(dictionary['x'][step][p]+choice(r)*a)
            y.append(dictionary['y'][step][p]+choice(r)*a)
            p+=1
        step+=1
    np.save("./tmp/data.npy",dictionary)

def charge_interaction(d,q1,q2,mp,qp,xp,yp,vxp,vyp,dt,t_end):
    q1_x=-d/2
    q2_x=+d/2
    q1_y=q2_y=0
    t=0
    i=0
    k=0.5*mp*(vxp**2+vyp**2)
    p=(q1*qp)/(np.sqrt((q1_x-xp)**2+yp**2))+(q2*qp)/(np.sqrt((q2_x-xp)**2+yp**2))
    fle= open("./tmp/data.txt","w+")
    while t<t_end:
        fle.write(f"{i} {t} {q1} {q1_x} {q1_y} {q2} {q2_x} {q2_y} {qp} {xp} {yp} {vxp} {vyp} {k} {p}\n")
        r1=np.sqrt((q1_x-xp)**2+yp**2)
        r2=np.sqrt((q2_x-xp)**2+yp**2)
        if r1<0.01:
            r1=0.01
        if r2<0.01:
            r2=0.01
        f1=qp*q1/r1**2
        b1=q1_x-xp
        p=yp
        if abs(b1)<0.01:
            b1=np.sign(b1)*0.01
        th1=np.arctan(p/b1)
        f1_x=np.cos(th1)*f1
        f1_y=np.sin(th1)*f1

        f2=qp*q2/r2**2
        b2=q2_x-xp
        p=yp
        if abs(b2)<0.01:
            b2=np.sign(b2)*0.01
        th2=np.arctan(p/b2)
        f2_x=np.cos(th2)*f2
        f2_y=np.sin(th2)*f2
        fx=f1_x+f2_x
        fy=f1_x+f2_y
        xp+=vxp*dt
        yp+=vyp*dt
        vyp+=fx/mp*dt
        vyp+=fy/mp*dt
        k=0.5*mp*(vxp**2+vyp**2)
        p=(q1*qp)/(np.sqrt((b1)**2+yp**2))+(q2*qp)/(np.sqrt((b2)**2+yp**2))
        i+=1
        t+=dt
    fle.close()
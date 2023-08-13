from pyFiles.solver import *
from pyFiles.plotter import *


def projectile_motion(v, theta, h, dt, t_end):
    projectile(v, theta, h, dt, t_end)
    plot_projectile()
    make_movie()


def single_pendulum_motion(m, l, th, dth, r, dt, t_end):
    simple_pendulum(m, l, th, dth, r, dt, t_end)
    plot_simple_pendulum()
    make_movie()


def spring_block_motion(m, ks, x0, x, vx, mu, dt, t_end):
    spring_block(m, ks, x0, x, vx, mu, dt, t_end)
    plot_spring_block()
    make_movie()


def random_walker_motion(n, steps, a):
    random_walker(n, steps, a)
    plot_random_walker()
    make_movie()

def charge_interaction_motion(d,q1,q2,mp,qp,xp,yp,vxp,vyp,dt,t_end):
    charge_interaction(d,q1,q2,mp,qp,xp,yp,vxp,vyp,dt,t_end)
    plot_charge_interaction()
    make_movie()

# charge_interaction_motion(2,-10,3,2,1,0,0,1,-1,0.1,5)


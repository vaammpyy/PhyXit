from solver import *
from plotter import *

def projectile_motion(v,theta,h,dt,t_end):
    projectile(v,theta,h,dt,t_end)
    plot_projectile()
    make_movie()
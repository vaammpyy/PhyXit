import matplotlib.pyplot as plt
import os
import pandas as pd

import subprocess

def make_movie_gnuplot():
    #cmd = "ffmpeg -framerate 20 -pattern_type  glob -i /output/*.png c_change_bif.mp4"
    cmd = "ffmpeg -framerate 20 -pattern_type glob -i 'output/*.png' -c:v libx264 -pix_fmt yuv420p out.mp4"
    os.system(cmd)
    os.system("rm -r output/*.png")

def plot_projectile_gnuplot():
    data = pd.read_csv('data.txt', delimiter=' ').to_numpy().T
    frames=data[0]-1
    t=data[1]
    x=data[2]
    y=data[3]
    vx=data[4]
    vy=data[5]

    os.system("mkdir output")

    for frame in frames:
        os.system("awk 'FNR == %d {print $0}' data.txt > outputfile"%(int(frame)))
        cmd="""
gnuplot <<- EOF
set terminal png size 1200,1000
set output "output/{:05d}.png"
set multiplot title "Projectile Motion"
set nokey

set origin 0.0, 0.5
set size 1.0, 0.45
set title "Position of the particle"
set xlabel "x-axis"
set ylabel "y-axis"
plot "data.txt" using 3:4 with lines lw 2.5 lc 22 title 'Position', \
    "outputfile" using 3:4 pt 7 ps 3

unset xlabel
unset ylabel
set origin 0.0, 0.0
set size 0.25, 0.45
set title "X position vs time"
plot "data.txt" using 2:3 with lines lw 2.5 lc 22 title 'X vs T' , \
    "outputfile" using 2:3 pt 7 ps 3

set origin 0.25, 0.0
set size 0.25, 0.45
set title "Y position vs time"
plot "data.txt" using 2:4 with lines lw 2.5 lc 22 title 'Y vs T' , \
    "outputfile" using 2:4 pt 7 ps 3

set origin 0.5, 0.0
set size 0.25, 0.45
set title "Velocity along x-axis vs time"
plot "data.txt" using 2:5 with lines lw 2.5 lc 22 title 'Vx vs T' , \
    "outputfile" using 2:5 pt 7 ps 3

set origin 0.75, 0.0
set size 0.25, 0.45
set title "Velocity along y-axis vs time"
plot "data.txt" using 2:6 with lines lw 2.5 lc 22 title 'Vy vs T' , \
    "outputfile" using 2:6 pt 7 ps 3

unset multiplot
EOF
    """.format(int(frame))
        os.system(cmd)
        
def plot_pendulum_gnuplot():
    data = pd.read_csv('data.txt', delimiter=' ').to_numpy().T
    frames=data[0]-1
    t=data[1]
    x=data[2]
    y=data[3]
    vx=data[4]
    vy=data[5]

    os.system("mkdir output")

    for frame in frames:
        os.system("awk 'FNR == %d {print $0}' data.txt > outputfile"%(int(frame)))
        cmd="""
gnuplot <<- EOF
set terminal png size 1200,1000
set output "output/{:05d}.png"
set multiplot title "Projectile Motion"
set nokey

set origin 0, 0.667
set size 0.5, 0.333
set title "Position of the particle"
set xlabel "x-axis"
set ylabel "y-axis"


#set arrow 1 from 0,0 to x1,y1 nohead ls 8 lw 2
plot "data.txt" using 6:7 with lines lw 2.5 lc 22 title 'Position', \
    "outputfile" using 6:7 pt 7 ps 3

unset xlabel
unset ylabel

set origin 0.5, 0.667
set size 0.5, 0.333
set title "Position of the particle"
plot "data.txt" using 2:4 with lines lw 2.5 lc 22 title 'Position', \
    "outputfile" using 2:4 pt 7 ps 3
    

set origin 0, 0.333
set size 0.5, 0.333
set title "X position vs time"
plot "data.txt" using 2:5 with lines lw 2.5 lc 22 title 'X vs T' , \
    "outputfile" using 2:5 pt 7 ps 3

set origin 0.5, 0.333
set size 0.5, 0.333
set title "Y position vs time"
plot "data.txt" using 2:8 with lines lw 2.5 lc 22 title 'Y vs T' , \
    "outputfile" using 2:8 pt 7 ps 3

set origin 0, 0
set size 0.5, 0.333
set title "Velocity along x-axis vs time"
plot "data.txt" using 2:9 with lines lw 2.5 lc 22 title 'Vx vs T' , \
    "outputfile" using 2:9 pt 7 ps 3

set origin 0.5, 0
set size 0.5, 0.333
set title "Velocity along y-axis vs time"
plot "data.txt" using 4:5 with lines lw 2.5 lc 22 title 'Vy vs T' , \
    "outputfile" using 4:5 pt 7 ps 3

unset multiplot
EOF
    """.format(int(frame))
        os.system(cmd)



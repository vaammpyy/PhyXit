import matplotlib.pyplot as plt
import os
import pandas as pd

import subprocess

def make_movie():
    cmd='ffmpeg -framerate 5 -start_number 0 -i ./%05d.jpeg -vcodec mpeg4 -vb 20M '+'movie.mp4'
    os.system(cmd)
    os.system("rm -r ./*.jpeg")

def plot_projectile():
    data = pd.read_csv('data.txt', delimiter=' ').to_numpy().T
    frames=data[0]-1
    t=data[1]
    x=data[2]
    y=data[3]
    vx=data[4]
    vy=data[5]

    #os.system("mkdir output_plot")


    for frame in frames:
        os.system("awk 'FNR == %d {print $0}' data.txt > outputfile"%(int(frame)))
        cmd="""
gnuplot <<- EOF
set terminal jpeg size 1200,1000
set output "{:05d}.jpeg"

set multiplot title "Plot_something_something"
set nokey

set origin 0.0, 0.5
set size 1.0, 0.45
plot "data.txt" using 3:4 with lines lw 3 lc 22 title 'Position', \
    "outputfile" using 3:4 pt 7 ps 3

set origin 0.0, 0.0
set size 0.25, 0.45
plot "data.txt" using 2:3 with lines lw 3 lc 22 title 'X vs T' , \
    "outputfile" using 2:3 pt 7 ps 3

set origin 0.25, 0.0
set size 0.25, 0.45
plot "data.txt" using 2:4 with lines lw 3 lc 22 title 'Y vs T' , \
    "outputfile" using 2:4 pt 7 ps 3

set origin 0.5, 0.0
set size 0.25, 0.45
plot "data.txt" using 2:5 with lines lw 3 lc 22 title 'Vx vs T' , \
    "outputfile" using 2:5 pt 7 ps 3

set origin 0.75, 0.0
set size 0.25, 0.45
plot "data.txt" using 2:6 with lines lw 3 lc 22 title 'Vy vs T' , \
    "outputfile" using 2:6 pt 7 ps 3

unset multiplot
EOF

""".format(int(frame))
        os.system(cmd)
        


plot_projectile()
make_movie()

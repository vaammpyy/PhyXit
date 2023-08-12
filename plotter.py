import matplotlib.pyplot as plt
import os
import pandas as pd

def make_movie():
    cmd='ffmpeg -framerate 5 -start_number 0 -i ./%05d.jpg -vcodec mpeg4 -vb 20M '+'movie.mp4'
    os.system(cmd)
    os.system("rm -r ./*.jpg")

def plot_projectile():
    data = pd.read_csv('data.txt', delimiter=' ').to_numpy().T
    frames=data[0]-1
    t=data[1]
    x=data[2]
    y=data[3]
    vx=data[4]
    vy=data[5]

    for frame in frames:
        fig=plt.figure(figsize=(25,20),facecolor='white')

        fig.suptitle(f"Time={t[int(frame)]:.3f}", fontsize=30)

        gs = fig.add_gridspec(2,4)
        ax1 = fig.add_subplot(gs[1, 0])
        ax2 = fig.add_subplot(gs[1, 1])
        ax3 = fig.add_subplot(gs[1, 2])
        ax4 = fig.add_subplot(gs[1, 3])
        ax5 = fig.add_subplot(gs[0, :])

        ax5.scatter(x[int(frame)],y[int(frame)],color='red',edgecolors='black',s=50)
        ax5.plot(x,y,'--k')
        ax5.set_xlabel("X-axis",fontsize=24)
        ax5.set_ylabel("Y-axis",fontsize=24)

        ax1.plot(t,x,'--k')
        ax1.scatter(t[int(frame)],x[int(frame)],color='red',edgecolors='black',s=50)
        ax1.set_xlabel("Time",fontsize=24)
        ax1.set_ylabel("X",fontsize=24)

        ax2.plot(t,y,'--k')
        ax2.scatter(t[int(frame)],y[int(frame)],color='red',edgecolors='black',s=50)
        ax2.set_xlabel("Time",fontsize=24)
        ax2.set_ylabel("Y",fontsize=24)

        ax3.plot(t,vx,'--k')
        ax3.scatter(t[int(frame)],vx[int(frame)],color='red',edgecolors='black',s=50)
        ax3.set_xlabel("Time",fontsize=24)
        ax3.set_ylabel("VX",fontsize=24)

        ax4.plot(t,vy,'--k')
        ax4.scatter(t[int(frame)],vy[int(frame)],color='red',edgecolors='black',s=50)
        ax4.set_xlabel("Time",fontsize=24)
        ax4.set_ylabel("VY",fontsize=24)

        plt.tight_layout()

        plt.savefig("{:05d}.jpg".format(int(frame)),dpi=50)
        plt.close()



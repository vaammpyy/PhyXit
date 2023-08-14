import matplotlib.pyplot as plt
import os
import pandas as pd
import numpy as np

def make_movie():
    cmd='ffmpeg -framerate 5 -start_number 0 -i ./tmp/%05d.jpg -vcodec mpeg4 -vb 20M '+'./tmp/movie.mp4'
    os.system(cmd)
    os.system("rm -r ./tmp/*.jpg")

def plot_projectile():
    data = pd.read_csv('./tmp/data.txt', delimiter=' ').to_numpy().T
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

        ax5.scatter(x[int(frame)],y[int(frame)],color='red',edgecolors='black',s=200)
        ax5.plot(x[:int(frame)+1],y[:int(frame)+1],'--k')
        ax5.set_xlim([np.min(x)-1,np.max(x)+1])
        ax5.set_ylim([np.min(y)-1,np.max(y)+1])
        ax5.set_xlabel("X-axis",fontsize=24)
        ax5.set_ylabel("Y-axis",fontsize=24)

        ax1.plot(t,x,'--k')
        ax1.scatter(t[int(frame)],x[int(frame)],color='red',edgecolors='black',s=200)
        ax1.set_xlabel("Time",fontsize=24)
        ax1.set_ylabel("X",fontsize=24)

        ax2.plot(t,y,'--k')
        ax2.scatter(t[int(frame)],y[int(frame)],color='red',edgecolors='black',s=200)
        ax2.set_xlabel("Time",fontsize=24)
        ax2.set_ylabel("Y",fontsize=24)

        ax3.plot(t,vx,'--k')
        ax3.scatter(t[int(frame)],vx[int(frame)],color='red',edgecolors='black',s=200)
        ax3.set_xlabel("Time",fontsize=24)
        ax3.set_ylabel("VX",fontsize=24)

        ax4.plot(t,vy,'--k')
        ax4.scatter(t[int(frame)],vy[int(frame)],color='red',edgecolors='black',s=200)
        ax4.set_xlabel("Time",fontsize=24)
        ax4.set_ylabel("VY",fontsize=24)

        plt.tight_layout()

        plt.savefig("./tmp/{:05d}.jpg".format(int(frame)),dpi=50)
        plt.close()

def plot_simple_pendulum():
    data = pd.read_csv('./tmp/./tmp/data.txt', delimiter=' ').to_numpy().T
    # print(data[0])
    frames=data[0]-1
    t=data[1]
    th=data[3]
    dth=data[4]
    x=data[5]
    y=data[6]
    k=data[7]
    p=data[8]

    for frame in frames:
        fig=plt.figure(figsize=(25,20),facecolor='white')

        fig.suptitle(f"Time={t[int(frame)]:.3f}", fontsize=30)

        gs = fig.add_gridspec(3,2)
        ax1 = fig.add_subplot(gs[0,0])
        ax2 = fig.add_subplot(gs[0,1])
        ax3 = fig.add_subplot(gs[1,0])
        ax4 = fig.add_subplot(gs[1,1])
        ax5 = fig.add_subplot(gs[2,0])
        ax6 = fig.add_subplot(gs[2,1])

        ax1.scatter(x[int(frame)],y[int(frame)],color='red',edgecolors='black',s=200)
        ax1.plot(x[:int(frame)+1],y[:int(frame)+1],'--k')
        ax1.plot([0,x[int(frame)]],[0,y[int(frame)]],'blue')
        ax1.set_xlabel("X-axis",fontsize=24)
        ax1.set_ylabel("Y-axis",fontsize=24)

        ax2.plot(t,th,'--k')
        ax2.scatter(t[int(frame)],th[int(frame)],color='red',edgecolors='black',s=200)
        ax2.set_xlabel("Time",fontsize=24)
        ax2.set_ylabel(r"$\theta$",fontsize=24)

        ax3.plot(t,dth,'--k')
        ax3.scatter(t[int(frame)],dth[int(frame)],color='red',edgecolors='black',s=200)
        ax3.set_xlabel("Time",fontsize=24)
        ax3.set_ylabel(r"$\dot{\theta}$",fontsize=24)

        ax4.plot(t,k,'--k')
        ax4.scatter(t[int(frame)],k[int(frame)],color='red',edgecolors='black',s=200)
        ax4.set_xlabel("Time",fontsize=24)
        ax4.set_ylabel("KE",fontsize=24)

        ax5.plot(t,p,'--k')
        ax5.scatter(t[int(frame)],p[int(frame)],color='red',edgecolors='black',s=200)
        ax5.set_xlabel("Time",fontsize=24)
        ax5.set_ylabel("PE",fontsize=24)

        ax6.plot(th,dth,'--k')
        ax6.scatter(th[int(frame)],dth[int(frame)],color='red',edgecolors='black',s=200)
        ax6.set_xlabel(r"$\theta$",fontsize=24)
        ax6.set_ylabel(r"$\dot{\theta}$",fontsize=24)

        plt.tight_layout()

        plt.savefig("./tmp/{:05d}.jpg".format(int(frame)),dpi=50)
        plt.close()

def plot_spring_block():
    data = pd.read_csv('./tmp/data.txt', delimiter=' ').to_numpy().T
    frames=data[0]-1
    t=data[1]
    x0=data[2]
    x=data[3]
    y=data[4]
    vx=data[5]
    k=data[6]
    p=data[7]

    for frame in frames:
        fig=plt.figure(figsize=(25,20),facecolor='white')

        fig.suptitle(f"Time={t[int(frame)]:.3f}", fontsize=30)

        gs = fig.add_gridspec(3,2)
        ax1 = fig.add_subplot(gs[0,0])
        ax2 = fig.add_subplot(gs[0,1])
        ax3 = fig.add_subplot(gs[1,0])
        ax4 = fig.add_subplot(gs[1,1])
        ax5 = fig.add_subplot(gs[2,0])
        ax6 = fig.add_subplot(gs[2,1])

        ax1.plot([0,x[int(frame)]+x0[int(frame)]],[0,y[int(frame)]],'blue')
        ax1.scatter(x[int(frame)]+x0[int(frame)],y[int(frame)],color='red',edgecolors='black',s=200,marker='s')
        #ax1.plot(x,y,'--k')
        ax1.set_xlim([-1+np.min(x),1+np.max(x)])
        ax1.set_xlabel("X-axis",fontsize=24)
        ax1.set_ylabel("Y-axis",fontsize=24)

        ax2.plot(t,x,'--k')
        ax2.scatter(t[int(frame)],x[int(frame)],color='red',edgecolors='black',s=200)
        ax2.set_xlabel("Time",fontsize=24)
        ax2.set_ylabel("X",fontsize=24)

        ax3.plot(t,vx,'--k')
        ax3.scatter(t[int(frame)],vx[int(frame)],color='red',edgecolors='black',s=200)
        ax3.set_xlabel("Time",fontsize=24)
        ax3.set_ylabel("VX",fontsize=24)

        ax4.plot(t,k,'--k')
        ax4.scatter(t[int(frame)],k[int(frame)],color='red',edgecolors='black',s=200)
        ax4.set_xlabel("Time",fontsize=24)
        ax4.set_ylabel("KE",fontsize=24)

        ax5.plot(t,p,'--k')
        ax5.scatter(t[int(frame)],p[int(frame)],color='red',edgecolors='black',s=200)
        ax5.set_xlabel("Time",fontsize=24)
        ax5.set_ylabel("PE",fontsize=24)

        ax6.plot(x,vx,'--k')
        ax6.scatter(x[int(frame)],vx[int(frame)],color='red',edgecolors='black',s=200)
        ax6.set_xlabel("X",fontsize=24)
        ax6.set_ylabel("VX",fontsize=24)

        plt.tight_layout()

        plt.savefig("./tmp/{:05d}.jpg".format(int(frame)),dpi=50)
        plt.close()
    
def plot_random_walker():
    data=np.load("./tmp/data.npy",allow_pickle=True).item()
    frames=data['frame']
    x_min=np.min(np.ndarray.flatten(np.array(data['x'])))-1
    x_max=np.max(np.ndarray.flatten(np.array(data['x'])))+1
    y_min=np.min(np.ndarray.flatten(np.array(data['y'])))-1
    y_max=np.max(np.ndarray.flatten(np.array(data['y'])))+1
    for frame in frames:
        x_all=np.array(data['x'][frame])
        y_all=np.array(data['y'][frame])
        fig=plt.figure(figsize=(25,20),facecolor='white')
        fig.suptitle(f"Steps={int(frame)}", fontsize=30)
        gs = fig.add_gridspec(2,1)
        ax1 = fig.add_subplot(gs[0,0])
        ax2 = fig.add_subplot(gs[1,0])
        ax1.set_xlim([x_min,x_max])
        ax1.set_ylim([y_min,y_max])
        n=np.sqrt(x_max**2+y_max**2)
        for i in range(n):
            ax1.scatter(x_all[i],y_all[i],color='red',edgecolors='black',s=200)
            ax1.set_xlabel("X-axis",fontsize=24)
            ax1.set_ylabel("Y-axis",fontsize=24)

            ax2.hist(np.sqrt(x_all**2+y_all**2),alpha=0.5,color='red')
            ax2.set_ylim([0,n])
            ax2.set_xlim([0,n])
            ax2.set_xlabel("Radial distance",fontsize=24)
            ax2.set_ylabel("# particles",fontsize=24)
            #plt.scatter(x[0],y[0],color='green',edgecolors='black',s=200)
        plt.tight_layout()
        plt.savefig("./tmp/{:05d}.jpg".format(int(frame)),dpi=50)
        plt.close()

def plot_charge_interaction():
    data = pd.read_csv('./tmp/data.txt', delimiter=' ').to_numpy().T
    frames=data[0]-1
    t=data[1]
    q1=data[2]
    qx1=data[3]
    qy1=data[4]
    q2=data[5]
    qx2=data[6]
    qy2=data[7]
    qp=data[8]
    xp=data[9]
    yp=data[10]
    vxp=data[11]
    vyp=data[12]
    k=data[13]
    p=data[14]

    for frame in frames:
        fig=plt.figure(figsize=(25,20),facecolor='white')

        fig.suptitle(f"Time={t[int(frame)]:.3f}", fontsize=30)

        gs = fig.add_gridspec(2,4)
        ax1 = fig.add_subplot(gs[1, 0])
        ax2 = fig.add_subplot(gs[1, 1])
        ax3 = fig.add_subplot(gs[1, 2])
        ax4 = fig.add_subplot(gs[1, 3])
        ax5 = fig.add_subplot(gs[0, :])

        frm=int(frame)


        if q1[frm]>0:
            c1='blue'
        else:
            c1='red'
        ax5.scatter(qx1[frm],qy1[frm],color=c1,edgecolors='k',s=200*abs(int(q1[frm])))

        if q2[frm]>0:
            c2='blue'
        else:
            c2='red'
        ax5.scatter(qx2[frm],qy2[frm],color=c2,edgecolors='k',s=200*abs(int(q2[frm])))

        ax5.scatter(xp[frm],yp[frm],color='yellow',edgecolors='k',s=200)
        ax5.plot(xp[:frm+1],yp[:frm+1],color='yellow')
        ax5.set_xlabel("X-axis",fontsize=24)
        ax5.set_ylabel("Y-axis",fontsize=24)

        ax1.plot(t,vxp,'--k')
        ax1.scatter(t[frm],vxp[frm],color='yellow',edgecolors='k',s=200)
        ax1.set_xlabel("Time",fontsize=24)
        ax1.set_ylabel("VX",fontsize=24)

        ax2.plot(t,vyp,'--k')
        ax2.scatter(t[frm],vyp[frm],color='yellow',edgecolors='k',s=200)
        ax2.set_xlabel("Time",fontsize=24)
        ax2.set_ylabel("VX",fontsize=24)

        ax3.plot(t,k,'--k')
        ax3.scatter(t[frm],k[frm],color='yellow',edgecolors='k',s=200)
        ax3.set_xlabel("Time",fontsize=24)
        ax3.set_ylabel("KE",fontsize=24)

        ax4.plot(t,p,'--k')
        ax4.scatter(t[frm],p[frm],color='yellow',edgecolors='k',s=200)
        ax4.set_xlabel("Time",fontsize=24)
        ax4.set_ylabel("PE",fontsize=24)

        plt.tight_layout()

        plt.savefig("./tmp/{:05d}.jpg".format(int(frame)),dpi=50)
        plt.close()
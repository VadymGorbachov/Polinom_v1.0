from pylab import *
import numpy as np
import scipy as sp
pointsx=[]
pointsy=[]
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlim([0, 6])
ax.set_ylim([0, 6])
plt.title("Interpolation (any key for build)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
m=3

def onclick(event):
    plt.scatter(event.xdata, event.ydata, 15)
    pointsx.append(float(event.xdata))
    pointsy.append(float(event.ydata))
    fig.canvas.draw()

def calcs(event):
    calc_mnk()
    calc_polinom_MNK()
    method_Lagranga()

def calc_mnk():
    pointsxy = [len(pointsx)]
    pointsxx = [len(pointsx)]
    for i in range(len(pointsx)-1):
        pointsxy.append(pointsx[i]*pointsy[i])
    for i in range(len(pointsx)):
        pointsxx.append(pointsx[i]*pointsx[i])
    sumxy=0
    for i in range(len(pointsxy)):
        sumxy=sumxy+pointsxy[i]
    sumx=0
    for i in range(len(pointsx)):
        sumx=sumx+pointsx[i]
    sumy=0
    for i in range(len(pointsy)):
        sumy = sumy + pointsy[i]
    sumxx=0
    for i in range(len(pointsxx)):
        sumxx = sumxx + pointsxx[i]
    a=(len(pointsx)*sumxy-sumx*sumy)/(len(pointsx)*sumxx-(sumx*sumx))
    b=(sumy-a*sumx)/len(pointsx)
    x = linspace(0, 6, 50)
    plot(x,a*x+b,label ='Line')
    ax.legend()
    fig.canvas.draw()

def calc_polinom_MNK():
    fx = sp.linspace(0,6,50)
    fp, residuals, rank, sv, rcond = sp.polyfit(pointsx, pointsy, m, full=True)
    f = sp.poly1d(fp)
    plot(fx, f(fx,),label ='MNK')
    fig.canvas.draw()

def method_Lagranga():
    def lagranz(t):
        z = 0
        for j in range(len(pointsy)):
            p1 = 1;
            p2 = 1
            for i in range(len(pointsx)):
                if i == j:
                    p1 = p1 * 1;
                    p2 = p2 * 1
                else:
                    p1 = p1 * (t - pointsx[i])
                    p2 = p2 * (pointsx[j] - pointsx[i])
            z = z + pointsy[j] * p1 / p2
        return z

    xnew = np.linspace(0, 6, 100)
    ynew = [lagranz(i) for i in xnew]
    plot(xnew, ynew,label="Lagrange")
    ax.legend()
    plt.show()

cid = fig.canvas.mpl_connect('button_press_event', onclick)
cid = fig.canvas.mpl_connect('key_press_event', calcs)
plt.show()
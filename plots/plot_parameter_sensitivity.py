import numpy as np
import pandas as pd
import math as m
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

x = np.arange(1,1000,1)


def plotalpha():
    alpha = np.arange(10,10000,1)
    alpha = 1 / alpha
    fig, ax = plt.subplots()
    wr = np.arange(100,500,100)
    
    for r in wr:
        y = [ks(a,r) for a in alpha]

        ax.plot(alpha,y,label="$r$ = "+str(r))
        
    ax.set_xscale("log")
    ax.legend()
    ax.set(xlabel=r'$\alpha$', ylabel='Required Distance')
    plt.show()
    fig.savefig("ps_ks_alpha.eps",dpi=1000, format='eps',quality=95)
    
def plotr():
    x = np.arange(1,1000,1) 
    alphas = [0.1,0.01,0.001,0.0001]
    fig, ax = plt.subplots()

    for alpha in alphas:
        y = [ks(alpha,int(r)) for r in x]
        ax.plot(x, y,label=r"$\alpha$ = "+str(alpha))
    

    ax.set_xscale("log")
    ax.set(xlabel='Window Size $r$', ylabel='Required Distance') 
    ax.legend()
    plt.show()
    fig.savefig("ps_ks_r.eps",dpi=1000, format='eps',quality=95)


def ks(alpha,r):
    return m.sqrt(-1*(m.log(alpha))/(r))

plotalpha()
plotr()


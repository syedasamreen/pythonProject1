''' Discreate distribution
-> Binomial distribution
-> Poisson distribution'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import sys
import seaborn as sns
from scipy import stats


sys.path.append(os.path.join('..','..','Utilities'))
try:
    from ISP_style import setFonts, showData
except ImportError:
    def setFonts(*options):
        return
    def showData(*options):
        plt.show()
        return
sns.set(context = 'poster',style = 'ticks')
sns.set_palette(sns.color_palette('hls',3))
setFonts(24)

#### binimial dist #####
def showbinom():
    '''Binomial dist plot'''
    ns = [20,20,40]
    ps = [0.5,0.7,0.5]
    for (p,n) in zip(ps,ns):
        bd = stats.binom(n,p)
        x = np.arange(n+1)
        plt.plot(x,bd.pmf(x),'o--',label='p={0:3.1f},n={1}'.format(p,n))
    plt.legend()
    plt.title('Binomial distribution')
    plt.xlabel('X')
    plt.ylabel('p(x)')
    plt.annotate('Upper Limit', xy=(20,0),xytext=(27,0.04),arrowprops=dict(shrink=0.05))
    showData('bino_dist.png')

######### poisson distribution ###########
def showpoisson():
    '''poisson dist plot'''
    lamdas = [1,4,10]
    k = np.arange(20)
    markersize = 8
    for par in lamdas:
        plt.plot(k,stats.poisson.pmf(k,par),'o--',label='$\lambda={0}$'.format(par))
    plt.legend()
    plt.title('Poisson distribution')
    plt.xlabel('X')
    plt.ylabel('P(x)')
    showData('poisson_dist.png')

######## poisson views ######33
def show_poisson_views():
    """Show different views of a Poisson distribution"""

    sns.set_palette(sns.color_palette('muted'))

    fig, ax = plt.subplots(3, 1)

    k = np.arange(25)
    pd = stats.poisson(10)
    setFonts(12)

    ax[0].plot(k, pd.pmf(k), 'x-')
    ax[0].set_title('Poisson distribution', fontsize=24)
    ax[0].set_xticklabels([])
    ax[0].set_ylabel('PMF (X)')

    ax[1].plot(k, pd.cdf(k))
    ax[1].set_xlabel('X')
    ax[1].set_ylabel('CDF (X)')

    y = np.linspace(0, 1, 100)
    ax[2].plot(y, pd.ppf(y))
    ax[2].set_xlabel('X')
    ax[2].set_ylabel('PPF (X)')

    plt.tight_layout()
    plt.show()
print(show_poisson_views())
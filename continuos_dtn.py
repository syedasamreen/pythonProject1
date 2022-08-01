''' Countinous distribution functions.
-> T-dist
-> F-dist
-> chi2-dist
->Exponetial
->Weibull'''

# Import standard packages
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns
import os
import sys
sys.path.append(os.path.join('..','..','Utilities'))

try:
    from ISP_mystyle import showData
except ImportError:
    def showData(*options):
        plt.show()
        return
sns.set(context = 'poster',style = 'ticks',palette = 'muted',font_scale = 1.5)
def showT():
    '''Utility function to show T dist'''
    t = np.arange(-5,5,0.05)
    tvals = [1,5]
    normal = stats.norm.pdf(t)
    t1 = stats.t.pdf(t,1)
    t2 = stats.t.pdf(t,5)
    plt.plot(t,normal,'--',label = 'normal')
    plt.plot(t,t1,label = 'df=1')
    plt.plot(t,t2,label= 'df=5')
    plt.legend()
    plt.xlim(-5,5)
    plt.xlabel("X")
    plt.ylabel('pdf(x)')
    plt.axis('tight')
    outfile = 'dist_t.png'
    showData(outfile)

#######  Chi-square dist ########

def showchi2():
    '''Utility function for chi2 dist'''
    t = np.arange(0,8,0.05)
    chi2vals = [1,2,3,5]
    for chi2 in chi2vals:
        plt.plot(t,stats.chi2.pdf(t,chi2),label = 'k={0}'.format(chi2))
    plt.legend()
    plt.xlim(0,8)
    plt.xlabel('X')
    plt.ylabel('pdf(x)')
    plt.axis('tight')
    out_file='dist_chi2.png'
    showData(out_file)


########### F distribution #########
def showF():
    '''Utility function show F distribution'''
    t = np.arange(0,3,0.01)
    d1s = [1,2,5,100]
    d2s = [1,1,2,100]
    for (d1,d2) in zip(d1s,d2s):
        plt.plot(t,stats.f.pdf(t,d1,d2),label = 'F({0}/{1})'.format(d1,d2))
    plt.legend()
    plt.xlim(0,3)
    plt.xlabel('X')
    plt.ylabel('pdf(x)')
    plt.axis('tight')
    plt.legend()
    outfile = 'dist_f.png'
    showData(outfile)

#####   exponetial distribution #######
def showExp():
    '''Utility function to show exponential distribution'''
    t = np.arange(0,3,0.01)
    lambdas = [0.5,1,1.5]
    for par in lambdas:
        plt.plot(t,stats.expon.pdf(t,0,par),label = '$\lambda ={0:3.1f}$'.format(par))
    plt.legend()
    plt.xlim(0,3)
    plt.xlabel('X')
    plt.ylabel('pdf(x)')
    plt.axis('tight')
    plt.legend()
    outfile = 'dist_exp.png'
    showData(outfile)

###### weibull distribution #########
def showWeibull():
    '''Utility function to show weibul distrubution'''
    t = np.arange(0,2.5,0.01)
    ks = [0.5,1,1.5,5]
    for k in ks:
        wd = stats.weibull_min(k)
        plt.plot(t,wd.pdf(t),label = 'k={0:0.1f}'.format(k))
    plt.xlim(0,2.5)
    plt.ylim(0,2.5)
    plt.xlabel('X')
    plt.ylabel('pdf(X)')
    plt.legend()
    outfile = 'weibull.png'
    showData(outfile)
print(showWeibull())

# if __name__ = '__main__':
#     showT()
#     showF()
#     showExp()
#     showWeibull()
#     showchi2()

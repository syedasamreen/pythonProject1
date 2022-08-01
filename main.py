import numpy as np
from scipy import stats
import pandas as pd
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt

def main():
    '''Define main function'''
    t = np.arange(0,10,0.1)
    x = np.sin(t)
    outfile = 'Sine.txt'
    np.savetxt(outfile, np.vstack([t,x]).T)
    indata = np.loadtxt(outfile)
    t2 = indata[:,0]
    x2 = indata[:,1]
    plt.plot(t2,x2)
    plt.title('Hit any key')
    plt.waitforbuttonpress()
    t = np.arange(-100,100)
    par = {'offset':100,'slope':0.5,'noiseAMP':4}
    x= par['offset']+par['slope']*t+ par['noiseAMP']*np.random.randn(len(t))
    xhigh = x[t>10]
    thigh = t[t>10]
    plt.close()
    plt.plot(thigh, xhigh)
    xmat = np.vstack((thigh, np.ones_like(thigh))).T
    slope,intercept = np.linalg.lstsq(xmat,xhigh)[0]
    # plt.(True)
    plt.plot(thigh,intercept+slope*thigh,'r')
    plt.title("hit any key to continue")
    plt.savefig('linefit.png',dpi=200)
    plt.waitforbuttonpress()
    plt.close()
    print(('Fit line: intercept = {0:5.3f}, and slope = {1:5.3f}'.format(intercept, slope)))
if __name__ == '__main__':
    main()
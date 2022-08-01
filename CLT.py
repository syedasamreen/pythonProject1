''' Practical demonstartion of the central limit theorem, based on uniform distribution'''
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import sys

sys.path.append(os.path.join('..','..','Utilities'))
try:
    from ISP_mystyle import setFonts, showData
except ImportError:
    def setfonts(*options):
        return
    def showData(*options):
        plt.show()
        return
    sns.set(context = 'poster',style = 'ticks',palette = 'muted')
    ndata = 1000
    nbins = 50
    def showashistogram(axis,data,title):
        '''subrouting and showing histogram it'''
        axis.hist(data,bins=nbins)
        axis.set_xticks([0,0.5,1])
        axis.set_title(title)
    def main():
        '''Demontrate the central limit theorem.'''
        setfonts(24)
        data = np.random.random(ndata)
        fig,axs = plt.subplots(1,3)
        showashistogram(axs[0],data,'Random data')
        showashistogram(axs[1],np.mean(data.reshape((ndata//2,2)),axis=1),'Average over 2')
        showashistogram(axs[2], np.mean(data.reshape((ndata//10,10)), axis=1), 'Average over 10')
        axs[0].set_ylabel('Counts')
        plt.tight_layout()
        showData('CentralLIMTtheorem.png')
if __name__ == '__main__':
    main()
''' Binomial test using http://en.wikipedia.org/wiki/Binomial_test'''
from scipy import stats

def binomial_test(checkVal):
    '''Binomial test'''
    n = 235
    p = 1.0/6
    bd = stats.binom(n,p)
    p_onetail = bd.sf(checkVal-1)
    p_twoTail = stats.binom_test(checkVal,n,p)
    return(p_onetail,p_twoTail)

# if __name__ == '__main__':
#     main()
checkVal = 51
p1,p2 = binomial_test(checkVal)
print('The chance that you roll {0} or more "6" is {1:5.3f}, and the chance of an event as extreme as {0} or more rolls is {2:5.3f}'.format(checkVal,p1,p2))
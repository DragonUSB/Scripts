import numpy as np
from matplotlib import pyplot as plt

def hl_envelopes_idx(s, dmin=1, dmax=1, split=False):
    """
    Input :
    s: 1d-array, data signal from which to extract high and low envelopes
    dmin, dmax: int, optional, size of chunks, use this if the size of the input signal is too big
    split: bool, optional, if True, split the signal in half along its mean, might help to generate the envelope in some cases
    Output :
    lmin,lmax : high/low envelope idx of input signal s
    """

    # locals min      
    lmin = (np.diff(np.sign(np.diff(s))) > 0).nonzero()[0] + 1 
    # locals max
    lmax = (np.diff(np.sign(np.diff(s))) < 0).nonzero()[0] + 1 
    

    if split:
        # s_mid is zero if s centered around x-axis or more generally mean of signal
        s_mid = np.mean(s) 
        # pre-sorting of locals min based on relative position with respect to s_mid 
        lmin = lmin[s[lmin]<s_mid]
        # pre-sorting of local max based on relative position with respect to s_mid 
        lmax = lmax[s[lmax]>s_mid]


    # global max of dmax-chunks of locals max 
    lmin = lmin[[i+np.argmin(s[lmin[i:i+dmin]]) for i in range(0,len(lmin),dmin)]]
    # global min of dmin-chunks of locals min 
    lmax = lmax[[i+np.argmax(s[lmax[i:i+dmax]]) for i in range(0,len(lmax),dmax)]]
    
    return lmin,lmax

# Example 1: quasi-periodic vibration

t = np.linspace(0,8*np.pi,5000)
s = 0.8*np.cos(t)**3 + 0.5*np.sin(np.exp(1)*t)
high_idx, low_idx = hl_envelopes_idx(s)

# plot
plt.plot(t,s,label='signal')
plt.plot(t[high_idx], s[high_idx], 'r', label='low')
plt.plot(t[low_idx], s[low_idx], 'g', label='high')
plt.grid(True)
plt.show()

# Example 2: noisy decaying signal

t = np.linspace(0,2*np.pi,5000)
s = 5*np.cos(5*t)*np.exp(-t) + np.random.rand(len(t))

high_idx, low_idx = hl_envelopes_idx(s,dmin=15,dmax=15)

# plot
plt.plot(t,s,label='signal')
plt.plot(t[high_idx], s[high_idx], 'r', label='low')
plt.plot(t[low_idx], s[low_idx], 'g', label='high')
plt.grid(True)
plt.show()
import sys
import numpy as np
import matplotlib.pyplot as plt
from multiprocessing import Process, Queue,set_start_method


def generateNoisyWave(times, freq, amp, noise):
    
    # This simplifies code later, this basically just creates our noise for us
    if(not isinstance(times, float)):
        noiseArray = noise * np.random.randn(len(times))
    else:
        noiseArray = noise * np.random.randn(1)
    
    
    sineWave = amp * np.sin(freq * 2 * np.pi * times)
    return sineWave + noiseArray

    

#times = np.linspace(0,1,srate) # One second at 250Hz
#y = generateNoisyWave(times, 3, 10, 2) # (time, Freq, Amp, Noise)

#plt.plot(times, y)
#plt.show()

import matplotlib.pyplot as plt
import numpy as np
import scipy
import wave
from IPython.display import Audio

def setup_graph(title='', x_label='', y_label='', fig_size=None):
    fig = plt.figure()
    if fig_size != None:
        fig.set_size_inches(fig_size[0], fig_size[1])
    ax = fig.add_subplot(111)
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

def bfsk_modulate(bit_array, space_freq, mark_freq, baud, sample_rate):
    seconds_per_bit = 1 / baud
    samples_per_bit = int(sample_rate * seconds_per_bit)
    t = np.linspace(0, seconds_per_bit, samples_per_bit, endpoint=False)
    signal = np.array([])
    for bit in bit_array:
        if bit == 0:
            space = np.sin(2 * np.pi * space_freq * t)
            signal = np.append(signal, space)
        elif bit == 1:
            mark = np.sin(2 * np.pi * mark_freq * t)
            signal = np.append(signal, mark)
    return signal

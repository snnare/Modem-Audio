import numpy as np
from scipy.signal import butter, lfilter
import matplotlib.pyplot as plt

# Generar una señal de ejemplo
t = np.linspace(0, 1, 1000, False)  # 1 segundo de señal
f = 100  # frecuencia de la señal en Hz
f1 = 40 
signal = np.sin(2 * np.pi * f * t)  + np.sin(2*np.pi * f *t)

# Diseñar el filtro Butterworth
order = 4  # orden del filtro
cutoff_freq = 10  # frecuencia de corte en Hz
nyquist_freq = 0.5 * 1000  # frecuencia de Nyquist (mitad de la frecuencia de muestreo)
normalized_cutoff = cutoff_freq / nyquist_freq  # frecuencia de corte normalizada
b, a = butter(order, normalized_cutoff, btype='low', analog=False)

# Aplicar el filtro a la señal
filtered_signal = lfilter(b, a, signal)

# Graficar la señal original y la señal filtrada
plt.plot(t, signal, label='Señal original')
plt.plot(t, filtered_signal, label='Señal filtrada')
plt.xlabel('Tiempo')
plt.ylabel('Amplitud')
plt.legend()
plt.show()

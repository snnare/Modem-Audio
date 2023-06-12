import numpy as np
from scipy.io import wavfile
from scipy.signal import butter, lfilter
import matplotlib.pyplot as plt

def butter_lowpass(cutoff, fs, order=1):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data, cutoff, fs, order=1):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y

# Cargar archivo .wav
filename = 'grabacion.wav'
fs, data = wavfile.read(filename)

# Parámetros del filtro
cutoff_freq = 5000.0  # Frecuencia de corte del filtro

# Aplicar el filtro pasa bajos
filtered_data = butter_lowpass_filter(data, cutoff_freq, fs, order=1)

# Guardar el archivo filtrado como .wav
filtered_filename = 'archivo_filtrado.wav'
wavfile.write(filtered_filename, fs, filtered_data.astype(np.int16))

# Visualizar los resultados
plt.figure()
plt.plot(data, label='Señal original')
plt.plot(filtered_data, label='Señal filtrada')
plt.xlabel('Muestras')
plt.ylabel('Amplitud')
plt.legend()
plt.show()

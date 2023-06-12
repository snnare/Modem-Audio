import numpy as np
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt

# Parámetros de la demodulación FSK
fs = 44100  # Frecuencia de muestreo en Hz
duracion_tono = 0.2  # Duración del tono en segundos
f0 = 1000  # Frecuencia de la señal portadora para el bit 0
f1 = 2000  # Frecuencia de la señal portadora para el bit 1

def demodular_señal(señal):
    bits_demodulados = []
    duracion_muestra = int(fs * duracion_tono)
    
    for i in range(0, len(señal), duracion_muestra):
        muestra = señal[i:i+duracion_muestra]
        
        # Calcular las correlaciones cruzadas con las señales portadoras
        correlacion_f0 = np.abs(np.correlate(muestra, np.sin(2 * np.pi * f0 * np.arange(duracion_muestra) / fs)))
        correlacion_f1 = np.abs(np.correlate(muestra, np.sin(2 * np.pi * f1 * np.arange(duracion_muestra) / fs)))
        
        # Comparar las correlaciones y determinar el bit correspondiente
        if np.mean(correlacion_f0) > np.mean(correlacion_f1):
            bits_demodulados.append(0)
        else:
            bits_demodulados.append(1)
    
    return bits_demodulados

# Cargar el archivo de audio .wav del transmisor
sample_rate, señal_audio = wav.read("transmisor.wav")

# Demodulación de la señal de audio
bits_demodulados = demodular_señal(señal_audio)

# Mostrar la cadena de bits demodulada
print("Cadena de bits demodulada:", bits_demodulados)


# Calcular la transformada de Fourier de la señal modulada
fft = np.fft.fft(señal_modulada)
frecuencias = np.fft.fftfreq(len(señal_modulada), d=1/fs)

# Graficar el espectro de frecuencia
plt.plot(frecuencias, np.abs(fft))
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Amplitud")
plt.title("Espectro de Frecuencia")
plt.show()

import numpy as np
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt
import sounddevice as sd

# Parámetros de la modulación FSK
fs = 44100  # Frecuencia de muestreo en Hz
duracion_tono = 0.2  # Duración del tono en segundos
f0 = 1000  # Frecuencia de la señal portadora para el bit 0
f1 = 2000  # Frecuencia de la señal portadora para el bit 1

def modular_bit(bit):
    if bit == 0:
        frecuencia_portadora = f0
    else:
        frecuencia_portadora = f1
    
    tiempo = np.linspace(0, duracion_tono, int(fs * duracion_tono), endpoint=False)
    signal_portadora= np.sin(2 * np.pi * frecuencia_portadora * tiempo)
    
    return signal_portadora

def modular_cadena(cadena):
    signal_modulada = np.array([], dtype=np.float32)
    
    for bit in cadena:
        signal_modulada = np.concatenate((signal_modulada, modular_bit(bit)))
       
    return signal_modulada

# Cadena de bits a modular
cadena_bits = [0, 1, 0, 1, 1, 0, 1]

# Modulación de la cadena de bits
señal_modulada = modular_cadena(cadena_bits)

# Guardar la señal modulada como archivo de audio .wav
wav.write("transmisor.wav", fs, señal_modulada)

# Graficar la señal modulada en el dominio del tiempo
tiempo = np.arange(0, len(señal_modulada)) / fs
sd.play(señal_modulada, fs)
sd.wait()


# Calcular la transformada de Fourier de la señal modulada
fft = np.fft.fft(señal_modulada)
frecuencias = np.fft.fftfreq(len(señal_modulada), d=1/fs)

# Graficar el espectro de frecuencia
plt.plot(frecuencias, np.abs(fft))
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Amplitud")
plt.title("Espectro de Frecuencia")
plt.show()
import numpy as np
import sounddevice as sd

# Parámetros de la señal
frecuencia_portadora = 10000  # Frecuencia de la señal portadora en Hz
tiempo_bit = 0.1  # Duración de cada bit en segundos
fs = 44100  # Frecuencia de muestreo

# Grabar la señal de audio desde la entrada de audio
duracion_grabacion = 5  # Duración en segundos
senal_grabada = sd.rec(int(duracion_grabacion * fs), samplerate=fs, channels=1)
sd.wait()

# Demodulación de la señal FM
t = np.arange(len(senal_grabada)) / fs
señal_demodulada = np.sin(2 * np.pi * frecuencia_portadora * t) * senal_grabada.flatten()

# Decodificar la señal demodulada en bits
bits_recuperados = []
for i in range(0, len(señal_demodulada), puntos_bit):
    promedio_bit = np.mean(señal_demodulada[i: i + puntos_bit])
    bit_recuperado = 1 if promedio_bit > 0 else 0
   
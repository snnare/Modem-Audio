import numpy as np
import sounddevice as sd
from scipy.io import wavfile

# Parámetros de la señal
frecuencia_portadora = 1000  # Frecuencia de la señal portadora en Hz
tiempo_bit = 0.1  # Duración de cada bit en segundos
fs = 44100  # Frecuencia de muestreo

# Obtener el mensaje de entrada
mensaje = input("Ingrese el mensaje a modular: ")

# Convertir el mensaje a una secuencia de bits
bits = []
for caracter in mensaje:
    bits.extend([int(bit) for bit in format(ord(caracter), '08b')])

# Duración de cada bit y número total de puntos en la señal
puntos_bit = int(fs * tiempo_bit)

# Generación de la señal portadora
t = np.arange(puntos_bit) / fs
portadora = np.sin(2 * np.pi * frecuencia_portadora * t)

# Generación de la señal modulada PSK
senal_modulada = np.zeros(len(bits) * puntos_bit)
for i, bit in enumerate(bits):
    fase = 2 * np.pi * bit / 2  # Fase de la portadora (0 o pi)
    senal_modulada[i * puntos_bit: (i + 1) * puntos_bit] = np.sin(2 * np.pi * frecuencia_portadora * t + fase)

# Reproducir la señal modulada
sd.play(senal_modulada, fs)

# Guardar la señal modulada en un archivo WAV
wavfile.write("senal_modulada.wav", fs, senal_modulada)

# Esperar a que termine la reproducción
sd.wait()
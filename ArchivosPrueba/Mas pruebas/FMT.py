import numpy as np
import sounddevice as sd

# Parámetros de la señal
frecuencia_portadora = 2000  # Frecuencia de la señal portadora en Hz
tiempo_bit = 0.1  # Duración de cada bit en segundos
fs = 44100  # Frecuencia de muestreo

# Mensaje a transmitir
mensaje = "Hola, esta es una prueba."

# Convertir el mensaje a una secuencia de bits
bits = []
for caracter in mensaje:
    bits.extend([int(bit) for bit in format(ord(caracter), '08b')])

# Duración de cada bit y número total de puntos en la señal
puntos_bit = int(fs * tiempo_bit)

# Generación de la señal portadora
t = np.arange(puntos_bit) / fs
portadora = np.sin(2 * np.pi * frecuencia_portadora * t)

# Generación de la señal modulada FM
senal_modulada = np.zeros(len(bits) * puntos_bit)
for i, bit in enumerate(bits):
    fase = 2 * np.pi * bit / 2  # Fase de la portadora (0 o pi)
    senal_modulada[i * puntos_bit: (i + 1) * puntos_bit] = np.sin(2 * np.pi * frecuencia_portadora * t + fase)

# Reproducir la señal modulada en la salida de audio
sd.play(senal_modulada, fs)
sd.wait()
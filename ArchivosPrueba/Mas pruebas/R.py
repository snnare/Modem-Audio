import numpy as np
import sounddevice as sd
from scipy.io import wavfile

# Parámetros de la señal
frecuencia_portadora = 1000  # Frecuencia de la señal portadora en Hz
tiempo_bit = 0.1  # Duración de cada bit en segundos
fs = 44100  # Frecuencia de muestreo

# Cargar la señal modulada desde el archivo WAV
fs_mod, senal_modulada = wavfile.read("senal_modulada.wav")

# Duración de cada bit y número total de puntos en la señal
puntos_bit = int(fs_mod * tiempo_bit)

# Generación de la señal portadora
t = np.arange(puntos_bit) / fs_mod
portadora = np.sin(2 * np.pi * frecuencia_portadora * t)

# Demodulación de la señal PSK
bits_demodulados = []
for i in range(0, len(senal_modulada), puntos_bit):
    producto = senal_modulada[i:i + puntos_bit] * portadora
    suma_producto = np.sum(producto)
    fase_promedio = np.angle(suma_producto)
    bit_demodulado = 0 if fase_promedio < np.pi else 1
    bits_demodulados.append(bit_demodulado)

# Convertir los bits demodulados a caracteres
mensaje_demodulado = ""
for i in range(0, len(bits_demodulados), 8):
    byte = bits_demodulados[i:i + 8]
    byte_str = "".join([str(bit) for bit in byte])
    if byte_str.startswith('0b'):
        byte_str = byte_str[2:]
    byte_int = int(byte_str, 2)
    caracter = chr(byte_int)
    mensaje_demodulado += caracter

# Imprimir el mensaje demodulado
print("Mensaje demodulado:", mensaje_demodulado)
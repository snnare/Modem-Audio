import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

def modular_FSK(bits, f0, f1, fs, duracion_tono):
    tiempo_bit = 1 / fs
    tiempo_total = tiempo_bit * len(bits)
    t = np.linspace(0, tiempo_total, int(tiempo_total * fs), endpoint=False)

    signal = np.zeros_like(t)

    for i, bit in enumerate(bits):
        if bit == '0':
            signal[i * int(tiempo_bit * fs): (i + 1) * int(tiempo_bit * fs)] = np.sin(2 * np.pi * f0 * t[i * int(tiempo_bit * fs): (i + 1) * int(tiempo_bit * fs)])
        elif bit == '1':
            signal[i * int(tiempo_bit * fs): (i + 1) * int(tiempo_bit * fs)] = np.sin(2 * np.pi * f1 * t[i * int(tiempo_bit * fs): (i + 1) * int(tiempo_bit * fs)])

    signal *= duracion_tono

    return t, signal


def texto_a_bits(texto):
    # Inicializar la cadena de bits vacía
    bits = ""

    # Iterar sobre cada carácter en el texto
    for caracter in texto:
        # Obtener el código ASCII del carácter
        codigo = ord(caracter)

        # Convertir el código ASCII a una representación binaria de 8 bits
        binario = bin(codigo)[2:].zfill(8)

        # Agregar el binario a la cadena de bits
        bits += binario

    return bits


# Ejemplo de uso
bits = texto_a_bits('H')
print(bits)
#bits = '110010101'  # Cadena de bits
f0 = 1000  # Frecuencia para el bit 0
f1 = 2000  # Frecuencia para el bit 1
fs = 44100  # Frecuencia de muestreo
duracion_tono = 0.1  # Duración del tono en segundos

t, signal = modular_FSK(bits, f0, f1, fs, duracion_tono)
sd.play(signal, samplerate= fs)
sd.wait()


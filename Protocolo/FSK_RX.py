import soundfile as sf
import sounddevice as sd
import numpy as np

fs = 960000  # Frecuencia de muestreo en Hz
duracion_tono = 0.2  # Duración del tono en segundos
f0 = 1000  # Frecuencia de la señal portadora para el bit 0
f1 = 2000  # Frecuencia de la señal portadora para el bit 1

def demodular_señal(señal, fs):
    bits_demodulados = []

    tiempo_muestreo = int(fs * duracion_tono)
    ventana = np.hanning(tiempo_muestreo)  # Aplicar ventana de Hamming para reducir el efecto de las discontinuidades en los extremos de la señal

    for i in range(0, len(señal), tiempo_muestreo):
        muestra = señal[i:i+tiempo_muestreo] * ventana

        frecuencia = np.fft.rfftfreq(len(muestra), d=1.0/fs)
        transformada = np.abs(np.fft.rfft(muestra))

        indice_f0 = np.argmax(transformada[np.where(frecuencia == f0)])
        indice_f1 = np.argmax(transformada[np.where(frecuencia == f1)])

        bit_demodulado = 0 if indice_f0 > indice_f1 else 1
        bits_demodulados.append(bit_demodulado)
    print(bits_demodulados)
    return bits_demodulados


# Aquí iría el código para recibir la señal de audio, por ejemplo, utilizando sounddevice y grabando la señal.

# Una vez que se tiene la señal grabada, se puede demodular:
señal_grabada, _ = sf.read('archivo_filtrado.wav')  # Leer la señal grabada desde el archivo WAV
bits_demodulados = demodular_señal(señal_grabada, fs)

# Convertir los bits demodulados a una cadena de texto
mensaje_demodulado = ""
for i in range(0, len(bits_demodulados), 8):
    byte = bits_demodulados[i:i+8]
    caracter = chr(int(''.join(map(str, byte)), 2))
    mensaje_demodulado += caracter

print("Mensaje demodulado:", mensaje_demodulado)

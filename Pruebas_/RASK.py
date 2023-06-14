import soundfile as sf
import numpy as np

fs = 18000  # Frecuencia de muestreo en Hz
duracion_tono = 0.3  # Duración de cada tono en segundos
f0 = 2000  # Frecuencia de la señal portadora para el bit 0
f1 = 3000  # Frecuencia de la señal portadora para el bit 1

def demodulate_signal(signal, fs):
    bits_demodulated = []

    muestras_por_tono = int(fs * duracion_tono)

    for i in range(0, len(signal), muestras_por_tono):
        tono = signal[i:i+muestras_por_tono]

        frecuencia = np.fft.rfftfreq(len(tono), d=1.0/fs)
        espectro = np.abs(np.fft.rfft(tono))

        indice_f0 = np.argmax(espectro[np.where(frecuencia == f0)])
        indice_f1 = np.argmax(espectro[np.where(frecuencia == f1)])

        bit_demodulado = 0 if indice_f0 > indice_f1 else 1
        bits_demodulated.append(bit_demodulado)

    return bits_demodulated


# Aquí agregarías el código para recibir la señal de audio, por ejemplo, utilizando sounddevice para grabar la señal.

# Una vez que tengas la señal grabada, puedes demodularla:
recorded_signal, _ = sf.read('ASK.wav')  # Lee la señal grabada desde el archivo WAV
bits_demodulated = demodulate_signal(recorded_signal, fs)

# Convertir los bits demodulados a una cadena de texto
mensaje_demodulado = ""
for i in range(0, len(bits_demodulated), 8):
    byte = bits_demodulated[i:i+8]
    character = chr(int(''.join(map(str, byte)), 2))
    mensaje_demodulado += character

print("Mensaje demodulado:", mensaje_demodulado)
